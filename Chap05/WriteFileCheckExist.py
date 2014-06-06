with open('somefile', 'x') as f:
    f.write('hello world')

# write again, and this will fail, since somefile already exists
with open('somefile', 'x') as f:
    f.write('hello world')
