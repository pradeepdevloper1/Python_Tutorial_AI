
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
 

#Types of Function
#1 Built In Function
#2 User Defined Function

#absolute function
num1=-100
print(abs(num1))

# all function
# return true when  elements are iterable

lst=[1,2,3,4,5,6,7,8,9]
print(all(lst))

lst=[0,1,2,3,4,5,6,7,8,9]
print(all(lst))

lst=[2,3,4,5,6,7,8,9,False]
print(all(lst))



#dir
numbers=[1,2,3,4,5]
print(dir(numbers))



#edivmod
print(divmod(9,2))

#filter function
number_list=range(-10,10)
print(list(number_list))

def find_positive_number(number):
    return number>0
    
pos_num_list=list(filter(find_positive_number,number_list))
print(pos_num_list)



#isinstance
lst=[1,2,3,4,5,6,7]
print(isinstance(lst,list))

lst2=(1,2,3,4,5,6,7)
print(isinstance(lst2,list))



#map Function
numbers=[1,2,3,4,5,6,7,8,9]

def poweroftwo(num):
    return num**2
    
squared =list(map(poweroftwo,numbers))  
print(squared)


#Reduce function
def multiply(a,b):
    return a*b
lst=[1,2,3,4]
from functools import reduce
product=reduce(multiply,lst)
print(product)

    
