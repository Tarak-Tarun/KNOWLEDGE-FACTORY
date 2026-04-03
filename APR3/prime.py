def check_prime(number):
    if number<=1:
        return False
    for i in range(2,int(number**0.5)+1):
        if number%i==0:
            return False
    return True
number=int(input("Enter a Number: "))
if(check_prime(number)):
    print(f"{number} is a Prime Number")
else:
    print(f"{number} is not a Prime Number")