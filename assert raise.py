#try:
    #year  = int(input())
#except ValueError:
    #print("must enter an integer")
    #year = int(input())
#assert ( 1900 <= year) and ( year <= 2023) , "A year should between 1900 - 2023 only"
#print(2023 - year)


# idea while true except else break

year = int(input())#2012
#assert year < 2023
if year < 1900 or year > 2023:
    raise (ValueError, "don't give a ....")
print(2023 - year)