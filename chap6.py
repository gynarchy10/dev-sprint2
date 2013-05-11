# Enter your answers for chapter 6 here
# Name: Jenna Gopilan


# Ex. 6.6

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    """
    Determines if word is a palindrome
    """
#    print repr(word)
    if (len(word) == 1)or(len(word) == 0):
        return True
    else:
        if first(word) == last(word):
            return is_palindrome(middle(word))
        else:
            return False
    



# Ex 6.8

def gcd(a,b):
    """
    Finding the greatest common divisor of a and b without any remainder.
    """
#    print repr(a) + " and " + repr(b)
    if b == 0:
        return a
    else:
        remainder = a%b
        other = gcd(b,remainder)
        return other




 
a = is_palindrome("wow")    
print a

b = gcd(8,21)
print b
    
    