#random password generator

import string
import random

s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation
pass_len = int(input('enter password length'))
no_pass = int(input('how many password you want to generate ?'))
s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
print('your password is :')

for i in range(no_pass):
    print(i, '========>',   ''.join(random.sample(s,pass_len)))
