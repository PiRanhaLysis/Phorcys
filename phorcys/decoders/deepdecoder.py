import os
from os import path
from os.path import expanduser
from typing import Optional

from yapsy.PluginManager import PluginManager

from phorcys.decoders import utils
from phorcys.decoders.base import Layer
from phorcys.decoders.base64 import Base64
from phorcys.decoders.bzip import Bzip
from phorcys.decoders.css import Css
from phorcys.decoders.gzip import Gzip
from phorcys.decoders.html import Html
from phorcys.decoders.http_headers import HttpHeaders
from phorcys.decoders.json import Json
from phorcys.decoders.lzma import Lzma
from phorcys.decoders.protobuf import Protobuf
from phorcys.decoders.text import Text
from phorcys.decoders.urlencoded import UrlEncoded
from phorcys.decoders.zlib import Zlib
from phorcys.plugins.decoder import DecoderPlugin


class DeepDecoder:
    def __init__(self):
        self.top_layer = None
        self.plugin_manager = PluginManager()
        self.plugin_locations = [path.join(expanduser("~"), '.phorcys', 'plugins')]
        try:
            environ_locations = os.environ['PLUGINS_DIR']
            if environ_locations is not None and len(environ_locations) > 0:
                dirs = environ_locations.split(';')
                for d in dirs:
                    if os.path.isdir(d):
                        self.plugin_locations.append(d)
                    else:
                        pass
        except KeyError:
            pass
        self.plugin_manager.setPluginPlaces(directories_list=self.plugin_locations)
        self.plugin_manager.setCategoriesFilter(DecoderPlugin.filter())
        self.plugin_manager.collectPlugins()

    def get_loaded_plugins(self):
        return self.plugin_manager.getPluginsOfCategory(DecoderPlugin.category())

    def _complete_leaves(self):
        for leaf in self.top_layer.leaves:
            if leaf.parent is not None and leaf.parent.name == 'base64' and len(leaf.name) == 0:
                leaf.parent.name = 'text'
                leaf.parent.human_readable = True
                leaf.parent.raw_data = ''.join(leaf.parent.lines)
                leaf.parent.del_extracted_layer(leaf)
                continue
            if len(leaf.lines) == 0:
                try:
                    leaf.lines = utils.to_hex_lines(bytes(leaf.raw_data))
                    leaf.name = 'raw'
                except Exception as e:
                    pass

    def decode(self, data, **kwargs) -> Layer:
        parent = Layer()
        parent.raw_data = data
        parent.name = 'root'
        to_visit = [parent]
        while len(to_visit) != 0:
            next = to_visit.pop()
            layer = self.go_deeper(next, **kwargs)
            if layer is not None:
                layers = layer.extracted_layers
                if layers is not None:
                    to_visit.extend(layers)

        self.top_layer = parent
        self._complete_leaves()
        return parent

    def inspect(self):
        pass

    def go_deeper(self, parent, **xargs) -> Optional[Layer]:
        protocols = [
            HttpHeaders(),
            UrlEncoded(),
            Json(),
            Protobuf(),
            Base64(),
            Lzma(),
            Zlib(),
            Bzip(),
            Gzip(),
            Text(),
            Html(),
            Css(),
        ]

        plugins = []
        for plugin in self.plugin_manager.getPluginsOfCategory(DecoderPlugin.category()):
            plugins.append(plugin.plugin_object)

        plugins.extend(protocols)
        protocols = plugins

        for p in protocols:
            try:
                return p(parent, **xargs)
            except Exception as e:
                # print(traceback.format_exc())
                # print('Not %s' % type(p))
                # print(e)
                pass

        return None
