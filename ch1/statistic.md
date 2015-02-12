```python
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

from collections import Counter

words_count = Counter(words)
print(words_count)

top3 = words_count.most_common(3)
print(top3)

print(words_count.keys())

rows = [
    {'address': '5412NCLARK', 'date': '07/01/2012'},
    {'address': '5148NCLARK', 'date': '07/04/2012'},
    {'address': '5800E58TH', 'date': '07/02/2012'},
    {'address': '2122CLARK', 'date': '07/03/2012'},
    {'address': '5645RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060ADDISON', 'date': '07/02/2012'},
    {'address': '4801BROADWAY', 'date': '07/01/2012'},
    {'address': '1039GRANVILLE', 'date': '07/04/2012'},
]



from operator import itemgetter
from itertools import groupby
```

 we first need sort according to certain item needed to group
```python
rows.sort(key=itemgetter('date'))

```

 then we can group it according to certain item
```python
grouped = groupby(rows, key=itemgetter('date'))
for date, items in grouped:
    print(date, list(items))



```
