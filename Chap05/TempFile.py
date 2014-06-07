#from tempfile import TemporaryFile
from tempfile import NamedTemporaryFile
from tempfile import TemporaryDirectory

#with TemporaryFile('w+') as f:
with NamedTemporaryFile('w+') as f:
    print(f.name)
    f.write('hello world\n')
    f.write('testing')

    f.seek(0)
    print(f.read())

with TemporaryDirectory() as tempdir:
    print(tempdir)
