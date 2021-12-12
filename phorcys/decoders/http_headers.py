from io import StringIO
import re
from phorcys.decoders.base import Layer
from phorcys.plugins.decoder import DecoderPlugin


class HttpHeaders(DecoderPlugin):
    def __call__(self, parent: Layer, **metadata):
        data = parent.raw_data
        self.layer = parent
        self._decode(data)
        self.layer.name = 'http_headers'
        self.layer.is_structured = True
        self.layer.human_readable = True
        return self.layer

    def _decode(self, data, **metadata):
        try:
            http_header = data
            if type(http_header) is bytes:
                http_header = http_header.decode('utf-8')

            pattern = b'^(GET|POST|PUT|HEAD|DELETE|CONNECT|OPTIONS|TRACE|PATCH) '
            if not re.match(pattern, data):
                raise Exception()
            if '\r\n' not in http_header:
                raise Exception()

            sio = StringIO(http_header)
            headers = []
            first_line = True
            lines = sio.readlines()
            self.layer.lines = lines
            for line in lines:
                if first_line:
                    split = line.split()
                    self._decode_data('method', split[0])
                    self._decode_data('path', split[1])
                    self._decode_data('version', split[2])
                    first_line = False
                if ': ' in line:
                    split = line.split(': ')
                    self._decode_data(split[0].strip(), split[1].strip())
        except Exception as e:
            raise ValueError("[Phorcys] Failed to parse input.")

    def _decode_data(self, key, value):
        child = Layer(True)
        child.parent = self.layer
        child.name = key
        child.add_header({'http_header_name': key})
        child.raw_data = value
        child.lines = [value]
        self.layer.add_extracted_layer(child)
