import sys
with open('IterLoops.py') as f:
    for chunk in iter(lambda: f.read(10), ''):
        sys.stdout.write(chunk)
