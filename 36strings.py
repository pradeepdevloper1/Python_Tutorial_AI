#String is sequence of character
#  Unicode and AScii is encoding 
#in python String is sequence of unicode character


print('----String  single quotes--- ')
str1='singlequotes'
print(str1)

print('----String  double quotes--- ')
str1="doublequotes"
print(str1)

print('----String  triple quotes--- ')
str1='''triplequotes'''
print(str1)

print('----String  first character--- ')
str1='Pradeepkumar'
print(str1[0])
print(str1[len(str1)-1])
print(str1[-1])
print(str1[2:9])

# print('----String are immutable--- ')
# str1='Pradeepkumar'
# str1[4]='yhy'
# print(str1)

# print('---- delete in String --- ')
# str1='Pradeepkumar'
# del str1
# print(str1)


print('----concat in String --- ')
str1='Pradeep '
str2='kumar'
print(str1+str2)
print(str1*3)

print('----count  in String --- ')
count=0
str1='pradeep kumar'
for l in str1:
    if 'p' in l:
        count+=1
print(count)

print('----Membership  in String --- ')
str1='pradeep kumar'
print('p' in str1)

print('----lower  in String --- ')
str1='Pradeep Kumar'
print(str1.lower())

print('----upper  in String --- ')
str1='Pradeep Kumar'
print(str1.upper())

print('----split   in String --- ')
str1='This will split all the word in list '
print(str1.split())

print('----join   in String --- ')
print('-'.join(['This', 'will', 'split', 'all', 'the', 'word', 'in', 'list']))

print('----find in string---')
print('Good Morning '.find('Mo'))

print('----Replace  in string---')
s1='Bad Morning'
s2=s1.replace('Bad','Good')
print(s2)


print('------------Palindrome in String-------- ')
mystr='MadaM'
lowerstr=mystr.lower()
revstr=reversed(lowerstr)

if list(lowerstr)==list(revstr):
    print('Given String is palindrome')
else:
    print('Given String is  NOT palindrome')    



print('------------sort  in String-------- ')
mystr="python program to sor  words in alphabetical order"

words=mystr.split()
words.sort()

for word in words:
    print(word) 