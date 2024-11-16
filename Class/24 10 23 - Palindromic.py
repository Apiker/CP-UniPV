#find palindromic numbers
#compute the lenght of the number (n of digits)
import math
#math.log10 #ci da la potenza di dieci p#er cui 10**x= n ===> se n ha due cifre è 1, se ne ha tre è 3,qualcosa: approssimando poi trovo il numero di cifre -1 
def lenght_n (n):
    if n==0:
        return 1
    else: 
        return math.floor(math.log(n)) + 1 and len(str(n))

def last_digit (n): #natural number n
   return n % 10   #this gives us the rest of the division by 10: 34:10=3.4 ==> 4

def first_digit (n):
   return n // 10**(lenght_n(n)-1)

def inner_nat(n):
    order = 10**(lenght_n(n)-1)
    without_first = (n-first_digit(n)*order)
    without_last = without_first // 10 #// da come risultato solo la parte intera
    return without_last


def is_palindromic_nat(n): #return if a number n is palindromic
   first = first_digit(n)
   second = last_digit(n)
   inner = inner_nat (n) 
   if lenght_n(n) == 1:
        return True
   elif lenght_n(n) >= 2 and first == second:
        return True
   elif lenght_n(n) >= 2 and first != second:
        return False
   else:
        return first == second and is_palindromic_nat(inner(n))

n = int(input ('dammi un numero: '))
print (n, 'is palindromic?', is_palindromic_nat(n))