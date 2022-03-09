#import random 
import random
#input password length
passlen = int(input("Enterlength of password : "))
#store characters used in password
passchar="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
#generate new password
genpass = "".join(random.sample(passchar,passlen ))
#print generated password on screan
print ("\nPassword Is : " + genpass)
