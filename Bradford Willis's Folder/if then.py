temp = int(input("What is the temperature?\n"))

if temp > 5000:
    print("Wow are you on the sun?")
elif temp < -1:
    print("Sheesh it's pretty cold outside.")  
elif temp == 21:
    print("SUS")  
else:
    print("It's a good day day for a picnic, since it's only " + str(temp) + " degrees Outside.")

beans_num = int(input("Enter how many beans you want\n"))

for i in range(1, beans_num + 1):
    print("you have " + str(i) + " beans")