import math
temp = int(input("what is the temperature today?"))

if temp > 5000:
    print("wow are you on the sun?")
elif temp < -1:
    print("sheesh it's pretty cold outside.")
elif temp == 21:
    print("deez")
else:
    print ("It's a good day for a picnic, since it's only " + str(temp) + " degrees outside")
    
its_corn_num = int(input("enter how many corn cobs you want\n"))

for i in range(1, its_corn_num + 1):
    print("you have" + str(i) + "cobs")