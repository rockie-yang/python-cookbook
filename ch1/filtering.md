We have data in a sequence, dictionary, generator or other containers.
For different processing we need different part of data based on some criteria.
And most likely, the data also need be mapped from one format to another.


using list comprehension will create a real list
```python
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
filtered = [n for n in mylist if n > 0]
print(type(filtered), filtered)


```

filter and map can be done at the same time
```python
filtered_doubled = [n * 2 for n in mylist if n > 0]
print(type(filtered_doubled), filtered_doubled)


```

using generator expression will not create a real list, it will just create a generator
```python
filtered_generator = (n for n in mylist if n > 0)
print(type(filtered_generator), filtered_generator)

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}


```

we can filter a dictionary using dictionary comprehension
```python
filter_dictionary = {key: value for key, value in prices.items() if value > 40}
print(filter_dictionary)


```

dictionary filtering and mapping can be done at the same time
```python
filter_map_dictionary = {key + "a": value*2 for key, value in prices.items() if value > 40}
print(filter_map_dictionary)
```
