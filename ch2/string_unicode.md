
```python
just_len = 60
oland_combined = 'O\u0308land'
oland_single = '\u00d6land'
print('some extended characters can be decomposed or composed'.ljust(just_len),
      oland_combined, oland_single, len(oland_combined), len(oland_single))

s1 = 'Jalapen\u0303o'
s2 = 'Jalape\u00f1o'

print('depends on font, decomposed might display correct'.ljust(just_len),
      s1, s2, len(s1), len(s2))

```

NFC = normal form composed
NFD = normal form decomposed
```python
import unicodedata
t1 = unicodedata.normalize('NFC', s1)
t2 = unicodedata.normalize('NFC', s2)
print('NFC means normal form composed'.ljust(just_len),
      t1, t2, len(t1), len(t2), t1 == t2)

t1 = unicodedata.normalize('NFD', s1)
t2 = unicodedata.normalize('NFD', s2)
print('NFD means normal form decomposed'.ljust(just_len),
      t1, t2, len(t1), len(t2), t1 == t2)

t1 = unicodedata.normalize('NFKD', '\u2160')
t2 = unicodedata.normalize('NFKD', '\u0049')
print('NFKD means normal form compatible decomposed'.ljust(just_len),
      t1, t2, len(t1), len(t2), t1 == t2)

t1 = unicodedata.normalize('NFKD', '\u2160')
t2 = unicodedata.normalize('NFKD', '\u0049')
print('NFKC means normal form compatible composed'.ljust(just_len),
      t1, t2, len(t1), len(t2), t1 == t2)
```
