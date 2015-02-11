just_len = 60

s = 'pýtĥöñ\fis\tawesome\r\n'
print('every time see strange characters are annoying'.ljust(just_len), s)

remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): ' '
}

print('using translate function could map some chars'.ljust(just_len), s.translate(remap))



import unicodedata
import sys

# all unicode, its a huge number
all_unicodes = range(sys.maxunicode)
s='O\u0308 \u00d6'
print('if its a combining(decorate) char or not, \u0308  \u00d6'.ljust(just_len), unicodedata.combining(s[1]), unicodedata.combining(s[-1]))

# get all combining chars
# since we need using this map to translate, here just map to None
all_combining_chars = dict.fromkeys(c for c in all_unicodes if unicodedata.combining(chr(c)))
# get all combining chars using dictionary comprehension
all_combining_chars = {c: None for c in all_unicodes if unicodedata.combining(chr(c))}

from collections import ChainMap
all_combining_chars_with_special_chars = ChainMap(all_combining_chars, remap)

# decomposed string means every char with decorate on will be split to two chars
s = 'pýtĥöñ\fis\tawesome\r\n'
decomposed_string = unicodedata.normalize('NFD', s)

print('we can decompose, then remove all combining chars'.ljust(just_len),
      decomposed_string.translate(all_combining_chars_with_special_chars))

# we should ignore encode error if the char can not be encoded to ascii
# or say that it's not in ascii range
# otherwise an exception will be raised.
print('we can remove by encode to ascii and decode to ascii'.ljust(just_len),
      unicodedata.normalize('NFD', s).encode('ascii', 'ignore').decode('ascii'))

print('without normalize will remove all special chars'.ljust(just_len),
      s.encode('ascii', 'ignore').decode('ascii'))


# print(''.ljust(just_len), s)