num=int(input("Enter Num"))

isDivisible=False

i=2
while i<num:
    if num%i==0:
        isDivisible=True
        print(f"{num} is Divisible by {i}")
        break
    i+=1
if isDivisible:
    print(f"{num} is not a prime no.")
else:
    print(f"{num} is a Prime No. ")        
