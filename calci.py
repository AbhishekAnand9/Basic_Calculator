def Calculator(a,b,opn):
  if opn=="+":
    print("Sum =",a+b)
  elif opn=="-":
    print("Difference =",a-b)
  elif opn=="*":
    print("Product =",a*b)
  elif opn =="/":
    print("Division =",a/b)
  elif opn=="%":
    print("Percentage = ",(a/100)*b)
 
  else:
    print("Invalid Operation")


if __name__ == "__main__":
  opn=input(" Choose a Operation (+ , - , * , / , % , !) : ")
  if opn=="%":
    print("In Case of percentage a=percentage and b=total")
  else:
    pass
  a=int(input("Enter 1st Number : "))
  b=int(input("Enter 2st Number : "))
  
  Calculator(a,b,opn)
  
