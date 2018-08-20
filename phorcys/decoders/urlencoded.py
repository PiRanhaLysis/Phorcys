from typing import Optional

from mitmproxy.net.http import url

from phorcys.decoders.base import Layer
from phorcys.plugins.decoder import DecoderPlugin


class UrlEncoded(DecoderPlugin):
    def __call__(self, parent: Layer, **metadata) -> Optional[Layer]:
        data = parent.raw_data
        self.layer = parent
        self._decode(data, **metadata)
        self.layer.name = 'urlencoded'
        self.layer.is_structured = True
        self.layer.human_readable = True
        return self.layer

    def _decode(self, data, **metadata):
        try:
            if type(data) is not str:
                data = data.decode("ascii", "strict")
            if not data.startswith('http'):
                raise ValueError("[Phorcys] Failed to parse input.")
            data = url.decode(data)
            if not data:
                raise ValueError("[Phorcys] Failed to parse input.")
            for (k, v) in data:
                child = Layer(True)
                child.human_readable = True
                child.parent = self.layer
                child.raw_data = v
                child.name = k
                child.lines = [v]
                self.layer.lines.append('%s=%s' % (k, v))
                self.layer.add_extracted_layer(child)
        except:
            raise ValueError("[Phorcys] Failed to parse input.")
