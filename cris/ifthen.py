temp = int(input("what is the temperature today?\n"))

if temp > 5000:
    print("wow are you on the sun?")
elif temp < -1:
    print("Sheesh it's pretty cold outside.")
elif temp == 21:
   print("Deez")
else:
    print("it's a good day for a picnic, since it's only " + str(temp) + " degrees outside")

beans_num = int(input("enter how many beans you want\n"))

for i in range(1, beans_num + 1):
    print("you have " + str(i) + " beans")
