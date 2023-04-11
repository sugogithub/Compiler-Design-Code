# Compiler-Design-Code
# Ex1 - Program to count white spaces and number of lines
Ex1 - Input file: ex1in.txt
We're here to help
Tell us your problem
so we can get you the right help and support.
Ex1 - Output

*** Ex1 - Count White spaces and Number of Lines ***
Enter the File name to Process:ex1in.txt
The File Content is
*******************
We're here to help
Tell us your problem
so we can get you the right help and support.
************************
Number of lines: 3
Number of spaces: 15

# Ex2 -TOkens
Input file: ex2input.txt
(id+id)
c=a+b-10

Output:
enter the file name:ex2input.txt
The given Input is: (id+id)
c=a+b-10
*** The Tokens are ***
Operator: -> (
Name or Identitifier: id
Operator: -> +
Name or Identitifier: id
Operator: -> )
Newline : \n
Name or Identitifier: c
Operator: -> =
Name or Identitifier: a
Operator: -> +
Name or Identitifier: b
Operator: -> -
the values: 10
Newline : \n
End of the Code 0
the total number of tokens: 14
mumber of identifires: 5
the number of operators: 6
the number of values: 1

# Ex09 - Shift Reduce Parser for the following grammar
E=E+E | E*E | (E)| id

Output:
Enter valid Input String for Shift-Reduce Parsing:id+id*id$
Given Input word is: ['id', '+', 'id', '*', 'id', '$']
======================================================================
Stack          	InputBuffer              	Action         
======================================================================
[$]            	[id, +, id, *, id, $]    	Begins         
[$, id]        	[+, id, *, id, $]        	Shift          
[$, E]         	[+, id, *, id, $]        	E=id           
[$, E]         	[+, id, *, id, $]        	None           
[$, E, +]      	[id, *, id, $]           	Shift          
[$, E, +]      	[id, *, id, $]           	None           
[$, E, +]      	[id, *, id, $]           	None           
[$, E, +, id]  	[*, id, $]               	Shift          
[$, E, +, E]   	[*, id, $]               	E=id           
[$, E]         	[*, id, $]               	Reduce by E=E+E
[$, E, *]      	[id, $]                  	Shift          
[$, E, *]      	[id, $]                  	None           
[$, E, *]      	[id, $]                  	None           
[$, E, *, id]  	[$]                      	Shift          
[$, E, *, E]   	[$]                      	E=id           
[$, E]         	[$]                      	Reduce by E=E*E
[$, E]         	[$]                      	Accepted - Done

