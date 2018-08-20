# Installation
*Phorcys* has been tested on Ubuntu 18.04 and Debian 9.4.

## System requirements
On Debian-like systems
```commandline
sudo apt-get install python3 python3-pip python3-dev protobuf-compiler build-essential
```

## With virtualenv
```commandline
sudo apt-get virtualenv
```
Create your virtualenv and install *Phorcys*
```commandline
mkdir my_venv
cd my_venv
virtualenv venv -p python3
source venv/bin/active
pip install phorcys
```

## Without virtualenv
```commandline
pip3 install phorcys
```

## Usage
```commandline
phorcys_decode.py -h                                                                                                                                          130 ↵
usage: phorcys_decode.py [-h] [-y YARA_FILE] [-f FLOW_FILE] [-b BINARY_FILE]
                         [-p]

Recursive network payloads decoder.

optional arguments:
  -h, --help      show this help message and exit
  -y YARA_FILE    path to file containing Yara rules
  -f FLOW_FILE    path to the MITM dump (.flow)
  -b BINARY_FILE  path to the file containing the payload to decode
  -p              list loaded plugins
```