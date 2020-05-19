# Evtx2json
Import Windows EventLogs(.evtx files) to JSON File.

I decide to modified some python code to process huge Windows EventLogs with pure-Python software.

evtx2json uses Rust library [pyevtx-rs](https://github.com/omerbenamram/pyevtx-rs).


## Install
```bash
$ sudo python3 setup.py install
```
## Usage
```bash
$ evtx2json /path/to/your/file.evtx
```

or

```python
from evtx2json.evtx2json import evtx2json

if __name__ == '__main__':
    filepath = '/path/to/your/file.evtx'
    evtx2json(filepath)
```

### Options
```
--size:
    bulk write size
    (default: 500)
```

### Examples
```
$ evtx2json /path/to/your/file.evtx --size=500
```

```py
if __name__ == '__main__':
    evtx2json('/path/to/your/file.evtx', size=500)
```

## Performance Evaluations
evtx2json was evaluated using the sample evtx file of [https://github.com/sbousseaden/EVTX-ATTACK-SAMPLES] (about 1MB binary data).

```.bash
$ time evtx2json ./Security.evtx
> 6.25 user 0.13 system 0:14.08 elapsed 45%CPU
```

### Running Environment
```
OS: Ubuntu 18.04  
CPU: Intel Core i7-6500  
RAM: DDR4 16GB  
```


## Installation
### via pip
```
$ pip install git+https://github.com/jonitampan/evtx2json
```

The source code for evtx2es is hosted at GitHub, and you may download, fork, and review it from this repository(https://github.com/jonitampan/evtx2json).

Please report issues and feature requests.

## License
evtx2json is released under the [MIT](https://github.com/jonitampan/evtx2json/blob/master/LICENSE) License.

Powered by [pyevtx-rs](https://github.com/omerbenamram/pyevtx-rs).  
Inspired by [evtx2es](https://github.com/sumeshi/evtx2es).
Inspired by [EvtxtoElk](https://github.com/dgunter/evtxtoelk).
