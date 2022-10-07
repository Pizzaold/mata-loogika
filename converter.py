'''
#dec to bin
number_as_string = input("Enter a decimal number:")
#number_as_string = input("tere")

# input() gives us text, let's convert it to number
number = int(number_as_string)

# here we gather the result
result = ""

while number > 0:
    remainder = number % 2
    result = str(remainder) + result
    number = number // 2


print("Result in binary:", result)
'''
#bin to dec
binary_as_string = input("Enter a binary number:")
binaryCount = len(binary_as_string)
print(binaryCount)
decimal_number = 0
pow_Value = 0
while(binaryCount > 0):
    print(binary_as_string[binaryCount - 1])
    decimal_number += pow(2, pow_Value) * int(binary_as_string[binaryCount - 1])
    binaryCount -= 1
    pow_Value += 1

print("Result in decimal:", decimal_number)
