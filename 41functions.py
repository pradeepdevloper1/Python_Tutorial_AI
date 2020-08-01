
def print_name(name):
    """
    this function print name
    """
    print("Hello "+ str(name))

print_name('Pradeep')  
#Doc String 
print("Doc string "+print_name.__doc__)
 
    
    
def get_sum(lst):
    """
    Return sum of list 
    """
    _sum=0
    for i in lst:
        _sum+=i
    return _sum 
    
s=get_sum([1,2,3,4,5])
print(s)


# lifetime of a variable
global_var="this is global variable"

def test_lifetime():
    local_var="this is local variable"
    print(global_var)
    print(local_var)

test_lifetime()
print(global_var)
print(local_var)


#HCF of Two No.

def compute_HCF(a,b):
    smaller=a if a<b else b
    hcf=1
    for i in range (1,smaller+1):
        if(a%i==0) and (b%i==0):
           hcf=i 
    return hcf

num1=98
num2=78
print(f"HCF of {num1} and {num2} is:",compute_HCF(num1,num2))   

