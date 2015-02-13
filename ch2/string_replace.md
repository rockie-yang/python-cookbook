
we can replace ALL(not the first one) substring with another substring
the original string does not change because string is immutable
```python
text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))

print(text)


```

change date from <month>/<day>/<year> to <year>-<month>-<day>
r'\3' means group number 3 in regular expression match group
```python
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

```

re.subn can return replaced string and how many has been replaced
```python
print(re.subn(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))


```

We also can use group for match response for more processing
```python
def change_date(text):
    # this is function will be called by re.sub
    def replace(match):
        from calendar import month_abbr
        # we can use group to get relative information
        month_name = month_abbr[int(match.group(1))]
        return '{day} {month} {year}'.format(day=match.group(2), month=month_name, year=match.group(3))

    return re.sub(r'(\d+)/(\d+)/(\d+)', replace, text)

print(change_date(text))
```
