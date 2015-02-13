There are good standard modules in Python can be used to do statistic.
like *collections.Counter*, *itertools.groupby*


Counter can be used to see how many time an item happened.
It even have a function *most_common(top_n)* to get top n common items.
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


```

We can group items according to certain criteria.
The *itemtools.groupby* is used exactly in this case.
Remember sort the collection first.
```python
from operator import itemgetter
from itertools import groupby

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

rows.sort(key=itemgetter('date'))

grouped = groupby(rows, key=itemgetter('date'))
for date, items in grouped:
    print(date, list(items))



```
