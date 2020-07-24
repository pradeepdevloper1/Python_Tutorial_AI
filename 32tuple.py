#  tuple is similar to list   its element cannoyt be changed once created

#empty tuple
t=()
print(t)

t2=(1,2,3)
print(t2)

print('----Nested Tuple----')
t3=(1,(1,2,3),['pradeep','kumar','yadav'])
print(t3)

print('----only parenthesis is not enough----')
t4=(1)
print(type(t4))

print('----, is Required ----')
t4=(1,)
print(type(t4))

print('----accessing element  ----')
t5=('pradeep','kumar','yadav')
print(t5[1])

print('----slicing  ----')
t6=(1,2,3,4,5,6,7,8,9)
print(t6[1:4])

print('----upto last second  element ----')
t7=(1,2,3,4,5,6,7,8,9)
print(t7[:-2])

# print('----immutable ----')
# t8=(1,2,3,4,[5,6,7,8,9])
# t8[2]='x'
# print(t8)

print('----immutable ----')
t9=(1,2,3,4,[5,6,7,8,9])
t9[4][1]='Pradeep'
print(t9)

print('----repeat element in tuple ----')
t10=(('Pradeep',)*4)
print(t10)

# print('----delete  in tuple ----')
# t10=(('Pradeep',)*4)
# del t10
# print(t10)

print('----count in tuple----')
t11=(1,2,3,4,3,1,2,2,2)
print(t11.count(2))


print('----index in tuple----')
t12=(1,2,3,4,3,1,2,2,2)
print(t11.index(3))

print('----Membership in tuple----')
t13=(1,2,3,4,3,1,2,2,2)
print(4 in t13)
print(7 in t13)


print('----length of tuple----')
t14=(1,2,3,4,3,1,2,2,2)
print(len(t14))


print('----sotted of tuple----')
t15=(1,2,3,4,3,1,2,2,2)
t16=sorted(t15)
print(t16)

print('----largest  of tuple----')
t17=(1,2,3,4,3,1,2,2,2)
print(max(t17))

print('----min of tuple----')
t18=(1,2,3,4,3,1,2,2,2)
print(min(t18))


print('----sum  of tuple----')
t20=(1,2,3,4,3,1,2,2,2)
print(sum(t20))
