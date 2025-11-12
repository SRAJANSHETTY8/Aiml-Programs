#data Types
a=4
b=2
print(a/b)

range(1,6,2)

n=5
ans=1
while (n>0):
    ans*=n
    print(ans)
    n-=1


#Write a program that keeps accepting numbers from user. If sum of accepted numbers is more than 300, the program execution should stop.

s = 0

while True:
    num = int(input("Enter a number: "))
    s += num
    if s>300:
        print("the sum exceeded",s)
        break


# Write a program that keeps accepting numbers until 0 is entered. Program execution stops when zero is entered.
while True:
    num=int(input("enter the number"))
    if num==0:
        print("you eneterd zero pls enter another number")
        break
#Write a program that keeps accepting strings until ‘Bon’ is entered. The program should display ‘Voyage’ and quit execution.
while True:
    s=input("enter the string")
    if s=="Bon":
        print("Voyage")
        break

        