temp = int(input("What is the temperature today?\n"))

if temp > 100:
    print("AHHHHH WE ARE GONNA DIE!")
elif temp < 20:
    print("my circuits are freezing")
elif temp == 21:
    print("DEEZ")
elif temp == 69:
    print("why")
else:
    print("The weather is decent today, since its only " + str(temp) + " degrees outside")

    beans = int(input("How many beans are need to satisfy"))

for i in range(1, beans + 1):
    print("you have" + str(i) + "beans")