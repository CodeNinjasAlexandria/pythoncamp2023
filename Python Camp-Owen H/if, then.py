temp = int(input(" what is the temperature today?\n"))

if temp > 5000:
    print(" Wow are you on the sun?")
elif temp < -1:
    print(" Sheesh it's pretty cold outside.")
elif temp == 21:
    print(" Deez")
else:
    print(" It's a good day for a picnic, since it's only " + str(temp) + " degrees outside")

    beans_num = int(input(" how many beans do you want?\n"))

for i in range(1, beans_num + 1):
    print(" you have " + str(i) + " beans")