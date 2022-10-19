import math

'''Practice different math expressions and calculations.'''

#declare num_a and num_b
num_a = 1
num_b = 2

# 1. Sum and difference
sum = num_a + num_b
#print(sum)
difference = num_a - num_b
#print(difference)

# 2. Float division
division = num_a / num_b
#print(division)

# 3. Integer division
division = num_a // num_b
#print(division)

# 4. Powerful operations
multiply_numbers = num_a * num_b
#print(multiply_numbers)
power = num_a ** num_b
#print(power)
remainder = num_a % num_b
#print(remainder)

# 5. Find average
average = num_a * num_b / 2
#print(average)

# decleare radius
radius = 5

# 6. Area of a circle
circle_area = round(radius * math.pi ** 2, 2)
#print(circle_area)

# decleare side_length
side_length = 5

# 7. Area of an equilateral triangle
height = math.sqrt(side_length ** 2 - (side_length / 2) ** 2)
#print(height)
triangle_area = side_length * height / 2
#print(triangle_area)

# decleare a, b & c
a = 2
b = 4
c = 6

# 8. Calculate discriminant
discriminant = b ** 2 - 4 * a * c
#print(discriminant)

# 9. Calculate hypotenuse length
c = math.sqrt(a ** 2 + b ** 2)
#print(c)

# 10. Calculate cathetus length
b = math.sqrt(c ** 2 - a ** 2)
#print(b)

# decleare seconds
seconds = 42069

# 11. Time converter
minutes = seconds / 60
houre = minutes / 60
minutes = int(60 * (houre % int(houre)))
#print(f"{int(houre)}:{minutes}") #11:41

# decleare angle
angle = 69

# 12. Student helper
sine = round(math.sin(angle), 1)
cosine = round(math.cos(angle), 1)
#print(f"{sine} & {cosine}")

# decleare n
n = 10

# 13. Greetings
lots_of_heys = n * "Hey"
#print(lots_of_heys)

# 14. Adding numbers
string_numbers = str(num_a) + str(num_b)
print(string_numbers)