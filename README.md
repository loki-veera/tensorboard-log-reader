# Visualisation

Code to extract the required tags in the tensorboard log file. 
The extracted tags are saved in a csv file.

## How to run:

```
python test_tboardreader.py --path=<Path_to_log_file> --tag=<'all'/specific tag>
```
If tag is set 'all'. All the tags are acquired.

## Example:

Run the examples/logfile_generator.py for generating example tensorboard event file. 
```
cd examples
python logfile_generator.py
```
We provide a test event file in examples/runs/ folder.
To read the tag 'linear_1' in a generated event file run
```
python test_tboardreader.py --path='./examples/runs/Nov05_11-40-55_lokesh-X510UNR/' --tag='linear_1'
```
If all the tags must be read then run
```
python test_tboardreader.py --path='./examples/runs/Nov05_11-40-55_lokesh-X510UNR/' --tag='all'
```
For a preview, a generated csv file with all extracted tags is also included.
## Help:
To know more about parser arguments run
```
python test_tboardreader.py -h
```