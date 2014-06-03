lines = """# this is something
# not that important
# maybe just some comment
# to go with
here is the main text
but still, nothing interesting
# so, these text will not be drop
# even they begin with #"""

from itertools import dropwhile
for line in dropwhile(lambda line: line.startswith('#'), lines.split('\n')):
    print(line)
