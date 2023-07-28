temp = int(input("What is the temperature today?\n"))

if temp > 5000:
    print("Wow are you on the sun?")
elif temp < -1:
    print("YeESh ITS PRettY cOlD OuT")
elif temp == 420:
    print("DEEEZ NUTS")
else:
    print("its so nice out oyu should go outside and go ot hte supermarket where there is a white van waiting for oyu to say hello and to give you some free money")


BEANS_NUM = int(input("enter how many beans you want "))

for i in range(1, BEANS_NUM + 1):
    print( 'you have ' + str(i) + " beans")