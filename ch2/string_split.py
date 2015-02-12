just_len = 55

line = 'asdf fjdk; afed, fjek,asdf,foo'
# we can split a string by a separator. the separator can be one or more characters
print('string split function'.ljust(just_len),
      line.split(','))

# but we can NOT split a string by either , or ;
print('string split does not support either concept'.ljust(just_len), line.split(',;'))

# but we could use powerful regular expression to split strings
# the downside is that it's not so obvious, it's always good to add some explanations for regular expression
import re
# split by either ; or , or space and followed by any number of spaces
print('we can use regular express to support either concept'.ljust(just_len),
      re.split(r'[;,\s]\s*', line))

# if we remove followed by any number of spaces
# then string like ', ' we are separated, there is an empty string item created
print('no suffix \s* means every character is a separator'.ljust(just_len), re.split(r'[;,\s]', line))

print('while we could remove it by list comprehension'.ljust(just_len), [s for s in re.split(r'[;,\s]', line) if s])

# if using capture group (parentheses added in regular expression)
# then the separation self also will be included in the result
fields = re.split(r'(;|,|\s)\s*', line)
print('delimiters will be in result if using group'.ljust(just_len), fields)

# the value will be item 0,2,4,6...
# the delimiters will be 1,3,5,7
delimiters = fields[1::2] + ['']
values = fields[::2]
print('start from 1 and every second item are delimiters'.ljust(just_len), delimiters)
print('start from 0 and every second item are values'.ljust(just_len), values)

# worth to notice that if there are consequence string with delimiters ';,'
# then there will be an empty string item in the result
line = 'asdf fjdk;, afed, fjek,asdf,foo'
fields = re.split(r'(?:;|,|\s)\s*', line)
print('between two delimiters will create an item in result'.ljust(just_len), fields)
