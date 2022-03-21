stop = False
from re import X
from login import Login
from file import handler

# Successfully implemented the transfer.
# Implement the transfer history function / modify pre-existing functions


reader = handler.reader; writer = handler.writer
Log = Login('accounts')
Log.greet()

# history function to log entry and failed or succesful status
def history(l_id,status):
    import time
    old = reader('history.bin')
    if status: x = 'Success'
    else: x = 'Failed'
    string = '{} {}'.format(x,time.ctime())

    old[l_id].append(string)

    writer(old,'history.bin')
# transaction history to log amounts withdrawn and deposited with timestamps
def tr_history(l_id,amount,wdraw = True,deposit = True):
    
    import time
    z = time.ctime().split()

    if wdraw and not(deposit):
        x = 'Withdrew'
    else: x = 'Deposited'
    string = '{} ${} at {} on {} {} {}'.format(x,amount,z[3],z[2],z[1],z[4])

    old = reader('pay.bin')
    old[l_id].append(string)

    writer(old,'pay.bin')

def tra_hist(log_id,t_id,t_amt):
    import time
    z = time.ctime().split()

    string = 'Wired ${}  to {} at {} on {} {} {}'.format(t_amt,t_id,z[3],z[2],z[1],z[4])
    string2 = 'Recieved ${}  from {} at {} on {} {} {}'.format(t_amt,log_id,z[3],z[2],z[1],z[4])
    old = reader('pay.bin')
    old[log_id].append(string)
    old[t_id].append(string2)
    writer(old,'pay.bin')

# None of the above function: for when the option entered is not valid
def nota():
    print("That ain't an option bruh! ")
print('Welcome to WeReign Bank.')

def deposit(p_id,amt,not_tr = True):
    bank_rec = reader('bank.bin')
                                      
    if log_id in bank_rec:
        bank_rec[p_id] += amt
    else:
        bank_rec[p_id] = amt
    if not_tr:tr_history(p_id,amt,wdraw = False,deposit = True)
    writer(bank_rec,'bank.bin')

def withdraw(p_id,w_amt,pr_tr):
    rec = reader('bank.bin')
    c_amt = rec[p_id]

    if w_amt  > c_amt:
        print('Insufficient Balance')
        return False
    else:

        rec[p_id] -= w_amt
        writer(rec,'bank.bin')
        
        tr_history(p_id,w_amt,wdraw= True,deposit = False)
        if pr_tr:
            print('${} withdrawn from your account'.format(w_amt))
        return True

'''
Create a reset function which empties all files and then resets them
'''


while not stop:
    
    choice = input('Select your next action \n [CREATE LOGIN EXIT] ')

    if choice.lower() == 'create':
        cr_id = input("Enter user id here ")
        cr_pw = input('Enter password here ')
        stat1 = Log.create(cr_id,cr_pw)

        if stat1[0]:
            print("Account Successfully Created")
            print('Welcome {name} to the best sht ever'.format(name = cr_id))
            
            # creating a history ledger
            h = reader('history.bin')
            h[cr_id] = []
            writer(h,'history.bin')

            i = reader('pay.bin')
            i[cr_id] = []
            writer(i,'pay.bin')

        if not stat1[0]:
            print(stat1[1])


    elif choice.lower() == 'login':
        log_id = input("Enter login id here ")
        status =  Log.login(log_id)
        
        stop1 = True
        if status[0]:   #if the password is accepted
            history(log_id,status[0])
            while stop1:
                choice2 = input("""How may we help you today
                [BALANCE, DEPOSIT, WITHDRAW, HISTORIES, TRANSFER, BACK]""").lower()

                if choice2 == 'balance':
                    print('balance')
                    balance = reader('bank.bin')[log_id]
                    
                    if int(balance) < 500:
                        print("You only have ${} in your balance.\n Please do Yoga and stop being nalla to earn more".format(balance))
                    
                    else:
                        print('You currently have ${} in your  account'.format(balance))

                elif choice2 == 'deposit':
                    amt = int(input("Enter deposit amount here "))
                    deposit(log_id,amt)
                    print("Successfully deposited ${} dough bruh!".format(amt))
                
                elif choice2 == 'withdraw':

                    w_amt = int(input('Enter withdraw amount here'))
                    withdraw(log_id,w_amt,pr_tr= True)
                                    


                elif choice2 == 'histories':
                    stop3 = False
                    while not stop3:
                        choice3 = input("Login/Transaction/Back")
                        if choice3.lower() == 'login':
                            x = reader('history.bin')
                            temp = x[log_id]
                            for s in temp:
                                date = s.split()
                                date.remove(date[1])
                                print(' '.join(date))

                        if choice3.lower() == 'transaction':
                            tr = reader('pay.bin')
                            temp = tr[log_id]
                            for _ in temp:
                                print(_)

                        if choice3.lower() == 'back':
                            stop3 = True


                elif choice2 == 'transfer':
                    t_p = input('Who do you want to transfer to ')
                    t_amt = int(input('How much do you want to transfer'))

                    chek_in = reader('accounts.bin')

                    if t_p.lower() in chek_in:
                        if withdraw(log_id,t_amt,pr_tr= False):
                            deposit(t_p,t_amt,not_tr = False)
                            print('Succesfully deposited {} to {}'.format(t_amt,t_p))
                            tra_hist(log_id,t_p,t_amt)



                
                elif choice2 == 'back':
                    print('Back to the Main Menu')
                    stop1 = False
                
                else:
                    nota()
    
        elif status == (False,'Incorrect Password'):
            history(log_id,status[0])    
    elif choice.lower() == 'exit':
        print('BIYE BIE BOYE BOI')
        stop = True

    else:
        nota()
        

