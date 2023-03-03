import random

def gen_otp(digit):     #generazione otp
    otp=random.randrange(1,10)
    for otp in range(digit-1):
        otp=(otp+10)+random.randrange(0,10)
        return otp
otp1=gen_otp(6)
print(otp1)


#questa funzione è scritta anche in javascript in index.js