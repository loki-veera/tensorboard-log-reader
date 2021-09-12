# Tensorboard-log_reader
Python implementation to read the tensorboard log files

## Code Usage
### Requirements
- Pandas-1.1.3 
- Python-3.7.10
- Tensorboard-2.5.0

To use, run the following commands
``` bash
$ git clone https://github.com/lokeshveeramacheneni/tensorboard-log_reader.git
$ cd tensorboard-log_reader/
$ python src/tboardreader.py --path=<path_to_log_files>
```
To know more about hyperparameters please use
``` bash
$ python src/tbaordreader.py --h
```
## TODO
- [x] Scalar save
- [ ] Plot
- [ ] Images