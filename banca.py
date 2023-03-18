#il codice lo preso da python.hub
#io ho aggiunto il phone recharge,il deposit e la richiesta del pin
# verrà richiesto il pin, il pin è (1234)
#alcune cose sono da aggiornare, FIXME: durante l'esecuzione sono presenti dei bug
import random
while True:
    balance=10000
    print(" ATM  Unicredit Bank")
  
    
    print("""
        1)Balance        
        2)Withdraw
        3)Deposit
        4)phone recharge
        5)Quit
        """)
    
    try:
            option=int(input("enter a option:"))
            pin=int(input("enter  a pin: "))
            if pin==1234:
                print("correct pin")
            else:
                 print("error pin")
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
        print("balance",forewardbalance)
        deposit=float(input("enter desposit amount £: "))
        if deposit>0:
             forewardbalance=(balance+deposit)
             print("forewarbalance £",forewardbalance)
        else:
            print("none depsoit made")
    
    if option ==4:
        print("""
        1) vodafone
        2) tim
        3)windtre
        4)fastweb
        """)
        try:
            option1=int(input("enter a operator:"))
            print(option1)
            phone=int(input("enter phone number:"))
            recharge=int(input("enter the amount £: "))
            if recharge > 0:
                forewardbalance=(balance-recharge)
                print(forewardbalance)
                print("charging successful")
                #importo la libreria win10toast che consente di inviare le notifiche windows
                #per la ricarica telefonica invio un notifica
                #questa libreria è da aggiornare quando si fa l'update a python 3.11
                import win10toast
                toaster = win10toast.ToastNotifier()
                toaster.show_toast("charging successful", duration=10) 
            else:
                print("recharge not done")
        except Exception as c:
            print("error",c)
            print("enter 1,2,3 or 4 ")
    if option ==5:
        print("card withdrawal, withdraw it within 30 seconds")
        exit()
       





#L'istruzione try pone sotto controllo il blocco di codice associato. 
# Se il blocco di codice viene eseguito correttamente, 
# il controllo passa all'istruzione successiva al blocco except .