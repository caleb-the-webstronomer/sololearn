''' Password Validator :: Validate a password string with the following rules:
        - Minimum length is 5;
        - Maximum length is 10;
        - Should contain at least one number;
        - Should contain at least one special character;
        - Should not contain spaces;
        
'''

import re

password_rules = r'(?=[^\s]*\d)(?=[^\s]*\W)^[^\s]{5,10}$'

password = input()

print( "true" if re.match(password_rules, password ) != None else "false" )