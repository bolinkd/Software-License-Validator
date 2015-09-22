Assignment 1
Dustin Bolink
V00747883

Software License Validator

In order to generate a License File:
1. run command 
	> python Validator.py --key --generate

	--generate will generate a license that will expire in 1 month
	--key will create the public and private keys

In order to test a Software License:
1. run command
	> python Validator.py --test

	--test will confirm that the license has not expired or been tampered with


In order to test for Tampering:
	1. edit the date for the software license to 10/10/2010
		- the license will have expired
	2. edit the date for the software license to 10/10/2099
		- the software license will have been tampured with
	(rerun the program to reset the digital signature and software license)
	3. change the digital signature by adding or removing a character
		- the software licese will have been tampured with

Two ways people can circumvent my implemeted fail safes
	1. There is no validation from person to person, so as long as the digital signature and software license are passed around the software will not be able to notice and problems.

	2. The hackers could go into my program and remove the part that tests for files as there is no file validation and everything is run remotly.