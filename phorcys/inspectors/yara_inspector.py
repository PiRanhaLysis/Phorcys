import yara

from phorcys.decoders.base import Layer


class YaraInspector:
    def __init__(self, rules: str):
        self.layer = None
        self.rules = yara.compile(source = rules)

    def __call__(self, layer: Layer, *args, **kwargs):
        tags = []
        rules = {}
        self.layer = layer
        count = 0
        leaves = self.layer.leaves
        for l in leaves:
            data = l.raw_data
            if type(data) is not str:
                data = str(data)
            matches = self.rules.match(data = data)
            if len(matches) > 0:
                count += 1
                for m in matches:
                    if str(m) not in rules:
                        rules[str(m)] = {'rule': str(m), 'tags': m.tags, 'count': len(m.strings)}
                    else:
                        rules[str(m)]['count'] += len(m.strings)
                    l.add_matching_rule({'rule': str(m), 'tags': m.tags, 'count': len(m.strings)})
                    tags.extend(m.tags)
        return count, list(set(tags)), rules
