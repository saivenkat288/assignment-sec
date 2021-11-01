import bcrypt 
def password_encrypt(passwd) :
    passwd = passwd.encode('utf8')
    hashed = bcrypt.hashpw(passwd,bcrypt.gensalt()).decode('utf8')
    return hashed
def password_check(user_passwd,system_passwd) :
    user_passwd = user_passwd.encode('utf8')
    system_passwd = system_passwd.encode('utf8')
    return bcrypt.checkpw(user_passwd,system_passwd)

