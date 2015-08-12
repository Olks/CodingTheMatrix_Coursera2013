# -*- coding: utf-8 -*-
# Coding the Matrix: Linear Algebra through Computer Science Applications
# by Philip Klein
# author of answers: Olks

## Problem 1     - SUBLIST WITHOUT MULTIPLES OF GIVEN INTEGER
# input: list of numbers and a number.
# output: list of numbers not containing a multiple of num.
# example: given list = [1,2,4,5,7] and num = 2, return [1,5,7].
def myFilter(L, num): return [x for x in L if x%num!=0]


## Problem 2    - LIST OF SEQUENCES
# input: list L of non-negative integers.
# output: a list of lists: for every element x in L create a list containing 1; 2; : : : ; x.
# example: given [1,2,4] return [[1],[1,2],[1,2,3,4]].
def myLists(L): return [range(x+1)[1:] for x in L]


## Problem 3   - FUNCTION COMPOSITION
# input: two functions f and g, represented as dictionaries, such that g o f exists.
# output: dictionary that represents a function g o f.
# example: given f = {0:'a', 1:'b'} and g = {'a':'apple', 'b':'banana'}, return {0:'apple'; 1:'banana'}.
def myFunctionComposition(f, g): return {x:g[f[x]] for x in f.keys()}


## Problem 4
# Please only enter your numerical solution.
# Each of the following asks for the sum of two complex numbers. For each, fnd the solution.
# a. (3 + 1i) + (2 + 2i)
# b. (􀀀1 + 2i) + (1 􀀀 1i)
# c. (2 + 0i) + (􀀀3 + :001i)
# d. 4(0 + 2i) + (:001 + 1i)

complex_addition_a = 5+3j
complex_addition_b = 1j
complex_addition_c = -1+.001j
complex_addition_d = .001+9j



## Problem 5
# For each of the following, calculate the answer over GF(2).
# GF(2) is the smallest finite field.
# A finite field or Galois field (so-named in honor of Évariste Galois) 
# is a field that contains a finite number of elements. 
# As with any field, a finite field is a set on which the operations of 
# multiplication, addition, subtraction and division are defined 
# and satisfy certain basic rules. 
# Rules: like with logical XOR (albo .., albo..) and AND operations (1+1=0) 
# a. 1 + 1 + 1 + 0
# b. 1 . 1 + 0 . 1 + 0 . 0 + 1 . 1
# c. (1 + 1 + 1) . (1 + 1 + 1 + 1)
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0


## Problem 6
# Input: list of numbers
# Output: sum of numbers in the list
def mySum(L):
    current=0
    for x in L:
        current += x
    return current
	

	
## Problem 7
# Input: list of numbers
# Output: product of numbers in the list
def myProduct(L): 
    current=1
    for x in L:
        current *= x
    return current


## Problem 8
# Input: list of numbers
# Output: minimum number in the list
def myMin(L): 
    current=L[0]
    for x in L:
        if x < current:
            current = x
    return current


## Problem 9
# Input: list of strings
# Output: concatenation of all the strings in L
def myConcat(L):
    current=''
    for x in L:
        current += x
    return current



## Problem 10
# Input: list of sets
# Output: the union of all sets in L.
def myUnion(L):
    current=set()
    for x in L:
        current |= x
    return current


