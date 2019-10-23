import mmap

def ListFile(input_str, input_file):
    with open(input_file) as f:
        s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        if s.find(input_str) != -1:
            print('true')
