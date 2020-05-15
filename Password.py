import random
import sys
import string
a=string.ascii_lowercase
b=string.ascii_uppercase
c=string.digits
d=string.punctuation
def gen():
    print("Enter the password length")
    e = int(input())# Enter password length
    f = random.randint(1,e-3)
    g = random.randint(1,e-f-2)
    h = random.randint(1,e-f-g-1)
    i = e-f-g-h
    a_1 = random.choices(a,weights=None,cum_weights=None,k=f)
    a_2 = random.choices(b,weights=None,cum_weights=None,k=g)
    a_3 = random.choices(c,weights=None,cum_weights=None,k=h)
    a_4 = random.choices(d,weights=None,cum_weights=None,k=i)
    pas = a_1 + a_2 + a_3 + a_4
    random.shuffle(pas)
    random.shuffle(pas)
    pas_string = ''.join(map(str ,pas))
    print("Here is your strong password: ",pas_string)
x = "start"
while x == "start" :
	gen()
	print("Type 'start' to generate another password or type anything to close")
	x = input()
else:
	print("Thank you for using my software................... Have a nice day")
	sys.exit()
