
temp = int(input("What is the tempature today?\n"))

if temp > 5000:
    print("Wow are you on the sun?")
elif temp < -1:
    print("Sheesh its pretty cold outside.")
elif temp == 21:
    print("Deez")
else:
    print("Its a pretty good day for a picnic, since its only " + str(temp) + " degrees.")

    num = (int(input("how much bobux you want\n")))

    for i in range(1, num + 1):
        print("adding " + str(i) + " bobux")