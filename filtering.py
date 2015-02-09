
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
# using list comprehension will create a real list
filtered = [n for n in mylist if n > 0]
print(type(filtered), filtered)

# filter and map can be done at the same time
filtered_doubled = [n * 2 for n in mylist if n > 0]
print(type(filtered_doubled), filtered_doubled)


# using generator expression will not create a real list, it will just create a generator
filtered_generator = (n for n in mylist if n > 0)
print(type(filtered_generator), filtered_generator)

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# we can filter a dictionary using dictionary comprehension
filter_dictionary = {key: value for key, value in prices.items() if value > 40}
print(filter_dictionary)

# dictionary filtering and mapping can be done at the same time
filter_map_dictionary = {key + "a": value*2 for key, value in prices.items() if value > 40}
print(filter_map_dictionary)