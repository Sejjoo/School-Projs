#sys module
import sys

#main menu loop
main = "yes"
while main == "yes":
    print("-------------------")
    print("1. Honey-Busy-Bee")
    print("2. ATM Simulator")
    print("3. Data Collector")
    print("4. Terminate Program")
    print("-------------------")
    print("ok")

    #main menu selection
    try:
        menu = str(input("Select a menu [1/2/3/4]: "))
    except ValueError:
        print()
        continue
    pass

    #honey-busy-bee
    if menu == '1' :
        #honey-busy-bee loop
        hbb = True
        while hbb:
            #displays a list from 1-100
            x = (list(range(1,101)))
            #counts every integer in the list
            for x in (range(1,101)):
                count = 0
                #checks if an integer is prime
                for i in range(1,x + 1):
                    if x % i == 0:
                        count += 1                
                if count == 2:
                    print ("Honey")
                #integers divisible by 3 and 5
                elif x % 3 == 0 and x % 5 == 0:
                    print("Busy Bee")
                #integers divisible by 3 only
                elif x % 3 == 0:
                    print ("Busy")
                #integers divisible by 5 only
                elif x % 5 == 0:
                    print ("Bee")
                #integers not included in the conditions
                else:
                    print (x)
            #loop that asks to run honey-busy-bee again
            again = True
            while again:
                again = str(input("Do you want to run the Honey-Busy-Bee again? [y/n] :"))
                #"y" runs the honey-busy-bee again
                if again == "y":
                    print()
                    again = False
                    hbb = True
                #"n" asks the user to return to main menu
                elif again == "n":
                    hbb = False
                    #loop for asking the user to go back to main menu
                    run_again = True
                    while run_again:
                        run_again = str(input('''Do you want to go back to main menu? 
(Note: Selecting "n" will automatically terminate the program)[y/n] '''))
                        #'y' directs the user to the main menu
                        if run_again == "y":
                            run_again = False
                            again = False
                            main = "yes"
                        #'n' terminates the whole program
                        elif run_again == "n":
                            print("Thank you for using the program!")
                            sys.exit()
                        #an invalid input will ask the user again
                        else:
                            print("Invalid Input")
                            run_again = True
                #an invalid input will ask the user again
                else:
                    print('Invalid Input')
                    hbb = False
                    again = True
    #atm simulator       
    elif menu == '2':
        #current and savings initial balance
        c_balance = 0
        s_balance = 0
        #function for current deposit
        def c_deposit(amount):
            global c_balance
            c_balance = c_balance + amount
            print ('\nYou have deposited PHP ', amount)
            print ('\nYour Current Account Balance is PHP ', c_balance)
        #function for savings deposit
        def s_deposit(amount):
            global s_balance
            s_balance = s_balance + amount
            print ('\nYou have deposited PHP ', amount)
            print ('\nYour Savings Account Balance is PHP ', s_balance)
        #function for current withdrawal
        def c_withdraw(amount):
            global c_balance
            c_balance = c_balance - amount
            print('\nYou have withdrawed PHP', amount)
            print('\nYour Current Account balance is PHP ', c_balance)
        #function for savings withdrawal
        def s_withdraw(amount):
            global s_balance
            s_balance = s_balance - amount
            print('\nYou have withdrawed PHP', amount)
            print('\nYour Savings Account balance is PHP ', s_balance)
        #function for current transfer
        def c_transfer(amount):
            global c_balance
            global s_balance
            c_balance = c_balance - amount
            s_balance = s_balance + amount
            print('\nYou have transfered PHP ', amount, 'to your Savings Account')
            print('\nYour Current Account balance is PHP ', c_balance)
            print('\nYour Savings Account balance is PHP ', s_balance)
        #function for savings transfer   
        def s_transfer(amount):
            global s_balance
            global c_balance
            s_balance = s_balance - amount
            c_balance = c_balance + amount
            print('\nYou have transfered PHP', amount, 'to your Current Account')
            print('\nYour Savings Account balance is PHP ', s_balance)
            print('\nYour Current Account balance is PHP ', c_balance)
        #function for balance inquiry
        def balance():
            global c_balance
            print('\nYour Current Account balance is PHP ',c_balance)
            global s_balance
            print('\nYour Savings Account balance is PHP ',s_balance)
            

        #loop for PIN authentication
        enterpin = True
        while enterpin:
            pin = str(input(' Enter a 6-digit PIN: '))
            #checks if input is an integer
            if pin.isdigit():
                pass
                #allows the user to input exactly 6 integers
                if len(pin) == 6:
                    cpin = str(input(' Please enter your PIN again: '))
                    #checks if first input is the same as second input
                    if pin == cpin:
                        confirm = str(input(' Is this your final PIN? [y/n]'))
                        #'y' directs the user to the ATM simulator menu
                        if confirm == 'y':
                            print ('---------------------------------------')
                            print ("You have successfully created an account!")
                            print ('---------------------------------------')
                            print ('Welcome to the EITFRM ATM Simulator!')
                            enterpin = False
                        #'n' allows the user to repeat and create PIN again
                        elif confirm == 'n':
                            enterpin = True
                        #invalid input allows the user to repeat and create PIN again
                        else:
                            print('Invalid Input')
                            enterpin = True
                    #incorrect inputted second pin allows the user to repeat creating a PIN
                    else:
                        print('Incorrect PIN')
                        enterpin = True
                #inputting a PIN ≠ 6 allows the user to create another PIN
                else:
                    print ('You should enter a 6-digit PIN')
                    enterpin = True
            #inputs other than integers allows the user to create another PIN
            else:
                print ('The PIN only accepts integers')
                enterpin = True

        #loop for the main atm simulator    
        option = True
        while option:
            print('---------------------------------------')
            print('''
1) Deposit
2) Withdraw
3) Transfer
4) Balance Inquiry
5) Exit
                    ''')
            print('---------------------------------------')
                    
            option = str(input(' Please select an option.[1/2/3/4/5] '))
            #deposit option
            if option == '1':
                print('''---------------------------------------
[C]urrent Account
[S]avings Account
---------------------------------------''')
                #loop for account selection
                depacc = True
                while depacc:
                    account = str(input('Select an account: [c/s]'))
                    #selection for current account
                    if account == 'c':
                        print('Your Current Account balance is PHP ',c_balance)
                        #loop for current deposit
                        cdep = True
                        while cdep:
                            try:
                                cdep = int(input('''\n Enter the amount you want to deposit to your current account
(Note: PHP 100 is the minimum amount): '''))
                            except ValueError:
                                print('Invalid Input')
                                continue
                            pass
                            #0 deposit is considered invalid transaction
                            if cdep == 0:
                                print ('You have entered an invalid amount')
                                cdep = True
                            #the atm requires atleast PHP 100 deposit
                            elif cdep < 100:
                                print('The minimum amount you can deposit is PHP 100')
                                cdep = True
                            #allows the user to deposit in current account
                            else:
                                c_deposit(cdep)
                            #loop asking the user to have another deposit or not
                            cdp = True
                            while cdp:
                                cdp = (str(input('Do you want to have another deposit? [y/n]')))
                                #'y' allows the user to deposit again to his current account
                                if cdp == 'y':
                                    cdp = False
                                    cdep = True
                                #'n' returns the user to the menu of the atm simulator
                                elif cdp == 'n':
                                    cdp = False
                                    cdep = False
                                    depacc = False
                                    option = True
                                #invalid input asks the user again to have another deposit or not
                                else:
                                    print('Invalid Input')
                                    cdep = False
                                    option = False
                                    cdp = True
                    #selection for savings account           
                    elif account == 's':
                        print('Your Savings Account balance is PHP ',s_balance)
                        #loop for savings deposit
                        sdep = True
                        while sdep:
                            try:
                                sdep = int(input('''\n Enter the amount you want to deposit to your savings account
(Note: PHP 100 is the minimum amount): '''))
                            except ValueError:
                                print('Invalid Input')
                                continue
                            pass
                            #0 deposit is considered invalid transaction
                            if sdep == 0:
                                print ('You have entered an invalid amount')
                                sdep = True
                            #atm requires atleast PHP 100 deposit
                            elif sdep < 100:
                                print ('The minimum amount you can deposit is PHP 100')
                                sdep = True
                            #allows the user to deposit in savings account
                            else:
                                s_deposit(sdep)
                            #asks the user to have another deposit or not
                            sdp = True
                            while sdp:
                                sdp = (str(input('Do you want to have another deposit? [y/n]')))
                                #'y' allows the user to deposit again to his savings account
                                if sdp == 'y':
                                    sdp = False
                                    sdep = True
                                #'n' returns the user to the menu of the atm
                                elif sdp == 'n':
                                    sdp = False
                                    sdep = False
                                    depacc = False
                                    option = True
                                #invalid input asks the user again to have deposit or not
                                else:
                                    print('Invalid Input')
                                    sdep = False
                                    option = False
                                    sdp = True
                    #invalid input asks the user to select an account again
                    else:
                        print('Invalid Input')
                        option = False
                        depacc = True
            #withdraw option         
            elif option == '2':
                print('''---------------------------------------
[C]urrent Account
[S]avings Account
---------------------------------------''')
                #loop for account selection
                widacc = True
                while widacc:
                    account = str(input('Select an account: [c/s]'))
                    #selection for current withdrawal
                    if account == 'c':
                        print('\nCurrent Balance: PHP ', c_balance)
                        #loop for current withdrawal
                        c_wid = True
                        while c_wid:
                            try:
                                c_wid = (int(input(''' Enter the amount you want to withdraw
(Note: PHP 100 is the minimum amount): ''')))
                            except ValueError:
                                print('Invalid Input')
                                continue
                            pass
                            #withdrawing amount less than balance is invalid
                            if c_wid > c_balance:
                                print('You have insufficient balance for your withdrawal')
                                wid = True
                            #negative input is invalid
                            elif c_wid is not abs(c_wid):
                                print ('You have entered an invalid amount')
                                c_wid = True
                            #the atm requires atleast PHP 100 withdrawal
                            elif c_wid < 100:
                                print('The minimum amount you can withdraw is PHP 100')
                                c_wid = True
                            #allows the user to withdraw in current account
                            else:
                                c_withdraw(c_wid)
                            #loop asking the user to have another withdrawal
                            cwd = True
                            while cwd:
                                cwd = str(input('Do you want to withdraw again? [y/n]'))
                                #'y' allows the user to withdraw again to his current account
                                if cwd == 'y':
                                    cwd = False
                                    c_wid = True
                                #'n' returns the user to the menu of the atm simulator
                                elif cwd == 'n':
                                    cwd = False
                                    c_wid = False
                                    widacc = False
                                    option = True
                                #invalid input asks the user again to have another withdrawal or not
                                else:
                                    print('Invalid Input')
                                    c_wid = False
                                    option = False
                                    cwd = True
                    #selection for savings account
                    elif account == 's':
                        print('\nSavings Balance: PHP ', s_balance)
                        #loop for savings withdrawal
                        s_wid = True
                        while s_wid:
                            try:
                                s_wid = (int(input(''' Enter the amount you want to withdraw
(Note: PHP 100 is the minimum amount): ''')))
                            except ValueError:
                                print('Invalid Input')
                                continue
                            pass
                            #withdrawing amount less than balance is invalid
                            if s_wid > s_balance:
                                print('You have insufficient balance for your withdrawal')
                                s_wid = True
                            #negative input is invalid
                            elif s_wid is not abs(s_wid):
                                print ('You have entered an invalid amount')
                                s_wid = True
                            #the atm requires atleast PHP 100 withdrawal
                            elif s_wid < 100:
                                print('The minimum amount you can withdraw is PHP 100')
                                s_wid = True
                            else:
                            #allows the user to withdraw in savings account
                                s_withdraw(s_wid)
                            #asks the user to have another withdrawal or not
                            swd = True
                            while swd:
                                swd = str(input('Do you want to withdraw again? [y/n]'))
                                #'y' allows the user to withdraw again to his savings account
                                if swd == 'y':
                                    swd = False
                                    s_wid = True
                                #'n' returns the user to the menu of the atm
                                elif swd == 'n':
                                    swd = False
                                    s_wid = False
                                    widacc = False
                                    option = True
                                #invalid input asks the user again to have another withdrawal or not
                                else:
                                    print('Invalid Input')
                                    s_wid = False
                                    option = False
                                    swd = True
                    #invalid input asks the user to select an account again
                    else:
                        print('Invalid Input')
                        option = False
                        widacc = True
                            
            #transfer option
            elif option == '3':
                print('''---------------------------------------
[C]urrent to Savings
[S]avings to Current
---------------------------------------''')
                #loop for selecting transfer option
                tfacc = True
                while tfacc:
                    account = str(input('\nSelect your transfer: [c/s]'))
                    #'c' allows the user to transfer from current to savings
                    if account =='c':
                        print('\nCurrent Balance: PHP ', c_balance)
                        print('\nSavings Balance: PHP ', s_balance)
                        #loop for entering amount for transfer
                        c_trans = True
                        while c_trans:
                            try:
                                c_trans = (int(input(''' Enter the amount you want to transter to Savings Account
(Note: PHP 100 is the minimum amount): ''')))
                            except ValueError:
                                print('Invalid Input')
                                continue
                            pass
                            #transfer input less than balance is invalid
                            if c_trans >c_balance:
                                print ('You have insufficient balance for your transaction')
                                c_trans = True
                            #negative input is invalid
                            elif c_trans is not abs(c_trans):
                                print ('You have entered an invalid amount')
                                c_trans = True
                            #atm requires atleast PHP 100 transfer
                            elif c_trans < 100:
                                print ('The minimum ammount you can transfer to Savings account is PHP 100')
                                c_trans = True
                            else:
                            #allows the user to transfer from current to savings
                                c_transfer(c_trans)
                            #loop asking the user to transfer again or not
                            ctf = True
                            while ctf:
                                ctf = str(input('Do you want to transfer again? [y/n]'))
                                #'y' allows the user to transfer again
                                if ctf == 'y':
                                    ctf = False
                                    c_trans = True
                                #'n' returns the user to the atm menu
                                elif ctf == 'n':
                                    ctf = False
                                    c_trans = False
                                    tfacc = False
                                    option = True
                                #invalid input asks the user again to transfer or not
                                else:
                                    print('Invalid Input')
                                    c_trans = False
                                    option = False
                                    ctf = True
                    #'s' allows the user to transfer from savings to current              
                    elif account == 's':
                        print('\nSavings Balance: PHP ', s_balance)
                        print('\nCurrent Balance: PHP ', c_balance)
                        #loop for entering amount for transfer
                        s_trans = True
                        while s_trans:
                            try:
                                s_trans = (int(input(''' Enter the amount you want to transter to Current Account
(Note: PHP 100 is the minimum amount): ''')))
                            except ValueError:
                                print('Invalid Input')
                                continue
                            pass
                            #transfer input less than balance is invalid
                            if s_trans > s_balance:
                                print ('You have insufficient balance for your transaction')
                                s_trans = True
                            #negative input is invalid
                            elif s_trans is not abs(s_trans):
                                print ('You have entered an invalid amount')
                                s_trans = True
                            #atm requires atleast PHP 100 transfer
                            elif s_trans < 100:
                                print ('The minimum ammount you can transfer to Savings account is PHP 100')
                                s_trans = True
                            #allows the user to transfer from savings to current
                            else:
                                s_transfer(s_trans)
                            #loop asking the user to transfer again or not
                            stf = True
                            while stf:
                                stf = str(input('Do you want to transfer again? [y/n]'))
                                #'y' allows the user to transfer again
                                if stf == 'y':
                                    stf = False
                                    s_trans = True
                                #'n' returns the user to the atm menu
                                elif stf == 'n':
                                    stf = False
                                    s_trans = False
                                    tfacc = False
                                    option = True
                                #invalid input asks the user again to transfer or not
                                else:
                                    print('Invalid input')
                                    s_trans = False
                                    option = False
                                    stf = True
                    #invalid inputs asks the user to select a transfer option again                
                    else:
                        print('Invalid Input')
                        option = False
                        tfacc = True
                            
            #balance inquiry option                   
            elif option == '4':
                    balance()
            #option to go back to main menu        
            elif option == '5':
                #loop asking to go back to main menu
                mm = True
                while mm:
                    mm = str(input('Would you like to go back to the main menu? [y/n]'))
                    #'y' returns the user to the main menu
                    if mm =='y':
                        mm = False
                        option = False
                        main = "yes"
                    #'n' returns the user to the atm menu
                    elif mm == 'n':
                        mm = False
                        option = True
                    #invalid input asks the user again to go back to main menu or not
                    else:
                        print('Invalid Input')
                        mm = True
                        option = False
            #invalid input returns the user to the atm menu      
            else:
                print ('\nInvalid Input')
                option = True

    #data collector
    elif menu == '3':
        
        #List Functions

        #append function
        def apndfunc ():
            typ_list.append(apnd_item)
            print (typ_list)
        #insert function
        def insrfunc (**items):
            typ_list.insert(insr_inx, insr_item)
            print(typ_list)
        #sort function
        def sortfunc (*items):
            typ_list.sort()
            print (typ_list)
        #reverse function
        def revfunc(*items):
            typ_list.reverse()
            print(typ_list)
            
        #Set Functions

        #add function
        def addfunc():
            typ_set.add(add_item)
            print(typ_set)
        #discard function
        def discfunc(*item):
            typ_set.discard(disc_item)
            print(typ_set)
        #update function
        def updtfunc(*item):
            typ_set.update(updt_item)
            print(typ_set)
        #difference1 function
        def dif1func(**item):
            dif1_chc= typ_set.difference(new_items)
            print(dif1_chc)
        #difference2 function
        def dif2func(*item):
            dif2_chc= new_items.difference(typ_set)
            print(dif2_chc)
            
        #Tuple Functions

        #tuple variable
        typ_tup =()
        #append function
        def apndfunc_tup():
            global typ_tup
            tup2lst.append(apdtup_item)
            typ_tup=tuple(tup2lst)
            print(typ_tup)
        #insert function
        def insrfunc_tup (**items):
            global typ_tup
            insrtup2lst.insert(tupinsr_inx, tupinsr_item)
            typ_tup= tuple(insrtup2lst)
            print(typ_tup)
        #sort function
        def sortfunc_tup (*items):
            global typ_tup
            sortup2lst.sort()
            typ_tup=tuple(sortup2lst)
            print (typ_tup)
        #reverse function
        def revfunc_tup(*items):
            global typ_tup
            revtup2lst.reverse()
            typ_tup=tuple(revtup2lst)
            print(typ_tup)

          
          
            
        print('''\nHello user! This is a program that allows you to
utilize list, tuple, set, and dictionary data types.''')
        #loop for data collection menu
        choice = True
        while choice:
            print('---------------------------------------------------')
            print('''
a. List
b. Tuple
c. Set
d. Dictionary
e. Exit''')
            print('\n---------------------------------------------------')
            choice =(input("Please select an option: [a/b/c/d/e] "))
            print()
            #'a' allows the user to use a list function
            if choice in ('a'):
                list_items = input("Please enter item/s separated by a comma (,):")
                typ_list= list_items.split(",")
                typ_lis=list_items.strip()
                print ('\nThe list you have created is:', typ_list)
                #loop for list modification
                mod_choice = True
                while mod_choice:
                    mod_choice = input('Would you like to further modify the list? [y/n]:')
                    #'y' displays the available list modifier options
                    if mod_choice in ('y'):
                        print ('\n[1] append, [2] insert, [3] sort, [4] reverse')
                        mthd_choice = input('Please select a method:')
                        #'1' allows the user to append in the list
                        if mthd_choice in ('1'):
                            apnd_item = input('Please enter an item to append:')
                            apndfunc()
                            mod_choice = True
                        #'2' allows the user to insert in the list
                        elif mthd_choice in('2'):
                            insr_inx = int (input('\nPlease enter an index position:'))
                            insr_item = str(input('Please enter an item:'))
                            insrfunc()
                            mod_choice = True
                        #'3' allows the user to sort the list alphabetically
                        elif mthd_choice in ('3'):
                            sortfunc()
                            mod_choice = True
                        #'4' allows the user to reverse the list
                        elif mthd_choice in ('4') : 
                            revfunc()
                            mod_choice = True
                        #'0' returns an invalid selection
                        elif mthd_choice == '0':
                            print ('\nYou have entered an invalid selection')
                            mod_choice = True
                        #invalid choice returns the user to the data collector menu
                        else:
                            print('\nYou have entered an invalid choice')
                            choice = True
                    #'n' returns the user to the data collector menu        
                    elif mod_choice in ('n'):
                        mod_choice = False
                        choice = True
                    #invalid input returns the user to the data collector menu
                    else :
                        print ('\nInvalid Input')
                        choice = True
            # 'b' allows the user to use a tuple function  
            elif choice in ('b'):
                tup_item = input("\nPlease enter item/s separated by a comma (,):")
                septup_item = tup_item.split(",")
                typ_tup= tuple(septup_item)
                print ('\nThe tuple you have created is:', typ_tup)
                #loop for this modification
                mod_choice = True
                while mod_choice:
                    mod_choice = input('\nWould you like to further modify the tuple? [y/n]:')
                    #'y' displays a prompt to convert the tuple into a list
                    if mod_choice in ('y'):
                        t_con = (str(input('\nThe tuple should be converted to list before modifying. \nWould you like to convert it into list? [y/n] ')))
                        #'y' displays the available tuple modifier options
                        if t_con == 'y':
                            print ('\n[1] append, [2] insert, [3] sort, [4] reverse')
                            mthd_choice = input('Please select a method:')
                            #'1' allows the user to append in the list
                            if mthd_choice in ('1'):
                                apdtup_item = input('\nPlease enter an item to append:')
                                tup2lst=list(typ_tup)
                                apndfunc_tup()
                                choice = True
                            #'2' allows the user to  insert in the list
                            elif mthd_choice in('2'):
                                #allows the user to indicate the index position
                                tupinsr_inx = int (input('\nPlease enter an index position:'))
                                tupinsr_item = str(input('Please enter an item:'))
                                insrtup2lst=list(typ_tup)
                                insrfunc_tup()
                                choice = True
                            #'3' allows the user to sort the list
                            elif mthd_choice in ('3'):
                                sortup2lst=list(typ_tup)
                                sortfunc_tup()
                                choice = True
                            #'4' allows the user reverse the order of the list
                            elif mthd_choice in ('4'):
                                revtup2lst=list(typ_tup)
                                revfunc_tup()
                                choice= True
                            #invalid choice returns the user to the data collector menu
                            else:
                                print('\nYou have entered an invalid choice')
                                choice = True
                        #'n' returns the user to the data collector menu       
                        elif t_con == 'n':
                            mod_choice = False
                            choice = True
                        #invalid input returns the user to the data collector menu
                        else :
                            print ('\nInvalid Input')
                            choice = True
                    #'n' returns the user to the data collector menu            
                    elif mod_choice in ('n'):
                        mod_choice = False
                        choice = True
                    #invalid input returns the user to the data collector menu    
                    else :
                        print ('\nInvalid Input')
                        choice = True

            #'c' allows the user to use a set function
            elif choice in ('c'):
                set_items = input("\nPlease enter item/s separated by a comma (,):")
                sep_items= set_items.split(",")
                typ_set=set(sep_items)
                print ('\nThe set you have created is:', typ_set)
                #loop for this modification
                mod_choice = True
                while mod_choice:
                    mod_choice = input('\nWould you like to further modify the set? [y/n]:')
                    #'y' displays the avialable options for set modifications
                    if mod_choice in ('y'):
                        print ('[1] add, [2] difference, [3] discard, [4] update')
                        mthd_choice = input('Please select a method:')
                        #'1' allows the user to add item in the set
                        if mthd_choice in ('1'):
                            add_item = input('\nPlease enter an item to add:')
                            addfunc()
                            choice = True
                        #'2' allows the user to use difference function to the set
                        elif mthd_choice in('2'):
                              print (typ_set)
                              diff_items = input('\nPlease enter another set of items:')
                              difsep_items= diff_items.split(",")
                              new_items= set(difsep_items)
                              print('The new set you have created is:', new_items)
                              #loop for difference selection
                              #displays option under the difference function
                              oldnew = True
                              while oldnew:
                                print('\n[1]. Return a set that contains the items that only exist in the old set.')
                                print('[2]. Return a set that contains the items that only exist in the new set.')
                                diff_choice = input('\nPlease select a difference method:')
                                #'1' displays items that only exist in the old set
                                if diff_choice in ('1'):
                                    dif1_chc=0
                                    dif1func()
                                    choice = True
                                    oldnew = False
                                #'2' displays items that only exist in the new set
                                elif diff_choice in ('2'):
                                    dif2_chc = 0
                                    dif2func()
                                    choice = True
                                    oldnew = False
                                #invalid input, allows the user to choose again from the options     
                                else:
                                    print ('Invalid Input, please select [1/2]')
                                    choice = False
                                    oldnew = True
                        #'3' allows the user to use discard function to the set        
                        elif mthd_choice in ('3'):
                            disc_item = input('\nPlease enter an item to discard:')
                            discfunc()
                            choice = True
                            #displays a prompt that the item is not present in the set
                            if disc_item not in typ_set:
                              print ('The entered item is not present in the set')
                            else:
                              pass
                        #allows the user to update the set    
                        elif mthd_choice in ('4'):
                            updt_item = input('\nPlease enter item/s to include in the update,separate it with a comma(,):')
                            updt_item= updt_item.split(",")
                            updtfunc()
                            choice = True
                        #invalid input, displays a prompt that ask user to modify the set
                        else:
                            print('\nYou have entered an invalid choice')
                            choice = True
                    #'n' returns the user to the data collector menu        
                    elif mod_choice in ('n'):
                        mod_choice = False
                        choice = True
                    #invalid input returns the user to the data collector menu
                    else :
                        print ('Invalid Input')
                        choice = True
            #'d' allows the user to use a dictionary
            elif choice in ('d'):
              #loop for the dictionary
              no_item = True
              while no_item:
                try:
                  num_items = int(input('\nPlease enter the number of items you wish to use:'))
                except ValueError:
                  print('\nYou have entered an invalid input')
                  no_item = True
                  continue
                pass         
                main_dct ={}
                print('\nEnter key=value items separated by a space (" ").')
                print('Syntax: key value')
                print('*Sample: "Year 2020"')
                for i in range(num_items):
                    inpitems_dct = input().split()     
                    main_dct[inpitems_dct[0]] = inpitems_dct[1]
                print('\nThe dictionary you created is:', main_dct)
                #loop for this modification
                mod_choice = True
                while mod_choice:
                    mod_choice = input('\nWould you like to further modify the dictionary? [y/n]:')
                    #'y' displays the options for dictionary modification
                    if mod_choice in ('y'):
                        print ('[1] get, [2] items, [3] keys, [4] update')
                        mthd_choice = input('Please select a method:')
                        #'1' allows the user to use the get option 
                        if mthd_choice in ('1'):
                            get_item = input('\nPlease enter a specific key to return its value:')
                            get_mthd = main_dct.get(get_item)
                            print (get_mthd)
                            choice = True
                        #'2' allows the user to use the items option
                        elif mthd_choice in('2'):
                            items_mthd = main_dct.items()
                            print(items_mthd)
                            choice = True
                        #'3' allows the user to use the key option
                        elif mthd_choice in ('3'):
                            keys_mthd = main_dct.keys()
                            print(keys_mthd)
                            choice = True
                        #'4' allows the user to use the update option
                        elif mthd_choice in ('4'):
                            print('''\nPlease enter a key=value item,
separated with a space (" "), in order to update the current dictionary:''')
                            updt_dct = {}
                            updt_item = input().split()
                            updt_dct[updt_item[0]] = updt_item[1]
                            main_dct.update(updt_dct)
                            print(main_dct)
                            mthd_choice in ('4')
                        #invalid input, displays a prompt that ask user to continue modify the dictinary
                        else:
                            print('\nYou have entered an invalid choice')
                            choice = True
                    #'n' returns the user to the data collector menu         
                    elif mod_choice in ('n'):
                        no_item = False
                        mod_choice = False
                        choice = True
                    #invalid input returns the user to the data collector menu
                    else :
                        print ('\nInvalid Input')
                        choice = True
            #'e' allows the user to exit the program
            elif choice in ('e'):
                #loop for this option
                mm = True
                while mm:
                    mm = str(input('Would you like to go back to the main menu? [y/n]'))
                    #'y' returns the user to the main menu
                    if mm =='y':
                        mm = False
                        choice = False
                        main = "yes"
                    #'n' returns the user to the data collector menu
                    elif mm == 'n':
                        mm = False
                        choice = True
                    #invalid input returns the user to the data collector menu
                    else:
                        print('Invalid Input')
                        mm = True
                        choice = False
            #invalid input returns the user to the data collector menu
            else:
                print('\nPlease enter a valid Input')
                choice = True

    #terminates the program
    elif menu == '4':
        #loop asking the user to terminate the program
        term = True
        while term:
            term = str(input('Would you like to terminate the program? [y/n]'))
            #'y' allows the user to terminate the program
            if term == 'y':
                term = False
                print('Thank you for using the program.')
                sys.exit()
            #'n' returns the user to the main menu
            elif term == 'n':
                term = False
                menu = "yes"
            #invalid input returns the user to the main menu
            else:
                print('Invalid Input')
                term = True
                
    #invalid input returns the user to the main menu
    else:
        print('\nInvalid Input')
        menu = "yes"
            


