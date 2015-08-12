# -*- coding: utf-8 -*-
## Task 1
# Use Python to fnd the number of minutes in a week.
minutes_in_week = 7*24*60

## Task 2
# Use Python to fnd the remainder of 2304811 divided by 47 
# without using the modulo operator %.
# (Hint: Use //.)
remainder_without_mod = 2304811-(2304811//47)*47

## Task 3
divisible_by_3 = (673+909)%3==0

## Task 4
# Assign the value -9 to x and 1/2 to y. 
# Predict the value of the following expression, then enter it
# to check your prediction:
x = -9
y = 1/2
stat = [2**(y+1/2) if x+10<0 else 2**(y-1/2)]
statement_val = 1

## Task 5
# Write a comprehension over {1; 2; 3; 4; 5} whose value is 
# the set consisting of the squares of the first five positive integers.
first_five_squares = { x**2 for x in {1,2,3,4,5} }

## Task 6
# powers of 2
first_five_pows_two = { 2**x for x in {0,1,2,3,4} }

## Task 7: enter in the two new sets
# The value of the comprehension, {x*y for x in {1,2,3} for y in {2,3,4}}, 
# is a seven-element set. Replace {1,2,3} and {2,3,4} with two other 
# three-element sets so that the value becomes a nine-element set.
X1 = { 1, 2, 3 }
Y1 = { 5, 6, 7 }

## Task 8: enter in the two new sets
# Replace {1,2,3} and {2,3,4} in the previous comprehension with two disjoint 
# (i.e. non-overlapping) three-element sets so that the value becomes 
# a five-element set.
X2 = { 0, 1, 2 }
Y2 = { 3, 6, 12 }

## Task 9
# Assign 10 to the variable base. Assign the set {0,1,2,3,4,5,6,7,8,9} 
# to the variable digits. Now write an expression using a comprehension 
# and base and digits whose value is the set of all at-most-three-digit numbers.
# Your expression should work for any base. For example, if you instead 
# assign 2 to base and assign {0,1} to digits, the value of your expression 
# should be {0,1,2,3,4,5,6,7} because this is the set of numbers
# that, base two, have at most three digits.
base = 10
digits = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
three_digits_set={x+y*base+z*base**2 for x in digits for y in digits for z in digits }

## Task 10
S = {1, 2, 3, 4}
T = {3, 4, 5, 6}
S_intersect_T = { x for x in S if x in T }

## Task 11
L_average = sum([20,10,15,75])/len([20,10,15,75]) # average of: [20, 10, 15, 75]

## Task 12
LofL = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
LofL_sum = sum([sum(x) for x in LofL]) # use form: sum([sum(...) ... ])

## Task 13
cartesian_product = [[x,y] for x in {'A','B','C'} for y in {1,2,3}] # use form: [ ... {'A','B','C'} ... {1,2,3} ... ]

## Task 14
S = {-4, -2, 1, 2, 5, 0}
zero_sum_list = [(x,y,z) for x in S for y in S for z in S if sum((x,y,z))==0 ] 

## Task 15
exclude_zero_list = [(x,y,z) for x in S for y in S for z in S if sum((x,y,z))==0 and (x!=0 or y!=0 or z!=0)]

## Task 16
first_of_tuples_list = [(x,y,z) for x in S for y in S for z in S if sum((x,y,z))==0 and (x!=0 or y!=0 or z!=0)][0]

## Task 17
L1 = [1,1,2] # <-- want len(L1) != len(list(set(L1)))
L2 = [1,3,2] # <-- same len(L2) == len(list(set(L2))) but L2 != list(set(L2))

## Task 18
odd_num_list_range = {2*x+1 for x in range(50)}

## Task 19
L = ['A','B','C','D','E']
range_and_zip = list(zip(range(5),L))

## Task 20
list_sum_zip = [sum((x,y)) for (x,y) in zip([10,25,40],[1,15,20])]

## Task 21
dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
k = 'James'
value_list = [dlist[j][k] for j in range(len(dlist))]

## Task 22
dlist = [{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Richard'}]
k = 'Bilbo'
value_list_modified_1 = [dlist[j][k] for j in range(len(dlist))] # <-- Use the same expression here
k = 'Frodo'
value_list_modified_2 = [dlist[j][k] if k in dlist[j] else 'NOT PRESENT' for j in range(len(dlist)) ] # <-- as you do here

## Task 23
square_dict = {x:x*x for x in range(100)}

## Task 24
D = {'red','white','blue'}
identity_dict = {x:x for x in D for y in D}

## Task 25
base = 10
digits = set(range(10))
representation_dict = {x+y*base+z*base**2:[z,y,x] for x in digits for y in digits for z in digits}

## Task 26
d = {0:1000.0, 1:1200.50, 2:990}
names = ['Larry', 'Curly', 'Moe']
listdict2dict = {names[x]:d[x] for x in d.keys()}

## Task 27
def nextInts(L): return [ x+1 for x in L ]

## Task 28
def cubes(L): return [ x**3 for x in L] 

## Task 29
# input: dictionary dct, list keylist consisting of the keys of dct
# output: list L such that L[i] = dct[keylist[i]] for i = 0; 1; 2; : : : ; len(keylist)-1 􀀀
# example: input dct={'a':'A', 'b':'B', 'c':'C'} and keylist=['b','c','a'], output
# ['B', 'C', 'A']
def dict2list(dct, keylist): return [dct[x] for x in keylist]


## Task 30 
# input: list L, list keylist of immutable items
# output: dictionary that maps keylist[i] to L[i] for i = 0; 1; 2; : : : ; len(L)-1 
# example: input L=['A','B','C'] and keylist=['a','b','c'], output
# {'a':'A', 'b':'B', 'c':'C'}
def list2dict(L, keylist): return {keylist[i]:L[i] for i in range(len(L))} 

