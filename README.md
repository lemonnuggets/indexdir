# indexdir
A simple script to index directories
and print files with the required filename.

# Installation
```git clone https://github.com/lemonnuggets/indexdir.git```
```cd .\indexdir\```
```pip install requirements.txt```

# Usage:
### 1. To get help

```indexdir.py -h```

### 2. To find a file with a certain filename

```indexdir.py {filename} -dep {depth to be indexed(by default infinity)} -dir {directories to be indexed(by default current working directory)}```

### 3. To ensure that certain directories are ignored

Create a file ".dirignore" in the current working directory and add the paths that you want to be ignored in each line. Check .sample.dirignore if you have any doubts about the format. 
