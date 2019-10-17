'''This modules consists of mathematical operations on different types of numbers.'''


def odd(n):
    if (n % 2 == 0):
        return False
    else:
        return True




def p_odds(n):#prints odd values

    i = 0
    while (i <= n):
        if (i % 2 != 0):
            print(i)
        i += 1
    else:
        return ''
def i_odds(n1,n2):#prints odd numbers in the given intervals
    while(n1<=n2):
        if(n1%2!=0):
            print(n1)
        n1+=1
    else:
        return''



def even(n1):  # print even or not
    if (n1 % 2 == 0):
        return True
    else:
        return False




def p_evens(n):#prints even values

    i = 0
    while (i <= n):
        if (i % 2 == 0):
            print(i)
        i += 1
    else:
        return None

def i_evens(n1,n2):#prints odd numbers in the given intervals
    while(n1<=n2):
        if(n1%2==0):
            print(n1)
            if(n1==n2):
                return None
        n1+=1





