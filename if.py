num=int(input("enter the number"))
if num%2==0:
 print("it is even number")
else:
 print("it is not even number")
 def speed(time,distance):
      speed = distance//time
      print(speed)
 speed(5,100)
 def add(num1,num2):
  sum=num1+num2
  return sum
#Prime Number
number=int(input("Enter any number:\n"))
if number > 1:
    for i in range(2, number):
        if (number%i)==0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")
else:
    print(number, "is not a prime number")
