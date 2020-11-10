# FODA-Tasks-2020

**Fundamentals of Data Analysis Module-Assigned Tasks 2020**
***


# Introduction 

This document details a four task assignment, assigned as part of my studies for module - Fundamentals of Data Analysis. Each task, assigned at different stages throughout the term. 



## Task one 

Create A function that takes a list as input and returns a dictionary of unique items in the list as keys and the number of times each item appears as values. The Obejective is to create the function without the use of an imported library. 


 


To begin, we'll start with creating a variable called 'input_string' to capture the user input : [3]
 
    input_string = input("Please input a string of alpha numerical characters, using a space to separate: ")

The user is asked to 'input a string of alpha numerical characters, using a space to separate'. The reason the user is asked to use a space to separate each character within my code is shown below: 

*Input without spaces:*

    Please input a string of alpha numerical characters, using a space to separate: 157577TRR1

*Output*:

    '157577TRR1'

When the space is not included, the output will always return the input as one character. 

*Input with spaces:*

    Please input a string of alpha numerical characters, using a space to separate: 1 5 7 5 77 T R R 1

*Output*:

    '1 5 7 5 77 T R R 1'


The input function converts to sting, however, this tasks requires a list as input. 

I have included within the code to printout the input to the user, this way if spaces (whitespaces) have been overlooked, this is visible to the user. 

*Output:*

    You have input the following:  ['1', '5', '7', '5', '7', '7', 'T', 'R', 'R', '1']
    

Spliting string to list by using the .split() function. [2]

*Input:*


    x = input_string.split() # converting the input string to a list 
    print ("You have input the following: ", (x))

*Output:*


    You have input the following:  ['1', '5', '7', '5', '7', '7', 'T', 'R', 'R', '1']

Now we look at defining a function called 'counts', using the if/else statement; avoiding the use of an imported library [2]

*Input:*



    def counts (x): # defining a function called'counts' calling the input characters, requested above
    d = {} # creating a dictionary 
    for i in (x): # looping around each character 
    # Argument - if the current character in d equals d, then count same, else count as 1.
        if i in d: 
            d[i] = d[i] + 1
        else:
            d[i] = 1 
    return(d) # returning the value of d



    
*Output:*


    {'1': 2, '5': 2, '7': 3, 'T': 1, 'R': 2}


Returns a dictionary of unique items in the list as keys and the number of times each item appears as values.




***References***

[1] If statements/for statements;python https://docs.python.org/3.8/tutorial/controlflow.html#if-statements

[2] Built in functions; python https://docs.python.org/3/library/functions.html

[3] Accept list input from user; Pynative https://pynative.com/python-accept-list-input-from-user/






