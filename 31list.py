#list Creation

emptylist=[]
lst=[1,2,3,4,5]
print(lst)
lst2=['pradeep','kumar','yadav']
print(lst2)
lst3=[1,'pradeep',890000.99,True]
print(lst3)

#length 
print(len(lst3))

#append
lst3.append('kumar')
print(lst3)
lst3.append('kumar')
print(lst3)


#Insert
print('insert in list')
lst4=['one','two','four']
print(lst4)
lst4.insert(2,'three')
print(lst4)


#Remove
print('insert in list')
lst5=['one','two','four']
print(lst5)
lst5.remove('four')
print(lst5)


#Append vs Extend
print('Append vs Extend in list')
lst6=['one','two','three']
lst7=['Four','Five','Six']
lst6.append(lst7)
print('Append in list')
print(lst6)
lst8=['one','two','three']
lst9=['Four','Five','Six']
lst8.extend(lst9)
print('extend in list')
print(lst8)


#Delete
print('Delete in list')
lst10=['one','two','three']
print(lst10)
del lst10[1]
print(lst10)

a=lst10.pop(1)
print(a)
print(lst10)


#Keyword in list
lst11=['one','two','three','Four']
if 'two' in lst11:
    print('AI')
if 'Six' not in lst11:
    print('ML')


#Reverse
lst12=['one','two','three','Four']
lst12.reverse()
print(lst12)



#sorting
print('.................Sorted List...........')
lst13=[4,2,1,5,9,7]
print(lst13)
sorted_list=sorted(lst13)
print(sorted_list)

print('.................Reverse Sorted List...........')
lst14=[4,2,1,5,9,7]
print(lst14)
sorted_list=sorted(lst14,reverse=True)
print(sorted_list)

print('.................Sort...........')
lst15=[4,2,1,5,9,7]
print(lst15)
lst15.sort()
print(lst15)

#Multiple Reference
print('.................Multiple Reference...........')
lst16=[4,2,1,5,9,7]
print(lst16)
lst17=lst16
lst17.append(11)
print(lst16)
print(lst17)

# String Split to List
print('.................string to list...........')
s='one,two,three,four,five'
print(s)
slist=s.split(',')
print(slist)


print('.................string to list...........')
s='Hello Everyone ,This is Pradeep'
print(s)
slist=s.split()
print(slist)


#list Indexing
print('.................list Indexing...........')
lst18=[4,2,1,5,9,7]
print(lst18[1])
print(lst18[-1])

#list slicing
print('.................list Slicing...........')
lst19=[4,2,1,5,9,7]
print(lst19[:])
print(lst19[0:3])


#list COUNT
print('.................list count...........')
lst20=[4,1,2,1,1,5,9,7]
print(lst20.count(1))


#list Comprehensive
square=[]
print('.................list without comprehensive...........')
for i in range(1,11):
    square.append(i**2)
print(square)    

square2=[]
print('.................list with comprehensive...........')
square2=[i**2 for i in range(1,11)]
print(square2)   


# comprehensive in list 
print('.................list with comprehensive2...........')
lst =[-10,-20,10,20,30]
new_lst=[i*2 for i in lst]
print(new_lst)
    
print('.................list with comprehensive3  excluding negative...........')
lst =[-10,-20,10,20,30]
new_lst=[i for i in lst if i>0]
print(new_lst)

print('.................list of tupples with comprehensive..........')
lst =[-10,-20,10,20,30]
new_lst=[(i,i**2) for i in range(10)]
print(new_lst)
    
print('................. transpose matrix..........')

matrix=[[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12]]

transpose=[]
for i in range(4):  
    lst=[]
    for row in matrix:
        lst.append(row[i])
    transpose.append(lst)
print(transpose)               

print('.................   comprehensive transpose matrix..........')

matrix=[[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12]]

transpose2=[[row[i] for row in matrix] for i in range(4)]
print(transpose2)               


