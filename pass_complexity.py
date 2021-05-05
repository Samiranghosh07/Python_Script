password complexity check

import re
p = input('enter password here :')
ch= True
while(ch):
    
    if len(p)<6 or len(p)>16:
        print('Inavid password')
        break
        
    elif not re.search(r'[A-Z]',p):
        print('invalid password')
        break
        
    elif not re.search(r'[a-z]',p):
        print('invalid password')
        break
        
    elif not re.search(r'[0-9]',p):
        print('invalid password')
        break
        
    elif not re.search(r'[!@#$%^&*()_+]',p):
        print('invalid password')
        break
        
    else:
        print('valid password')
        break
        
