# test cases passed

def fizzBuzz(n):
    # Write your code here
    i=1;
    while i<=n:
        if i%3==0 and i%5==0:
            print('FizzBuzz')
        elif i%3==0 and i%5!=0:
            print('Fizz')
        elif i%3!=0 and i%5==0:
            print('Buzz')
        elif i%3!=0 and i%5!=0:
            print(i)
        i+=1














def fizz_buzz(n=100):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

fizz_buzz()