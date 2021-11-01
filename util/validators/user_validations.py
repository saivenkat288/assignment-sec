import re
def emailVerifier(email):  
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if(re.search(regex,email)):  
        return True        
    else:  
        return "Email is invalid"
def nameVerifier(name):
    if(bool(re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', name))):  
        return True        
    else:  
        return "Name is Invalid"
def passwordVerifier(password):
    if(bool(re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password))):  
        return True        
    else:  
        return "Enter a password with atleast 8 charecters long contains an Uppercase , a Lowercase,Numbers,Special charecters"


