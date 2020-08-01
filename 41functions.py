
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

    
    
#UserDefined Functions

def add(a,b):
    return a+b

def sub(a,b):
    return a-b
    
def multiply(a,b):
    return a*b
    
def divide(a,b):
    return a/b
    

print('Enter choice')
print('Enter 1 for addition' )
print('Enter 2 for subtraction' )
print('Enter 3 for multiplication' )
print('Enter 4 for division' )

choice=int(input("Enter Choice : "))
num1=float(input("Enter Num1 : "))
num2=float(input("Enter Num2 : "))

if choice==1:
    print(f"Addition of {num1} and {num2} is : ",add(num1,num2))
elif choice==2:
    print(f"subtraction of {num1} and {num2} is : ",sub(num1,num2))
elif choice==3:
    print(f"Multiplication of {num1} and {num2} is : ",multiply(num1,num2))  
elif choice==4:
    print(f"Division of {num1} and {num2} is : ",divide(num1,num2))    
else :
    print("Please Enter Valid Input ")    
    

    
# Function with Two argument
def greet(name,msg):
    """ 
    this Function is used to Greet 
    """
    print(f' hello  {name} , {msg}!')
    
greet('Pradeep','Good Morning')


def greet(name,msg="Good Evening"):
    """ 
    this Function is used to Greet with one argument  default set
    """
    print(f' hello  {name} , {msg}!')
    
greet('Pradeep')
    
    
#fdefault arg must be in second 
def greet(msg="Good Evening",name):
    """ 
    this Function is used to Greet with one argument  default set
    """
    print(f' hello  {name} , {msg}!')
    
greet('Pradeep')



#Keyword Argument 

def greet(**kwargs):
    """" this function greet person with provided arguments
    """
    if kwargs:
      print(' Hello {0}, {1}!'.format(kwargs['name'],kwargs['msg']))
    
greet(name="Pradeep",msg="Good AfterNoon")     

    
