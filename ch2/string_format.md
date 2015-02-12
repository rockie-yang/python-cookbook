```python
just_len = 60

text = 'Hello World'
print('ljust mean align on left, padding space on right by default'.ljust(just_len), text.ljust(20), '*')
print('ljust mean align on left, padding other chars'.ljust(just_len), text.ljust(20, '*'))

```

 only can specify char would work, provide more than one char will raise exception
 print('ljust mean align on left, padding other chars'.ljust(just_len), text.ljust(20, '*x'))

```python
print('rjust mean align on right, padding space on left by default'.ljust(just_len), text.rjust(20))
print('rjust mean align on right, padding other chars'.ljust(just_len), text.rjust(20, '*'))

print('center mean align on center, padding space on left and right'.ljust(just_len), text.center(20))
print('center mean align on center, padding other chars'.ljust(just_len), text.center(20, '*'))

print('format with >, doing the same with rjust'.ljust(just_len), format(text, '>20'))
print('format with <, doing the same with ljust'.ljust(just_len), format(text, '<20'))
print('format with ^, doing the same with center'.ljust(just_len), format(text, '^20'))

print('format with =>, the same with rjust padding ='.ljust(just_len), format(text, '=>20'))
print('format with =<, the same with ljust padding ='.ljust(just_len), format(text, '=<20'))
print('format with =^, the same with center padding ='.ljust(just_len), format(text, '=^20'))

print('format can be used format other types'.ljust(just_len), format(1.23456, '=>10.2f'))

print('its working, but not easy to read'.ljust(just_len),
      '{} {}'.format('rockie', 'yang'))


print('this format is quite easy to read'.ljust(just_len),
      '{first} {last}'.format(first='rockie', last='yang'))

print('even can replace more than one value regardless order'.ljust(just_len),
      '{last} {first} {last}'.format(first='rockie', last='yang'))

first = 'rockie'
last = 'yang'
print('format based on a map, like all local variables'.ljust(just_len),
      '{first} {last}'.format_map(vars()))

class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

print('format based on a map, like object'.ljust(just_len),
      '{first} {last}'.format_map(vars(Person('rockie', 'yang'))))

class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

print('if we missing some value, or want format with separate steps'.ljust(just_len),
      '{first} {middle} {last}'.format_map(safesub(vars())))

```

 this should be the same with using vars().
 but more complex

 import sys
 def sub_with_locals(text):
     return text.format_map(safesub(sys._getframe(1).f_locals))

 print('if we want substitute with frame hack'.ljust(just_len),
       sub_with_locals('{first} {middle} {last}'))

```python
print('join is very useful to concatenate items in tuple'.ljust(just_len),
      ' '.join(('an', 'apple', 'a', 'day')))
print('join is very useful to concatenate items in list'.ljust(just_len),
      ','.join(['keep', 'doctors', 'away']))

or_generator = (s for s in ['that', 'might', 'be', 'true'])
print('join is very useful to concatenate items even generator'.ljust(just_len),
      ' '.join(or_generator), type(or_generator))

```
