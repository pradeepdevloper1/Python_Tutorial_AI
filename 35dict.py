#dictionary
# it is unordered collection of items
# dictionary is hash table


dict1={}
print(type(dict1))

print(' ----create empty dictionary---')
dict1=dict()
print(dict1)

print('---dictionary---')
dict1={1:"abc",2:"def"}
print(dict1)

print('---- mixed keys in dictionary-----')
dict1={'Name':'Pradeep',1:"abc",2:"def"}
print(dict1)

print(' ----list of tuples in dictionary----')
dict1=([(1,'abc'),(2,'def')])
print(dict1)

print(' ----accessing dictionary----')
dict1={'Name':'Pradeep','Age':24,'Gender':'Male'}
print(dict1['Name'])

# print(' when key not exist accessing dictionary')
# dict1={'Name':'Pradeep','Age':24,'Gender':'Male'}
# print(dict1['email'])

print(' ---- use get in accessing dictionary----')
dict1={'Name':'Pradeep','Age':24,'Gender':'Male'}
print(dict1.get('Name'))


print(' ----update value in  dictionary----')
dict1={'Name':'Pradeep','Age':24,'Gender':'Male'}
dict1['Name']='Prado'
print(dict1['Name'])


print(' ----add new key value in  dictionary----')
dict1={'Name':'Pradeep','Age':24,'Gender':'Male'}
dict1['degree']='b.Tech'
print(dict1)

print(' ----pop in  dictionary----')
dict1={'Name':'Pradeep','Age':24,'Gender':'Male'}
dict1['degree']='b.Tech'
print(dict1.pop('Age'))
print(dict1)


print(' ----pop item in  dictionary----')
dict1={'Name':'Pradeep','Age':24,'Gender':'Male'}
print(dict1.popitem())
print(dict1)


print(' ----del in  dictionary----')
dict1={'Name':'Pradeep','Age':24,'Gender':'Male'}
del dict1['Age']
print(dict1)



print(' ----pop in  dictionary----')
dict1={'Name':'Pradeep','Age':24,'Gender':'Male'}
dict1.clear()
print(dict1)


print(' ----Methods in  dictionary----')
dict1={'Name':'Pradeep','Age':24,'Gender':'Male'}
dict2=dict1.copy()
print(dict2)

print(' ----from keys method in  dictionary----')
subject={}.fromkeys(['Eng','hindi','maths'],0)
print(subject)

print(' ----Returning new view  in  dictionary----')
dict3={2:4,3:9,4:16,5:25}
print(dict3.items())

print(' ----Returning keys  in  dictionary----')
dict3={2:4,3:9,4:16,5:25}
print(dict3.keys())

print(' ----Returning values  in  dictionary----')
dict3={2:4,3:9,4:16,5:25}
print(dict3.values())


print(' ----For Loop in  dictionary----')
dict3={'a':1,'b':1,'c':3}
for pairs in dict3.items():
    print(pairs)


print(' ----    Comprehensions For Loop in  dictionary----')
dict3={'a':1,'b':1,'c':3}
dict4={k:v for k,v in dict3.items() }
print(dict4)    

print(' ----    Comprehensions For Loop in  dictionary----')
dict3={'a':1,'b':1,'c':3}
dict4={k +'xt':v*2 for k,v in dict3.items()  if v>2}
print(dict4)    

