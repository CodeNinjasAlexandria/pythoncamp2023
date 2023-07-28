temp = int(input(" What is the temperature today?\n"))
#\n shows where you write ur response on a different line
if temp > 80:
    print(" Do you need to sit inside for a bit?")
elif temp < 40:
    print(" That is very cold, do you need a coat?")
elif temp == 75:
    print(" That's the perfect temperature for me, how about you?")
else:
    print(" It's a good day for a walk today, since it's only " + str(temp) + " degrees.")
#elif means else-if- is used in the beginning or the end of the code- else and if is used at the end and beginning respectively