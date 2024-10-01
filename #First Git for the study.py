#First Git for the study
#For fucntion
#1 step for function
test_list = ['one', 'two', 'three'] 
for i in test_list: 
     print(i)
# for 'variable' in 'list'
for i in ['one','two','three']:
     print (i)
# it is avaliable put list directly into for list
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
     print(first + last)
# (1,2) -> (first, last)
marks=[80,25,37,90,100]
number = 0
for mark in marks:
     number = number+1
     if mark>= 60:
          print("Student %d is passed." %number)
     else:
          print ("Student %d is failed"%number)
#
marks=[80,25,37,90,100]
number = 0
for mark in marks:
     number = number+1
     if mark<= 60:
          continue
     print("Student %d is passed." %number)
# continue = pass and go to next for loop
add=0
for i in range (1,11):
     add = add + i

print (add)
# range(a,b) - a~(b-1) range object
# range (a) - 0~(a-1)
marks=[80,25,37,90,100]
for number in range(len(marks)):
    if marks[number] < 60:
         continue
    print ("Student %d is passed" %(number+1))
# marks has 5 int
# range (5 = len(marks)) - repeat 0,1,2,3,4 = 5 times & print number +1 for student number
# marks[number] - bring numbers order to range (0,1,2,3,4) and compare with <60
#if the socore is under the 60, it pass and move to next number
for i in range(1,10):
     for j in range(1,10):
          print(i*j, end=" ")
     print(' ')
####### end=" " -> not keep the line / print (' ') change the line
