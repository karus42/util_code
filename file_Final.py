import os
import mmap

INPUT_PATH = 'path/to/folder'
CRITERIA = '.log'
FILE_LIST = []

def FindFile():
  # r=root, d=directories, f = files
  for r, d, f in os.walk(path):
    for file in f:
      if 'CRITERIA' in file:
        FILE_LIST.append(os.path.join(r, file))

for f in FILE_LIST:
    print(f)
    


def ListFile(input_str, input_file):
    with open(input_file) as f:
        s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        if s.find(input_str) != -1:
            print('true')    
