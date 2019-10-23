import mmap

with open('test.txt') as f:
    s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    if s.find('ABC') != -1:
        print('true')
