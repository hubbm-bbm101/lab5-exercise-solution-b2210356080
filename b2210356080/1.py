N = int(input('Please enter a number.'))
oddSum = 0
evenSum = 0
for i in range(1,N+1):
    if i%2==0:
        evenSum += i
    else:
        oddSum += i
print('Sum of the odd numbers is', oddSum)
print('Average of the even numbers is', evenSum/N)
