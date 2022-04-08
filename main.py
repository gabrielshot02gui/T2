name = input("Whats your name: ")
num1 = int(input("How much did you get on the first test: ")) #use numbers
num2 = int(input("How much did you get on the second test: ")) #use numbers here too
total = num1 + num2 
average = total/2
yp = average<5
if yp == True:
  print("Try to improve your grades")
else:
  print("Congratulations",name,"you passed")
  
