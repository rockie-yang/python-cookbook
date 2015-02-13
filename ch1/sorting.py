# Sorting a collection a common case in programming.
# While it is normally not sorting for a whole item, but part of the item.
# There are few choices to get those parts.
# *itemgetter* can be used to get some fields of the item.
# *attrgetter* can be used to get some attribute of the item.
# *lambda* or *function* can be used in more sophisticated case.


# We could sort it only by fname
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
from operator import itemgetter
by_fname = sorted(rows, key=itemgetter('fname'))
print(by_fname)

# We could sort it by fname and lname
by_name = sorted(rows, key=itemgetter('fname', 'lname'))
print(by_name)


# We could sort it by using lambda.
# While itemgetter is more preferred, since it's simple and a bit faster
by_name = sorted(rows, key=lambda r: (r['fname'], r['lname']))
print(by_name)


# We could sort it by uid
by_id = sorted(rows, key=itemgetter('uid'))
print(by_id)


# itemgetter is an class have *__call__* function.
# It will create an *getter* object when we call itemgetter(<itemname>).
# The *getter* object can accept an item.
# The *__call__* function will be called to get some fields from the item.
item1 = rows[0]
getter = itemgetter('fname')
print(getter(item1))


# we could get one or more attributes from an object
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


from operator import attrgetter
u1 = User(1)
u2 = User(2)
u3 = User(3)


print(attrgetter('user_id')(u1))

l = [u3, u1, u2]
by_id = sorted(l, key=attrgetter('user_id'))
print(by_id)