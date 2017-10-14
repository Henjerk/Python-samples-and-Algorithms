#!/usr/bin/python
# -*- coding: ascii -*-

import random as rd
from itertools import permutations
import re
import csv


#QUESTION ONE : Solution
x = rd.randint(0,100) #choose a random value between 1 and 100

def create_palindrome(y):
	yr = str(y)[::-1] #reverse provided integer
	isPalindrome(str(y)+yr) #append reversed integer to original to create a palindrome

def isPalindrome(z):
	if int(z) > 1000000: #check if value is below 1000000
	    	print "false"
	else :
	    if z == z[::-1]: #check if provided value is equal to reversed value
		print "palindrome is %s" %z
	    else :
	    	rev(z)


#QUESTION TWO : Solution
def regularexp():
	st = "This is my example"
	match = re.search(r'\w\w\w\w\s\w',st)
	if match:
		print 'found', match.group()
	else:
		print "Not found"

	match = re.search(r'b\w+','foobar')
	if match:
		print 'found', match.group()
	else:
		print "Not found"


#QUESTION THREE : Solution
def get_products():
	integers = [1,2,3,4]
	product_integers = []
	#loop thruough the list
	for i in integers:
		for x in integers:
			#check if current value of i is equal to current value of x
			if(i != x):
			    pdt =  i * x
			    #add products to product list
			    product_integers.append(pdt)
			else :
				pass
	print product_integers
	


#QUESTION FOUR : Solution
def remove_instance():
	value = 3

	#Approach 1 : list comprehension approach
	array_values = [3,2,2,3]
	#recreating the same array but excluding values that are equal to the provided value
	array_values =[x for x in array_values if x != value]
	print array_values

	#Approach 2 :Ordinary approach
	for x in array_values:
		if x == (x+1): #check if the next value is equal to the current value
			array_values.remove(x) #remove the value if found
	print array_values


#QUESTION FIVE : Solution
def compression():
	my_string = 'aabccccaaa'
	output_string = ''
	counter = 1 #initialise my counter to 1 for the current value that being held
	for key, value in enumerate(my_string):
		if key < 9: #check that keys don't exceed the String length, prevent out of bounds exceptions
			if value == (my_string[key+1]): #check if the current value  is equal to next value
				counter  = counter + 1 #if its equal, increment counter
			else:
				output_string = output_string+value + str(counter) # else, append the value and current counter value to the output string
				counter = 1 #reset our counter
	output_string = output_string + value + str(counter) #append the value and current counter value to the output string outside the loop to cater for last value
	if(len(output_string) < len(my_string)): #check if output string size is less than provided string
		print output_string		
	else:
		return my_string

#QUESTION SIX : Solution
def perm():	 
	# Get all permutations of length 2
	# and length 2
	perm = permutations([1, 2, 3], 3)
	 
	# Print the obtained permutations
	for i in list(perm):
	    print i


#QUESTION SEVEN : Solution
def find_one():
	twice_numbers= 0 #counter for numbers that appear twice
	single_number=0	#counter for numbers that appear once
	finished_number = [] #list to store counted numbers
	array_values = [3,2,2,3,5,4,5,6,4]
	for x in array_values: #loop through the array
		if x not in  finished_number: #check if the number exists in the list of counted numbers
			for y in array_values: #loop through the array again to search for the current value other instances
				if x == y: 
					twice_numbers = twice_numbers+1 #increment twice number counter if values are the same
				else:
					pass
			if twice_numbers < 2: #check if twice number counter is less than two 
				single_number = 1 #increment single number counter 
				onevalue = x # Since its one, store it in this value for easy accessibility
			else:
				twice_numbers = twice_numbers * 0 #reset twice number counter
			finished_number.append(x) #store the counted numbers
		else:
			pass
	print onevalue

#OR , using a dictionary
def find_one1():
	twice_numbers= 0
	dict = {}
	finished_number = []
	array_values = [3,2,2,3,5,4,5,6,4]
	for x in array_values:
		if x not in  finished_number:
			for y in array_values:
				if x == y:
					twice_numbers = twice_numbers+1
				else:
					pass
			if twice_numbers != 2:
				dict[x] = 1
			else:
				twice_numbers = twice_numbers * 0
				dict[x] = 2
			finished_number.append(x)
		else:
			pass
	for key, value in dict.items():
		if value == 1:
			print key
		else:
			pass


#QUESTION EIGHT : Solution
def seperate():
	num = 384
	int_str = [int(i) for i in str(num)]
	y = int(int_str[0]) + int(int_str[1])
	if(len(str(y)) == 2):
		int_str1 = [int(i) for i in str(y)]
		print int(int_str1[0]) + int(int_str1[1])
	else:
		print y 

#Or, simplified way
def process_number(my_number):
    result =0
    #check if number has more than one digit, if so jst return the number
    if len(str(my_number))<2:
        return my_number
    # pass number into a string and process string
    else:
        for val in str(my_number):
            result += int(val)
    #call function recursively to process result until only one number is left
        return process_number(result)
    

#QUESTION NINE : Solution
def twoSum(numbs, target):
        for x,y in enumerate(numbs):
            for w,z in enumerate(numbs):
                if (y + z) == target and (x != w):
                    	return [x,w]


#QUESTION TEN : Solution
def sequence():
	seq = '2a3b4c'
	outseq = ''
	outodd = seq[1::2]
	outeven = seq[0::2]

	print outodd + "--" + outeven
	for x,y in enumerate(outeven):
		for z in xrange(int(y)):
			outseq = outseq + outodd[x]
	print 'Original -->' + seq
	print 'Result --->' + outseq


#QUESTION ELEVEN : Solution 
def isPalindrome2(self, x):
		#check if number is not less than zero
		if x < 0:
			return False
		div = 1

        # initialize how many zeros in the variable div
		while((x/div) >= 10):
			div = div * 10

		#check if x is not zero
		while(x!=0):
			left = x/div
			right = x% 10

			if left != right:
				return False
			#change the value of x and div for the loop to continue
			x = ((x%div)/10)
			div = div/100

		return True


