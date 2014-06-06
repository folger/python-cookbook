import io
s = io.StringIO()
s.write('Hello world\n')
print('This is a test', file=s)
print(s.getvalue())
s.seek(0)

print(s.read(4))
print(s.read())

s = io.BytesIO()
s.write(b'binary data')
print(s.getvalue())
