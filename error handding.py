try:
    print('why gay dum')
    print(2/0) #name error
    print(vetit) #zerodivision
except NameError:
    print("name error")
except ZeroDivisionError:
    print("can't solve")
else:
    print("yipee no error") #if there were no error go else
finally:
    print("end")
print('done numb digger')