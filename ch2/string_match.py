# Match can be easy or very complex. For simple match we can use function in str.
# For sophisticated match, we can use regex or other external libraries.


# we could simply using endswith, startswith function in the string to check suffix or prefix
just_len = 55
filename = 'spam.txt'
print('whether filename ends with .txt'.ljust(just_len),
      filename.endswith('.txt'))

url = 'http://www.python.org'
print('whether url starts with http:'.ljust(just_len),
      url.startswith('http:'))


# if we want check match with multiple choices
# then just provide a tuple with all those choices
import os
python_files = [filename for filename in os.listdir('.') if filename.endswith(('.py', '.pyc'))]
print('get all file match .py or .pyc'.ljust(just_len),
      python_files)


# using following expression to check if there is any file which the filename end with '.py'
print('if there is any file ends with .py'.ljust(just_len),
      any(name.endswith('.py') for name in os.listdir('.')))


# 'any' could be treated as more powerful match compare to 'in'
# 'in' check the whole object, while any could using functions
print('if there is string_match.py'.ljust(just_len),
      'string_match.py' in os.listdir('.'))
print('if there is string_match.py'.ljust(just_len),
      any(name == 'string_match.py' for name in os.listdir('.')))


# we can use find to check whether and where is the substring located
# it will return position or -1 if not exist
text = 'yeah, but no, but yeah, but no, but yeah'
print('find "no" '.ljust(just_len), text.find('no'))
print('rfind "no"'.ljust(just_len), text.rfind('no'))


# the following test will be the same to check if the substring existed
print('whether "what" in text'.ljust(just_len),
      'what' in text)
print('whether "what" in text using find'.ljust(just_len),
      text.find('what') != -1)


# the following match using shell wildcard matching
# depends on OS, like on Windows, foo.txt is the same with FOO.TXT
# which means 'foo.txt' will match '*.TXT' on windows
# but it will not match on Unix like system
from fnmatch import fnmatch
print('whether foo.txt matches *.txt'.ljust(just_len),
      fnmatch('foo.txt', '*.txt'))
print('whether foo.txt matches *.TXT'.ljust(just_len),
      fnmatch('foo.txt', '*.TXT'))


# the following match always case sensitive
from fnmatch import fnmatchcase
print('whether foo.txt match *.txt case sensitive'.ljust(just_len),
      fnmatchcase('foo.txt', '*.txt'))
print('whether foo.txt match *.TXT case sensitive'.ljust(just_len),
      fnmatchcase('foo.txt', '*.TXT'))


# using regex to match a date
# it will either return a match object or None
import re
date_pattern = re.compile(r'\d+/\d+/\d+') # <digit>/<digit>/<digit>
print('11/27/2012 match to pattern'.ljust(just_len),
      date_pattern.match('11/27/2012'))
print('Nov 27, 2012 match to matter'.ljust(just_len),
      date_pattern.match('Nov 27, 2012'))


# if not a match from start, then it will return None
# but the suffix does not matter
print('Today is 11/27/2012. PyCon starts 3/13/2013. match'.ljust(just_len),
      date_pattern.match('Today is 11/27/2012. PyCon starts 3/13/2013.'))
print('11/27/2012. PyCon starts 3/13/2013. match'.ljust(just_len),
      date_pattern.match('11/27/2012. PyCon starts 3/13/2013.'))


# if want test with complete match, then add a $ in the pattern
print('11/27/2012 complete match',
      re.match(r'\d+/\d+/\d+$', '11/27/2012'))
print('11/27/2012. PyCon starts 3/13/2013. complete match',
      re.match(r'\d+/\d+/\d+$', '11/27/2012. PyCon starts 3/13/2013.'))


# we could find all matches. find all return a list
print('find all date'.ljust(just_len),
      date_pattern.findall('Today is 11/27/2012. PyCon starts 3/13/2013.'))


# to test whether a patter existed in a string
# we could using finditer which will return a generator
# and tested using 'any'
# there will be no list created, and will not doing further match if already found
print('find whether there is a date'.ljust(just_len),
      any(date_pattern.finditer('Today is 11/27/2012. PyCon starts 3/13/2013.')))


# we could match with groups
pattern_with_group = re.compile(r'(\d+)/(\d+)/(\d+)')
match = pattern_with_group.match('11/27/2012')
print('match get groups at once'.ljust(just_len),
      match.groups())

# group(0) is the complete match
# and consequence is each sub group
print('match get groups separately'.ljust(just_len),
      match.group(0), match.group(1), match.group(2), match.group(3))


text = 'UPPER PYTHON, lower python, Mixed Python'
print('find all python case insensitive'.ljust(just_len),
      re.findall('python', text, flags=re.IGNORECASE))

print('where there is python case insensitive'.ljust(just_len),
      any(re.finditer('python', text, flags=re.IGNORECASE)))

print('by default re using greedy match'.ljust(just_len),
      re.findall(r'\"(.*)\"', 'Computer says "no." Phone says "yes."'))

print('add ? after * makes match none greedy '.ljust(just_len),
      re.findall(r'\"(.*?)\"', 'Computer says "no." Phone says "yes."'))


multiline_comments = '''/* this is a
...
multiline comment */
this will not be included*/
... '''
# match /*<any comments>*/
print('by default match does not across new lines'.ljust(just_len),
      re.findall(r'/\*(.*?)\*/', multiline_comments))
print('re.DOTALL means . matches all include new lines'.ljust(just_len),
      re.findall(r'/\*(.*?)\*/', multiline_comments, re.DOTALL))

# match /*<any comments could across new lines>*/
# "?:"   means does not capture delimiters
# ".|\n" means either any character or new line
# "*?"   means none greedy match
print('((?:.|\\n) to specify include new line'.ljust(just_len),
      re.findall(r'/\*((?:.|\n)*?)\*/', multiline_comments))


print("[?:.|\\n] does not working(don't why)".ljust(just_len),
      re.findall(r'/\*[.|\n]*?\*/', multiline_comments))

