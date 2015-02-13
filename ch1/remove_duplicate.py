# Some container allow having duplicate items stored at the same time.
# A generator might not even know if there is duplicate item yet.
# Since those items only created when the generator was iterate through.


# The simplest way to remove duplicate items is to convert to a set.
# Since a set object is an *unordered* collection of *distinct* *hashable* objects.


# Duplicated items will be vanished just by using the *distinct* property.
# Only the first item with distinct value will be kept.
a = [1, 5, 2, 1, 9, 1, 5, 10]
no_duplicate_not_reserve_order = set(a)
print(no_duplicate_not_reserve_order)


# Due to the *unordered* property, the previous solution can not reserve the order.
# While this solution still have one prerequisite, the item must be *hashable*.
# TypeError Exception will be raised if we try to add a unhashable item like dictionary..
def remove_duplicate(items):
    """remove duplicate and reserve the order"""
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

no_duplicate_reserve_order = remove_duplicate(a)
print(list(no_duplicate_reserve_order))


# If the item in items is not hashable, Then it can not be added to a set.
# We need a function map from unhashable(e.g. map) to hashable(e.g. tuple).
# This function is a super set of previous function with bit complexity.
def remove_duplicate_unhashable(items, key=None):
    """key is used to map an item from unhashable to a hashable if needed"""
    seen = set()
    for item in items:
        # if key is None, then it does not need map
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
no_duplicate_unhashable = remove_duplicate_unhashable(a, key=lambda d: (d['x'], d['y']))
print(list(no_duplicate_unhashable))
