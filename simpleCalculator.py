'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("...welcome...")
repate=" "
doIt="yes"
print("enter two numbers,then choose operation you want to applied on this numbers: ")
while repate=="yes"or doIt=="yes":
    

    num1=int(input("enter number one: "))
    num2=int(input("enter number second: "))
    result=0 #intial value for the result 
    operation=input("which operation (enter  compintion or subtraction or multiplction or division:  ").lower()
    while True:
        if((operation=="compintion")or(operation=="subtraction")or(operation=="multiplction")or(operation=="division")):
          break
        else:
           operation=input("try to enter correct operation compintion or subtraction or multiplction or division: ")
   
    
    if(operation=="compintion"):
        result=num1+num2
  
    if(operation=="subtraction"):
    
        result=num1-num2
    
    if(operation=="multiplction"):   
       result=num1*num2
    
    if(operation=="division"):
       try:
          num1/num2
       except ZeroDivisionError:
            print('Cannot devide by zero.')
    
    print("The result :",result) 
    repate=input("do you want to repate?(yes or no)").lower()
    if(repate=="no"):
        doIt=" "
        
print("good bey :)")

    
