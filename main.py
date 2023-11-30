a=int(input("Enter the 1st number:"))     # input of 1st number


b=int(input("Enter the 2nd number:"))   #  input of 2nd number


print("Operations to choose are given below->") #  normal heading


print("To perform addition press 1:")      #  option of addition


print("To perform subtraction press 2:")    #  option of subtraction

print("To perform multiplication press 3:") #  option of multiplication

print("To perform division press 4:")   #option for division

print("To perform modulo operation or to find modulus press 5:")

ch=int(input("Enter your choice:"))
if(ch==1):
    print("Result = ",(a+b))
elif(ch==2):
    print("Result = ",(a-b))
elif(ch==3):
    print("Result = ",(a*b))
elif(ch==4):
    print("Result = ",(a/b))
elif(ch==5):
    print("Result = ",(a%b))