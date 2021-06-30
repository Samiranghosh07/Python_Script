#fizzbuzz game without modulo operator

def FizzBuzz(n):
    c3=c5=0
    for i in range(1,n+1):
        c3 +=1
        c5 +=1
        if(c3==3 and c5==5):
            print('FizzBuzz')
            c3=c5=0
        elif(c3==3):
            print('Fizz')
            c3=0
        elif(c5==5):
            print('Buzz')
            c5=0
        else:
            print(i)
          
          
n=int(input("\n Enter the last range of n: "))
FizzBuzz(n)  # function call