# Andrea Egan - Task One  
# Creating a function called 'counts' that takes a list 
# as input and returns a dictionary of unique items in 
# the list as keys and the number of times each item 
# appears as values

input_string = input("Please input a string of alpha numerical characters, using a space to separate: ")  # asking the user to input characters

x = input_string.split() # converting the input string to a list 
print ("You have input the following: ", (x))

def counts (x): # defining a function called'counts' calling the input characters, requested above
    d = {} # creating a dictionary 
    for i in (x): # looping around each character 
    # Argument - if the current character in d equals d, then count same, else count as 1.
        if i in d: 
            d[i] = d[i] + 1
        else:
            d[i] = 1 
    return(d) # returning the value of d

print ( "Result: ", counts (x))
print ("End")