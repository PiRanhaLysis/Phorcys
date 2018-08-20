import base64
from functools import partial
from multiprocessing import Pool, Lock

from phorcys.decoders.deepdecoder import DeepDecoder
from phorcys.loaders import DumpLoader


class DumpInspector:
    def __init__(self, dump: DumpLoader, inspectors = []):
        self.dump = dump
        self.inspectors = inspectors

    def set_inspectors(self, inspectors):
        self.inspectors = inspectors

    def inspect(self):
        with Pool() as p:
            flows = p.map(self.inspect_flow, self.dump)
            p.close()
            p.join()
            self.dump.flows = flows

    def inspect_flow(self, f):
        # for f in self.dump:
        total = 0
        all_tags = []
        all_rules = []
        inspection_results = {}
        # Inspect URL
        dd = DeepDecoder()
        top_layer = dd.decode(f['request']['url'])
        count = 0
        for i in self.inspectors:
            count, tags, rules = i(top_layer)
            all_rules.append(rules)
            all_tags.extend(tags)
        inspection_results['url'] = {'layers': top_layer.dict(recursive = True), 'clues': count}
        total += count

        # Inspect Request payload
        if len(f['request']['content']) > 0:
            dd = DeepDecoder()
            top_layer = dd.decode(base64.b64decode(f['request']['content']))
            count = 0
            for i in self.inspectors:
                count, tags, rules = i(top_layer)
                all_rules.append(rules)
                all_tags.extend(tags)
            inspection_results['content'] = {'layers': top_layer.dict(recursive = True), 'clues': count}
            total += count

        # Inspect Response payload
        if len(f['response']['content']) > 0:
            dd = DeepDecoder()
            top_layer = dd.decode(base64.b64decode(f['response']['content']))
            count = 0
            for i in self.inspectors:
                count, tags, rules = i(top_layer)
                all_rules.append(rules)
                all_tags.extend(tags)
            inspection_results['response'] = {'layers': top_layer.dict(recursive = True), 'clues': count}
            total += count

        aggregated_rules = {}
        for r in all_rules:
            for k, v in r.items():
                if k not in aggregated_rules:
                    aggregated_rules[k] = v
                else:
                    aggregated_rules[k]['count'] += v['count']
        f['inspection'] = inspection_results
        f['inspection']['rules'] = aggregated_rules
        f['inspection']['clues'] = total
        f['inspection']['tags'] = list(set(all_tags))

        return f
