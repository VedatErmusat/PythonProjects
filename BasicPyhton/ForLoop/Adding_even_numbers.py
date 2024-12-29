target = int(input("Enter a number: ")) #Number between 0 and 1000
even_sum = 0
for number in range(2,target + 1,2):#Start from 2 because the first even number is 2.
    even_sum  += number
print(even_sum) #Printing the sum of all even numbers

'''
Solution 2: 
alternative_sum = 0
for number  in range(1, target + 1):
if number % 2 == 0:
alternative_sum += number
print(alternative_sum)

This solution also calculates the sum of all even numbers.
'''