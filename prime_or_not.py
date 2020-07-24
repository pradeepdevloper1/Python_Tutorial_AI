num=int(input("Enter Number"))

isDivisible=False
for i in range(2,num):
    if num % i==0:
        isDivisible=True
        
if isDivisible:
    print(f"{num} is not a prime no.")   
else:
    print(f"{num} is a prime no.")      