#x = int(input())
#y = int(input())
#z = x+y
#a = x-y
#c = x*y
#e = x,"+",y,"=",z,
#x,"-",y,"=",a,
#x,"-",y,"=",c
#print(e)

#def calculator(a1, a2):
    #add = a1 + a2
    #subt = a1 - a2
    #mult = a1 * a2
    #divi = a1 // a2

    #return add, subt, mult, divi

#a1 = int(input())
#a2 = int(input())

#result_add, result_sub, result_mul, result_div = calculator(a1, a2)
#print(a1, "+", a2, "=", result_add)
#print(a1, "-", a2, "=", result_sub)
#print(a1, "*", a2, "=", result_mul)
#print(a1, "/", a2, "=", result_div)

#def mul(a1, a2):
  #mul = a1 * a2
  #return mul

#a1 = int(input())
#a2 = int(input())

#result_mul = mul(a1, a2)
#print(result_mul)

#def welcome(name1):
  #result = "Welcome"
  #result2 = "Sommai 108 Eleven Shop"
  #return result, result2

#name1 = str(input())

#result_result, result2_result2 = welcome(name1)
#print(result_result, name1, "\nSommai 108 Eleven Shop")

def draw_rectangle(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("#", end="")
            else:
                print(" ", end="")
        print()
# รับค่าความกว้างและยาวของสี่เหลี่ยมจัตุรัส
width_height = int(input())

# เรียกใช้ฟังก์ชันเพื่อวาดรูปสี่เหลี่ยม
draw_rectangle(width_height)