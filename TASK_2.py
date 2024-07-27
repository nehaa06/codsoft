def add (n1 , n2 ) :
    return n1 + n2 
def sub ( n1 ,n2):
     return n1 - n2 
def div (n1 ,n2):
    return n1 / n2
def multiply ( n1 , n2):
    return n1 * n2


print("Please  choose below operations: \n \t"
     "1.ADD\n\t"
     "2.SUBTRACT \n\t"
     "3.DIVISION\n\t"
     "4.MULTIPLY\n")


choose = int(input("choose  the operations  from 1, 2, 3, 4  : "))
n1 = int(input(" enter the first number:  "))
n2= int(input("enter he second number :"))


if choose == 1 :
    print(n1 , "+", n2, "=" , add(n1, n2))

elif choose == 2:
    print(n1 , "-", n2, "=" ,sub(n1, n2))

elif choose == 3 :
    print(n1 , "/", n2, "=" ,div(n1, n2))

elif choose == 4 :
    print(n1 , "*", n2, "=",3, multiply(n1, n2))    
else :
    print("exit ")    