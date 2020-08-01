
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



