
# round function is used to round a number to a given precision in decimal digits.
import math
print(round(math.pi, 1))  # 3.14 => 3.1, the last number is 4, it will be rounded
print(round(math.pi, 2))  # 3.141 =>, the last number is 1, it will be rounded
print(round(math.pi, 3))  # 3.1415 =>, the last number is 5, it will be carried

# ceil is used to get the up closest integer number
# floor is used to get the low closest integer number
import math
print(math.ceil(math.pi))
print(math.floor(math.pi))


