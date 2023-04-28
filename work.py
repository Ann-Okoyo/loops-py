# // Write a function that uses while, if and 
# // continue statements to print all the even
# //  numbers between 0 and 50. 
def even_number():
    Number=0
    while Number <=50:
        if Number%2!=0:
           Number+=1
           continue
        print(Number)
        Number+=1

even_number()

      



# // Write a function that takes an integer argument 
# // and prints "Prime" if the number is prime, and 
# // "Not prime" if the number is not prime.
def prime_number(numeral):
    if numeral<=1:
        print("Not prime")
        return
    for k in range(2,int(numeral**0.5)+1):
        if numeral%k==0:
           print("Not prime")
           return
        print("Prime")

prime_number(7)

# Write a function that takes a list of integers as 
# input and prints the sum of all the even numbers in the list.
def integers(numbers):
    sum=0
    for j in numbers:
        if  j%2==0:
            sum+=j
            print(sum)

integers(range(0,30))
     
 
#  Write a function that takes any two integers
# as input, and prints the sum of all the numbers
# between the two integers (inclusive) that are divisible by 3.
def  sum(start,end):
    sums=0
    for num in range(start,end+1):
        if num%3 ==0:
            sums+=num

print("The sum of numbers between",start "and" end ,"that are divisible by 3 is:",sums)
sum()







   