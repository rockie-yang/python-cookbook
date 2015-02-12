just_len = 60
s = '   \thello world \n'
print('strip will strip all spaces, include \\t \\n'.ljust(just_len), s.strip(), len(s.strip()))

s = '----\thello world \n==='
print('if specified, it will only strip those chars, exclude \\t \\n'.ljust(just_len), s.strip('-'), len(s.strip('-')))

print('but can specify more than on characters, \\t'.ljust(just_len), s.strip('-\t'), len(s.strip('-\t')))
print('but can specify more than on characters, \\t\\n'.ljust(just_len), s.strip('-\t\n'), len(s.strip('-\t\n')))
print('but can specify more than on characters, -=\\t\\n'.ljust(just_len), s.strip('-=\t\n'), len(s.strip('-=\t\n')))

print('we also can specify strip only left, -=\\t\\n'.ljust(just_len), s.lstrip('-=\t\n'), len(s.lstrip('-=\t\n')))
print('we also can specify strip only right, -=\\t\\n'.ljust(just_len), s.rstrip('-=\t\n'), len(s.rstrip('-=\t\n')))


s = '   hello     world   '
print('we also can remove all spaces'.ljust(just_len), s.replace(' ', ''), len(s.replace(' ', '')))
print('we also can remove all multiple spaces with replace'.ljust(just_len),
      s.replace(' ', '').replace('   ', ''), len(s.replace(' ', '').replace('   ', '')))

import re
print('we also can use regular expression'.ljust(just_len),
      re.sub('\s+', ' ', s), len(re.sub('\s+', ' ', s)))

print('but we still need strip prefix and suffix spaces'.ljust(just_len),
      re.sub('\s+', ' ', s).strip(), len(re.sub('\s+', ' ', s).strip()))

# using with key word means the __exit__ function will be automatically called after exit the scope
with open('./string_strip.py') as f:
    # here using generator comprehension normally is better than list comprehension
    # the real sequence should be only generated if it's very small when necessary
    lines = (line.strip() for line in f)
    print(next(lines))




