# Tuple is a very useful data structure to group some items together.
# While there is a minor drawback for the access.
# The magic number index is not so obvious compare to names.
# namedtuple is a wrapper on top of tuple, it can remove those magic numbers with a little overhead.
# It is like a light weighted class, or a read only dictionary with efficiency.


# using tuple can represent a record
sub = ('rockie@example.com', '2012-10-01')
# but access it need some magic number
print('email=', sub[0], 'joined at', sub[1])

from collections import namedtuple
Subscriber=namedtuple('Subscriber', ['email', 'joined'])
sub1 = Subscriber('rockie@example.com', '2012-10-01')
print(sub1.email)
print('number of attributes', len(sub1))

# this can not be executed, because it's read only
# sub1.email = 'rockie@example2.com'
