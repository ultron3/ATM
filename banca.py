#il codice lo preso da python.hub
#io ho aggiunto il phone recharge e il deposit
while True:
    balance=10000
    print(" ATM  Unicredit Bank")
  
    
    print("""
        1) Balance
        2) Withdraw
        3)Deposit
        4)phone recharge
        5)Quit
        """)
    
    try:
            option=int(input("enter a option:"))
            pin=int(input("enter  a pin: "))
            if pin==1234:
                print("correct")
            else:
                 print("error")
    except Exception as e:
            print("error",e,pin)
            print("enter 1,2,3 or 4 only")
            continue
    
    if option ==1:
        print("balance £",balance)
   
    if option ==2:
        print("balance £",balance)
        Withdraw=float(input("enter Withdraw amount £: "))
        if Withdraw>0:
            forewardbalance=(balance-Withdraw)
            print(forewardbalance)
        elif Withdraw>balance:
            print("no funs in account")
        else:
            print("none made")
    
    if option ==3:
        print("balance",balance)
        deposit=float(input("enter desposit amount £: "))
        if deposit>0:
             forewardbalance=(balance+deposit)
             print("forewarbalance £",forewardbalance)
        else:
            print("none depsoit made")
    
    if option ==4:
        phone=int(input("enter phone number:"))
        recharge=int(input("enter the amount £: "))
        if recharge > 0:
            forewardbalance=(balance-recharge)
            print(forewardbalance)
            print("charging successful")
        else:
            print("recharge not done")
    
    if option ==5:
        exit()