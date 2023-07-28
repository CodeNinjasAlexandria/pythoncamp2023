temp = int(input("what is the temp today?\n"))

if temp > 5000:
    print(" wow, are you on the sun?")
elif temp < -1:
    print(" pretty cold outside")
elif temp == 21:
    print("deez")
else:
    print(" its a good day for a picnic, since its only " + str(temp) + " degrees" )

beans_num = (int(input("enter how many beans you want")))

for i in range(1, beans_num + 1):
    print(str(i) + "beans_num")
