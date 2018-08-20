#!/usr/bin/env python3
import argparse
import sys
from datetime import datetime
from phorcys.decoders.deepdecoder import DeepDecoder
from phorcys.inspectors.dump_inspector import DumpInspector
from phorcys.inspectors.yara_inspector import YaraInspector
from phorcys.loaders.flow import FlowLoader

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'Recursive network payloads decoder.')
    parser.add_argument('-y', dest = 'yara_file', action = 'store',
                        help = 'path to file containing Yara rules')
    parser.add_argument('-f', dest = 'flow_file', action = 'store',
                        help = 'path to the MITM dump (.flow)')
    parser.add_argument('-b', dest = 'binary_file', action = 'store',
                        help = 'path to the file containing the payload to decode')
    parser.add_argument('-p', dest = 'list_plugins', action = 'store_true',
                        help = 'list loaded plugins')

    args = parser.parse_args()

    flow_file_mode = args.flow_file is not None
    yara_mode = args.yara_file is not None
    binary_mode = args.binary_file is not None
    plugin_mode = args.list_plugins

    if plugin_mode:
        dd = DeepDecoder()
        for p in dd.get_loaded_plugins():
            print(' - %s - %s' % (p.name, p.description))
        sys.exit(0)

    if not flow_file_mode and not binary_mode:
        print('One of -f or -b is required')
        parser.print_help()
        sys.exit(32)

    inspectors = []

    if yara_mode:
        inspectors.append(YaraInspector(open(args.yara_file, 'r').read()))

    if flow_file_mode:
        start_time = datetime.now()
        flows = FlowLoader(args.flow_file)
        flows.load()
        di = DumpInspector(flows, inspectors)
        di.inspect()
        time_elapsed = datetime.now() - start_time
        print('Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed), file=sys.stderr)
        print(flows.json(indent = 2))

    if binary_mode:
        dd = DeepDecoder()
        payload = dd.decode(open(args.binary_file, mode = 'rb').read())
        if yara_mode:
            inspectors[0](payload)
        print(payload)
