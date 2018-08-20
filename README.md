# Description
*Phorcys* is a recursive payload decoder. It will recursively decode and inspect binary and text content. As 
an example, it is able to decode a `base64` encoded JSON field which has been compressed in `gzip` and encoded 
in `base64`. *Phorcys* creates either a tree or a forest depending on input format. In case of a binary file, 
you will get a tree in which the root corresponds to the format/algorithm detected from the file content. Then, each child 
corresponds to the format/algorithm detected from the content extracted/decoded by the parent node. In case of a `.flow` 
file, each root corresponds to a single flow.

*Phorcys* is the analysis engine of [PiPrecious](https://github.com/PiRanhaLysis/PiPrecious).

It supports the following format/algorithms out-of-the-box:
* base64
* bzip
* css
* gzip
* html
* json
* lzma
* multipart
* protobuf
* text
* urlencoded
* zlib

It can be fed with a `.flow` file (from `mitmdump`) or with a binary file. In the case of a `.flow` file, *Phorcys* 
will recursively decompress/decode:
* URL
* request payload
* response payload
 
for each flow.

# Examples
* [Binary file example](doc/example_bin.md)
* [Yara rules example](doc/example_yara.md)
* [Flow file example](doc/example_flow.md)

# Installation
*Phorcys* depends on multiple system requirements
* python3
* python3-pip 
* python3-dev 
* protobuf-compiler 
* build-essential

See the [installation guide](doc/install.md).

