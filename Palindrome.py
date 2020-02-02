def palindrome(checkThis):
	original = str(checkThis) #conversion to string
	reverse= original[::-1] # Reversing the string
	if original == reverse : #checkpoint : Checks if the original & Reverse are the same
		print(original,'is a Palindrome')
	else:
		print(original,'is not a Palindrome')


print('''Today's date is : 02 FEBRUARY 2020 is a PALINDROME in all date formats (UK,USA,ISO)
* 02.02.2020 in dd/mm/yyyy format (UK)
* 02.02.2020 in mm/dd/yyyy format (USA)
* 2020.02.02 in yyyy/mm/dd format (ISO)''')
#TEST CASES
palindrome(20200202)
palindrome('MOM')
palindrome(121)
palindrome(1213)
palindrome('madam')
palindrome('madame')
palindrome('racecar')
palindrome('malayalam')
