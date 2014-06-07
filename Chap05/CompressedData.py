import gzip
import bz2

s = ''
with open('BinaryData.py', 'r') as f:
    s = f.read()

with gzip.open('B.gz', 'w') as f:
    f.write(s.encode())

with bz2.open('B.bz2', 'w') as f:
    f.write(s.encode())
