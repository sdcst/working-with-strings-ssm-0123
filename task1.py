#!python3

'''
Write a function that searches a string for all occurrences of the word "dog" and replaces it with "kitty"
You only need to modify the function replaceDog
The assertion tests are included so you can test your output
(4 points) 
'''

def replaceDog(input):
    '''
    parameters:
    str input - string to search and replace occurrences of dog with kitty

    return
    str - the modified string
    '''
    modifiedString = input
    modifiedString = modifiedString.split(' ')
    for i in range(0,len(modifiedString)):
        if modifiedString[i] == "dog":
            modifiedString[i] = "kitty"
    modifiedStringFinal = ""
    a = len(modifiedString)-1
    for i in range(0,len(modifiedString)):
        modifiedStringFinal = modifiedStringFinal + modifiedString[i]
        if i < a :
            modifiedStringFinal = modifiedStringFinal +" "
    

    



    return modifiedStringFinal






if __name__ == "__main__":
    '''
    assertion tests are basically a statement claiming truth
    if the statement is true, the program continues normally
    if the statement is not true, then an exception is thrown
    '''
    x = 'my dog has fleas'
    assert replaceDog(x) == 'my kitty has fleas'

    x = 'i have a dog and a goldfish as my pets'
    assert replaceDog(x) == 'i have a kitty and a goldfish as my pets'

