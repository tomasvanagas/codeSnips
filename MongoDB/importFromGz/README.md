# Import from GZ file/files into MongoDB

GZip'ed files should contain compresed text files with many lines each containing ONE JSON object.

Example: 
```
{"jsonarg1": "value1", "jsonarg2": "value2", ...}
{"jsonarg1": "value3", "jsonarg2": "value4", ...}
...
```


Usage: 
```
cat gzip_files* | gzip -cd | python3 main.py
```
