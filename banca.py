while True:
    balance=10000
    print(" ATM ")
    print("""
    1) Balnce
    2) Withdraw
    3)Deposit
    4)Quit
    """)
    try:
        option=int(input("inserisci un opzione:"))
    except Exception as e:
        print("error",e)
        print("invia 1,2,3 or 4 only")
        continue
    if option ==1:
        print("balance",balance)
    if option ==2:
        print("balance",balance)
        Withdraw=float(input("enter Withdraw amount"))
        if Withdraw>0:
            forewardbalance=(balance-Withdraw)
        elif Withdraw>balance:
            print("no funs in account")
        else:
            print("none made")
    if option ==3:
        print("balance",balance)
        deposit=float(input("enter desposit"))
        if deposit>0:
             forewardbalance=(balance+deposit)
             print("forewarbalance",forewardbalance)
        else:
            print("none depsoit made")
    if option ==4:
        exit()