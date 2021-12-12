import base64
from typing import Optional

from phorcys.decoders.base import Layer, split_string
from phorcys.plugins.decoder import DecoderPlugin


class Base64(DecoderPlugin):
    def __call__(self, parent: Layer, **metadata) -> Optional[Layer]:
        data = parent.raw_data
        if len(str(data)) < 4:
            raise ValueError("[Phorcys] Failed to parse input. Not BASE64")

        self.layer = parent
        self._decode(data)
        self.layer.name = "base64"
        return self.layer

    def _decode(self, data):
        try:
            decoded = base64.b64decode(data, validate=True)
            child = Layer()
            child.raw_data = decoded
            child.parent = self.layer
            self.layer.add_extracted_layer(child)
            self.layer.human_readable = False
            self.layer.headers = [{'length': len(decoded)}]
            self.layer.lines = split_string(str(data), 64)
        except:
            raise ValueError("[Phorcys] Failed to parse input. Not BASE64")
