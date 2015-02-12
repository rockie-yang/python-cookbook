
```python
s = '''Look into my eyes, look into my eyes, the eyes, the eyes,
the eyes, not around the eyes, don't look around the eyes,
look into my eyes, you're under.'''

import textwrap
print('Fill to length 70')

print(textwrap.fill(s, 70))

print('\nFill to length 70, indent the first line')
print(textwrap.fill(s, 70, initial_indent='   '))

print('\nFill to length 70, indent the first line, and all subsequent lines')
print(textwrap.fill(s, 70, initial_indent='   ', subsequent_indent='>'))


```

 this should first open a terminal
```python
import os
print('\nFill to the same size with terminal', os.get_terminal_size().columns)
print(textwrap.fill(s, os.get_terminal_size().columns))
```
