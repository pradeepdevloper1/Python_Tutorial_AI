index1=10
index2=20

print(f"Prime number between {index1} and {index2} are")

for num in range(index1,index2):
    if num>1:
        isDivisible=False
        for index in range(2,num):
            if num % index==0:
                isDivisible=True
        if not isDivisible:
            print(num)        