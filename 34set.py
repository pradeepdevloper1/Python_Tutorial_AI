#Set 
#Set is an unordered collection of items, non index


s={1,2,3,4,5,6}
print(type(s))
print(s)

print('---set does not allow duplicate')
s1={1,2,3,1,2,3,5,5,5,4,5,6}
print(s1)

print('---initialize set')
s1=set()
print(type(s1))

print('---set are mutable')
s1.add(2)
print(s1)

print('---add multiple item in set')
s1.update([1,3,4])
print(s1)

print('---add list and set')
s1.update([4,6],{1,2,3,4})
print(s1)

print('---discard set')
s2={1,2,3,4,5,6}
s2.discard(4)
print(s2)

print('---remove set')
s2={1,2,3,4,5,6}
s2.remove(3)
print(s2)

print('---discard ement when not exist in  set')
s2={1,2,3,4,5,6}
s2.discard(7)
print(s2)

# print('---remove element when not exist in  set')
# s2={1,2,3,4,5,6}
# s2.remove(7)
# print(s2)

print('---pop element in  set')
s2={1,2,3,4,5,6}
s2.pop()
print(s2)

print('---clear in  set')
s2={1,2,3,4,5,6}
s2.clear()
print(s2)


print('---operation in   set')
s1={1,2,3,4,5,6}
s2={3,4,5,6,7,8}
print(s1|s2)

print('---union  in   set')
s1={1,2,3,4,5,6}
s2={3,4,5,6,7,8}
print(s1.union(s2))

print('---and   in   set')
s1={1,2,3,4,5,6}
s2={3,4,5,6,7,8}
print(s1 &s2)

print('---intersection  in   set')
s1={1,2,3,4,5,6}
s2={3,4,5,6,7,8}
print(s1.intersection(s2))

print('---minus   in   set')
s1={1,2,3,4,5,6}
s2={3,4,5,6,7,8}
print(s1 -s2)

print('---diffrence  in   set')
s1={1,2,3,4,5,6}
s2={3,4,5,6,7,8}
print(s1.difference(s2))


print('---symmetric diffrence  in   set')
s1={1,2,3,4,5,6}
s2={3,4,5,6,7,8}
print(s1^s2)

print('---symmetric diffrence  in   set')
s1={1,2,3,4,5,6}
s2={3,4,5,6,7,8}
print(s1.symmetric_difference(s2))

print('---is subset  in   set')
s1={1,2,3,4,5,6}
s2={3,4,5}
print("set s2 is subset of s1:-----",s1.issubset(s1))


#frozen sets are mutable
#set as a key in dect
#set as key in frozen set

# print('---Frozen Set---')
# s3=frozenset([1,2,3,4])
# s3.add(22)
# print(s3)


print('---Frozen Set---')
s3=frozenset([1,2,3,4])
s4=frozenset([4,5,6,4])
print(s3 | s4)
