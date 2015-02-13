# Unpacking is to get some items from a collection.
# The grammar provided by Python is so elegant with a simple boilerplate.


# tuple can unpacking to variables
p = (4, 5)
x, y = p
print(x, y)  # 4 5


# list also can unpacking to variables
data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name, shares, price, date)


# embedded sequence also can unpacking to variables at once
name, shares, price, (year, month, day) = data
print(name, shares, price, (year, month, day))


# uninteresting part could using _ as variable name, so that don't need spend time to find a good name
name, shares, _, (year, month, _) = data
print(name, shares, (year, month, _))


# using * expression to group part of the items
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212', 'stockholm')
name, email, *phone_numbers, city = record
print(name, email, phone_numbers, city)


# also can using either index way or unpacking way to get interesting parts
_, _, *phone_numbers, _ = record
print(phone_numbers)

phone_numbers = record[2:-1]
print(phone_numbers)