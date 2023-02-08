mark1 = int(input("enter the physics mark:"))
mark2 = int(input("enter the chemistry mark:"))
mark3 = int(input("enter the biology mark:"))
mark4 = int(input("enter the mathematics mark:"))
mark5 = int(input("enter the computer mark:"))
per = ((mark1+mark2+mark3+mark4+mark5)*100/500)
print("your percentage : ",per ,"%")
if per>100:
    print("you have printed invalid mark")
elif per<=100 and per>=90:
    print("A grade")
elif per >= 80:
    print("B grade")
elif per >= 70:
    print("C grade")
elif per >= 60:
    print("D grade")
elif per >= 50:
    print("E grade")
elif per >= 40:
    print("F grade")
else:
    print("FAIL !!!!!")
