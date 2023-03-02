import random

def genotp(digit):
    otp=random.randrange(1,10)
    for otp in range(digit-1):
        otp=(otp+10)+random.randrange(0,10)
        return otp
otp1=genotp(6)
print(otp1)


#una funzione esiste anche in index.js