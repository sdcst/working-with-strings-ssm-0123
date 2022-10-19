#!python3
'''
##### Task 3
Split a string into 2 halves and insert a line break in the middle.  If doing so cuts a word in half, add a dash to the first line.  You will need to make use of the

len(str) function
this function returns the length of the string

(2 points)
'''



def split(input):
    '''
    parameters
    str input - string to be split
    
    return
    str new string with line break in the middle
    '''

    x = input
    print(len(x))
    s1 = x[:len(x)//2]
    s2 = x[len(x)//2:]
    print(s1,s2)
    print(len(s1),len(s2))
    print(s1[-1:])
    if s1[-1:] == " ":
        re = s1+"\n"+s2 
    else:
        if s2[0] == " ":
            re = s1+"\n"+s2
        else:
            re = s1+"-\n"+s2
    print(re)
    return re


if __name__ == "__main__":
    sentence = "There is a big balloon in the blue sky"
    assert split(sentence) == "There is a big ball-\noon in the blue sky"

    sentence = "I am a fat cat"
    assert split(sentence) == "I am a \nfat cat"

    sentence = "I was a fat cat"
    assert split(sentence) == "I was a\n fat cat"