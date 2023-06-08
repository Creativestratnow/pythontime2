# 1 in 1 out
def square(x):
    result = x ** 2
    return result

n = int(input())
square_of_n = square(n)
print(square_of_n) # 1 วิธี

#print(square(n)) อีกวิธี

#many in 1 out
def power(x, y):
    result = x ** y 
    return result

print(power(3, 6))

#0 in one out

def introduce():
    print('hi')
    return 'p ve'
introduce()

# 1 in many out
#del ใช้ลบ
def find_square_and_sqrt(x):
    sqrt_of_x = x ** 0.5
    square_of_x = x ** 2
    return sqrt_of_x, square_of_x

print(find_square_and_sqrt(9))

#1 in 0 out

def determine_curious(name):
    print(f"งงจังครับ {name}")

result = determine_curious("Vetit")
print(result)
