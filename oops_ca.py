import uuid
from datetime import * #import everything from datetime


'''
Customer class is used to assign values to the values for the specified object created of type
cutomer as well as account because account is the child of customer class
'''


#customer class to store customer details
class Customer(object):
    #to initialize the attributes of the customer class
    def __init__(self):
        self.client_details_list = []
        self.loggedin = False
        self.cash = 100
        self.TranferCash = False
        self.funds = 0
        self.account_details = []
        self.transactions = []
        self.minimum = 0
        self.account_dict = {}
        self.tran_bool = False
    #return customer ID and account number is string
    def __str__(self):
        result = "customer ID: " + str(self.account_details[0]) + "\n"

        return result

'''
Class Account

This class is the heart of the program it contains all the main functions like login, register for
a general account, deposit money, transfer money to another account, withdrawal, check current
balance, and lastly print all the transactions made by a cretain account. However, the withdrawal
works a bit different for all three accounts.
'''
#general bank account
class Account(Customer):
    #initialize the attributes of the bank class
    def __init__(self):
        #sttribute from customer class
        Customer.__init__(self)
        self.client_details_list = []
        self.loggedin = False
        self.cash = 100
        self.TranferCash = False
        self.funds = 0
        self.account_details = []
        self.transactions = []
        self.minimum = 0
        self.count = 0
        self.transfer_acc = []
        self.first_withdrawal_date = 0
        self.next_withdrawal_date = 0
        self.checking_minimum = -50
        self.tran_bool = False

    '''
    Login - When a user is asked to login it prompts for account_number and password as all the
    generated account numbers are unique the user need not worry about logging into savings, checking
    or general account. The login then return a list of all the customer details that can be further
    used for respective services
    '''
    def login(self, acc_no, password):

        #check account number and password whether or not this is in the account txt
        with open("account.txt", "r") as file:
            for i in file:
                sentence = i.split(",")
                if sentence[0] == acc_no and sentence[1] == password:
                    #store account detail in account_list
                    self.account_details = sentence
                    self.funds = int(sentence[3])
                    self.loggedin = True
        # check account number and password whether or not this is in the customer txt
        with open("customer.txt", "r") as file:
            for i in file:
                sentence = i.split(",")
                if sentence[0] == acc_no and sentence[1] == password:
                    self.account_details = (self.account_details + sentence)
        #if account number and password is match in account txt
        if self.loggedin:
            print("\nLOGGED IN SUCCESSFULLY!")
            return self.account_details
        else:
            return 0
    '''Registration - The registration function is a general type account
        registration. If the user already has a general account than no need to create another account
        directly login and then choose the wanted service.
    '''
    def register(self, acc_no, firstname, surname, age, phone, IBAN, funds, confirm_password, acc_type):
        self.conditions = 1
        #check phone nuber is match 10
        if len(str(phone)) != 10:
            print(len(str(phone)))
            self.conditions = 0
            print("Invalid Phone number ! please enter 10 digit number including 0")
        #check first name and last name is alpha
        if firstname.isalpha() == False or surname.isalpha() == False:
            self.conditions = 0
            print("Enter first name and surname not alpha")
        #condition is true
        if self.conditions == 1:
            #bank assign IBAN and acccount to user
            print("Your new General account account_number is: ", acc_no)
            print("Your new General account IBAN is:\t\t", IBAN)
            print("\nGeneral account created successfully")
            #store customer detail in customer list
            self.customer_list = [acc_no, confirm_password, firstname, surname, age, phone, acc_type]

            #store customer detail in customer txt
            with open("customer.txt", "a") as f:
                for details in self.customer_list:
                    f.write(str(details) + ",")
                f.write("\n")
            #store account detail in account txt
            self.account_list = []
            self.account_list = [acc_no, confirm_password, IBAN, funds, acc_type]
            with open(f"account.txt", "a") as f:
                for details in self.account_list:
                    f.write(str(details) + ",")
                f.write("\n")

    '''Deposit - The deposit function is a simple addition of amount to the current net balance.
            However, the user cannot deposit zero or less amount in the account '''


    def deposit(self, amount):
        #deposit cash must more than 0
        if amount > 0:
            newamount = self.funds + amount
            #open account.txt read account detail
            with open(f"account.txt", "r") as f:
                details2 = f.read()
                self.account_list = details2.split(",")
            f.close()
            #ater deposit cash in account
            if str(self.funds) in self.account_list:
                with open(f"account.txt", "a") as f:
                    # truncate the file
                    f.truncate(0)
                    #find user funds in account.txt then replace new amount
                    f.write(details2.replace(str(self.funds), str(newamount)))
                    f.write("\n")
                #close file
                f.close()

            #new funds
            self.funds += amount

            # transaction record
            self.transactions = ("deposit", amount)
            with open(f"accountTransaction.txt", "a") as f:
                f.write(str(self.account_details[0]) + "," + str(self.transactions) + "," + str(self.funds) + ",")
                f.write("\n")
            print("{} euro successfully deposited".format(amount))


        #error message
        else:
            print("Enter correct value of amount")
        '''Withdraw - If the account_type is "GENERAL" than the user can
        withdraw only until his/her net balance becomes zero. If the account_type is "SAVINGS" than the
        user can withdraw only once every month. and is it is of type "CHECKING" than the user can withdraw
        as many times as their wish but the net balance cannot be less than 50 euros. '''

    def withdraw(self, amount):
        if amount <= 0:
            print("You can only withdraw a positive value")
            return

        # you can withdraw only a positive amount if it is a general account
        if self.account_details[4] == "GENERAL":
            if self.funds - amount < self.minimum:
                print("Sorry, you can't withdraw that much")

            else:
                self.funds -= amount
                self.transactions = ("withdraw", amount)
                with open(f"accountTransaction.txt", "a") as f:
                    f.write(str(self.account_details[0]) + "," + str(self.transactions) + "," + str(self.funds))
                    f.write("\n")
                print("{} euro successfully witdrawed net balance = {} ".format(amount, self.funds))

        elif self.account_details[4] == "CHECKING":
            if self.funds - amount < self.checking_minimum:
                print("Sorry, you can't withdraw that much")
                return

            self.funds -= amount
            self.transactions = ("withdraw", amount)
            with open(f"accountTransaction.txt", "a") as f:
                f.write(str(self.account_details[0]) + "," + str(self.transactions) + ",")
                f.write("\n")

        # withdrawal from savings account can only be done once every month
        elif self.account_details[4] == "SAVINGS":
            # if this is the first transaction by the user after creating the savings account
            if self.first_withdrawal_date == 0:
                self.first_withdrawal_date = datetime.today()
                self.next_withdrawal_date = self.first_withdrawal_date + timedelta(days=30)
                print("Your next withdrawal date is {} ".format(self.next_withdrawal_date))
                if self.funds - amount < self.minimum:
                    print("Sorry, you can't withdraw that much")
                    return

                self.funds -= amount
                self.transactions = ("withdraw", amount)
                with open(f"accountTransaction.txt", "a") as f:
                    f.write(str(self.account_details[0]) + "," + str(self.transactions) + ",")
                    f.write("\n")

            # if this is the second, third or fourth transaction by the user after creating the savings account and
            # it matches the next withdraw date
            elif self.next_withdrawal_date == datetime.today():
                # transaction
                if self.funds - amount < self.minimum:
                    print("Sorry, you can't withdraw that much")
                    return

                self.funds -= amount
                self.transactions = ("withdraw", amount)
                with open(f"accountTransaction.txt", "a") as f:
                    f.write(str(self.account_details[0]) + "," + str(self.transactions) + ",")
                    f.write("\n")

                self.next_withdrawal_date = self.next_withdrawal_date + timedelta(days=30)

            # if this is the second, third or fourth transaction by the user after creating the savings account and
            # it does not matches the next withdraw date
            else:
                print("Sorry you can withdraw only once per month. \nYour next withdrawal date is {} ".format(
                    self.next_withdrawal_date))

    '''
    Transfer - This function provides the user an opportunity to transfer money between accounts it can
    be two accounts belonging to same person or any other account belonging to third party. To transfer
    money there is no need to know the password of receiving customer.'''

    def Transfer(self, amount, accNo):
        print(accNo)
        self.TransferCash = 0
        self.postion = 0
        self.totalcash = 0
        self.p = 0

        #record s new account detail for receive money account  in account.txt
        with open("account.txt", "r") as file:
            for i in file:
                sentence = i.split(",")
                if str(sentence[0]) == accNo:
                    self.TransferCash = 1
                    with open(f"account.txt", "a") as file:
                        sentence[3] = int(str(sentence[3])) + amount
                        #get a before transaction funds in p
                        self.p = int(str(sentence[3])) - amount
                        #store a new account detail in account.txt
                        file.write(str(sentence[0]) + "," + str(sentence[1]) + "," + str(sentence[2]) + "," + str(sentence[3]) +"," + str(sentence[4]+","))
                        file.write("\n")
                        break

        file.close()

        #remove a old account detail for receive money account in account.txt
        with open(r"account.txt", 'r+') as f:
            # read an store all lines into list
            lines = f.readlines()
            # move file pointer to the beginning of a file
            f.seek(0)
            # truncate the file
            f.truncate()

            # start writing lines
            # iterate line and line number
            for line in lines:
                # delete line number 5 and 8
                # note: list index start from 0
                if str(self.p) not in line:
                    f.write(line)
        f.close()

        #record  a send money account detail in account.txt
        if self.TransferCash == 1:
            left_cash = self.funds - amount
            with open(f"account.txt", "r") as f:
                details2 = f.read()
                self.account_list = details2.split(",")
            f.close()
            if str(self.funds) in self.account_list:
                with open(f"account.txt", "a") as f:
                    # truncate the file
                    f.truncate(0)
                    #replace old balance
                    f.write(details2.replace(str(self.funds), str(left_cash)))
                    f.write("\n")
                f.close()


            #transaction record in accountTransaction.txt
            self.transactions = ("transfer", amount)
            with open(f"accountTransaction.txt", "a") as f:
                f.write(str(acc_no) + str(self.transactions) + "Balance:" + str(left_cash))
                f.write("\n")

            print("Amount Transfered Successfully to", accNo)
            print("Balance left =", left_cash)
            #new account balance
            self.funds = left_cash

    #check account balance
    def balance(self):
        print("\nNET BALANCE = {} | ACCOUNT NUMBER = {} | FIRSTNAME = {} | ACCOUNT TYPE = {} ".format(self.account_details[3], self.account_details[0], self.account_details[8], self.account_details[12]))

    #check transaction record
    def trans(self):
        #open file
        with open(f"accountTransaction.txt", "r") as f:
            for i in f:
                sentence = i.split(",")
                #check account number are match
                if sentence[0] == self.account_details[0]:
                    print("Account number {} {} {} current total is {}".format(sentence[0], sentence[1], sentence[2], sentence[3]))
                    self.tran_bool = True

        if not self.tran_bool:
            print("\nNo transactions made yet\n")


    '''Delete - This function allow user who want to delete an account.'''
    def delete(self, acc_no):


        with open("account.txt", 'r+') as f:
            # read an store all lines into list
            lines = f.readlines()
            # move file pointer to the beginning of a file
            f.seek(0)
            # truncate the file
            f.truncate()

            # start writing lines
            # iterate line
            for line in lines:
                # delete line number
                if acc_no not in line:
                    f.write(line)
        f.close()


        print("Account Delete successful")
'''
Class checkingAccount - child class of Account class

This class checks all the details of the logged in person or the recently created general account
and makes sure that the account being created is for someone 18 or older. Moreover, a person needs
a general to create a checking account. If all the criterias are met then the details are entered
to the account.txt and customer.txt files
'''

class checkingAccount(Account):

    # to initialize the attributes of the customer class
    def __init__(self):
        Account.__init__(self)
        self.client_details_list = []
        self.loggedin = False
        self.cash = 100
        self.TranferCash = False

    '''Registration - The registration function is a checking type account
        registration. '''
    def register(self, acc_no3, firstname, surname, age, phone, IBAN, funds, confirm_password, acc_type):
        self.conditions = 1

        # check phone nuber is match 10
        if len(str(phone)) != 10:
            print(len(str(phone)))
            self.conditions = 0
            print("Invalid Phone number ! please enter 10 digit number")
        #check first name and syrname i=are alpha
        if firstname.isalpha() == False or surname.isalpha() == False:
            self.conditions = 0
            print("Enter first name and surname not alpha")

        #if person open check account,check age is greater equal then 18
        if int(age) <= 18:
            print("You must be 18 to create a checking account")
            self.conditions = 0

       #condition is true
        if self.conditions == 1:
            #bank management system assign an unique account number and IBAN
            print("Your account_number for new checking account is:",acc_no3)
            print("Your IBAN for new checking account is:\t\t", IBAN)
            print("\nChecking account created successfully\n")
            #after successfully create new account,
            self.customer_list = [acc_no3, password, firstname, surname, age, phone, acc_type]

            #store a new customer stail in customer.txt
            with open("customer.txt", "a") as f:
                for details in self.customer_list:
                    f.write(str(details) + ",")
                f.write("\n")

            #store a new account stail in account.txt
            self.account_list = []
            self.account_list = [acc_no3, confirm_password, IBAN, funds, acc_type]
            with open(f"account.txt", "a") as f:
                for details in self.account_list:
                    f.write(str(details) + ",")
                f.write("\n")

'''
Class savingsAccount - child class of Account class

This class checks all the details of the logged in person or the recently created general account
and makes sure that the account being created is for someone 14 or older. Moreover, a person needs
a general to create a savings account. If all the criterias are met then the details are entered
to the account.txt and customer.txt files
'''
class savingsAccount(Account):

    # to initialize the attributes of the customer class
    def __init__(self):
        Account.__init__(self)
        self.client_details_list = []
        self.loggedin = False
        self.cash = 100
        self.TranferCash = False

    '''Registration - The registration function is a saving type account
            registration. '''
    def register(self, acc_no2, firstname, surname, age, phone, IBAN, fund, confirm_password, acc_type):
        conditions = 1
        # only allow user over 14 years to open saving account
        if int(age) < 14:
            print("you cannot open saving account under 14 years")
            conditions = 0

        #condition is ture
        if conditions == 1:
            #bank system assign unique account number and IBAN
            print("Your account_number for new savings account is:", acc_no2)
            print("Your IBAN for new savings account is:\t\t", IBAN)
            print("\nSAVINGS account created successfully\n")
            #store a new customer stail in customer.txt
            self.customer_list = [acc_no2, firstname, surname, age, phone, acc_type]
            with open(f"customer.txt", "a") as f:
                for details in self.customer_list:
                    f.write(str(details) + ",")
                f.write("\n")
            # store a new account stail in customer.txt
            self.accountlist = []
            self.accountlist = [acc_no2, confirm_password, IBAN, fund, acc_type]
            with open(f"account.txt", "a") as f:
                for de in self.accountlist:
                    f.write(str(de) + ",")
                f.write("\n")


#main function for bank service
if __name__ == "__main__":
    repeat = 1

    while repeat != 0:
        # 3 options
        print("\n-------------------------------------------------------------")
        print("Welcome to TUD Bank\nSelect one of the following Services")
        print("-------------------------------------------------------------\n")
        print("1.Login")
        print("2.Create a new Account")
        print("3.Exit")
        user = input("Choose an option: ")
        #log in
        if user == '1':
            acc_no = input("\nEnter Account number:\t")
            password = input("Enter Password:\t")
            obj1 = Account()

            # obj1.login returns a list and that list is stored in funds_ava
            logged_details = obj1.login(acc_no, password)

            if logged_details == 0:
                print("\n\nWrong Account Number or Password \nSorry you cannot use services!")

            while logged_details != 0:

                # print services menu
                print("\n---------SERVICES---------")
                print("1.Deposit")
                print("2.Withdraw")
                print("3.Transfer money")
                print("4.Show Balance amount")
                print("5.Open saving account")
                print("6.Open checking account")
                print("7.Check transaction record")
                print("8.Delete Account")
                print("9. LOGOUT")
                print("----------------------------")
                u = int(input("Choose an option:\t"))
                #deposit
                if u == 1:
                    dep = int(input("How much money would you like to desposit?: "))
                    obj1.deposit(dep)
                #withdraw
                elif u == 2:
                    withdraw = int(input("How much money would you like to withdraw?: "))
                    obj1.withdraw(withdraw)
                #transfer money
                elif u == 3:
                    amount = int(input("How much money would you like to transfer?: "))
                    accNo = input("Enter the account number you want to transfer to")
                    obj1.Transfer(amount, accNo)
                #check balance
                elif u == 4:
                    obj1.balance()
                #create new saving account
                elif u == 5:
                    print("\n---------------------------")
                    print("Creating a Savings Account")
                    print("----------------------------\n")

                    obj2 = savingsAccount()

                    # generate a unique account_number
                    acc_no2 = uuid.uuid4().int >> 128 - (128 - 118)

                    # generate a unique IBAN number
                    IBAN_sav_1 = str(uuid.uuid4())[:8]

                    acc_type = "SAVINGS"
                    choice = input("DO you want to a new password or use the same? \nPlease enter n/s:\t")

                    if choice == "n":
                        # allow the user the use different password to create checking account
                        new_password = input("Enter your password for savings account:\t")
                        confirm_new_password = input("Re-enter the new password:\t")
                        if new_password == confirm_new_password:
                            obj2.register(logged_details[0], logged_details[8], logged_details[9], logged_details[10],
                                          logged_details[11], IBAN_sav_1, logged_details[3], confirm_new_password, acc_type)

                    elif choice == "s":
                        # create checking account using same password
                        obj2.register(logged_details[0], logged_details[8], logged_details[9], logged_details[10],
                                      logged_details[11], IBAN_sav_1, logged_details[3], logged_details[1], acc_type)

                    else:
                        print("Invalid input")
                #create new checking account
                elif u == 6:
                    print("\n---------------------------")
                    print("Creating a Checking Account")
                    print("----------------------------\n")

                    obj2 = checkingAccount()

                    # generate a unique account_number
                    acc_no3 = uuid.uuid4().int >> 128 - (128 - 118)

                    # generate a unique IBAN number
                    IBAN_sav_1 = str(uuid.uuid4())[:8]

                    acc_type = "CHECKING"
                    choice = input("DO you want to a new password or use the same? \nPlease enter n/s:\t")

                    if choice == "n":
                        # allow the user the use different password to create checking account
                        new_password = input("\nEnter your password for checking account: ")
                        confirm_new_password = input("\nRe-enter the new password ")
                        if new_password == confirm_new_password:
                            obj2.register(logged_details[0], logged_details[8], logged_details[9], logged_details[10],
                                          logged_details[11], IBAN_sav_1, logged_details[3], confirm_new_password, acc_type)

                    elif choice == "s":
                        # create checking account using same password
                        obj2.register(logged_details[0], logged_details[8], logged_details[9], logged_details[10],
                                      logged_details[11], IBAN_sav_1, logged_details[3], logged_details[1], acc_type)

                    else:
                        print("Invalid input")
                #check transaction record
                elif u == 7:
                    obj1.trans()

                #delete account
                elif u == 8:
                    confrim= input("confirm to delete account?y/n ")
                    if confrim == 'y':
                        obj1.delete(acc_no)
                        logged_details = 0
                #log out account service
                elif u == 9:
                    print("\nLOGGING OUT")
                    logged_details = 0
        #create new account
        elif user == '2':
            print("Creating new account....")
            # generate a unique IBAN number
            IBAN = str(uuid.uuid4())[:8]
            # generate a unique account_number
            acc_no = uuid.uuid4().int >> 128 - (128 - 118)

            # ask user inputs to enter user details
            print("\n--------------------Required Details------------------------")
            # ask user inputs to enter user details
            firstname = input("\nEnter firstName:\t\t")
            surname = input("Enter surnameName:\t\t")
            age = input("Enter Age:\t\t\t\t")
            phone = input("Enter Phone Number:\t\t")
            funds = int(input("Enter funds:\t\t\t"))
            password = input("Create a  password:\t\t")
            confirm_password = input("Re-enter the password:\t")
            print("------------------------------------------------------------\n")
            acc_type = "GENERAL"
            obj1 = Account()
            if password == confirm_password:
                # create savingsAccount object
                obj1.register(acc_no, firstname, surname, age, phone, IBAN, funds, confirm_password, acc_type)

            else:
                print("Password did not match! :( \nAccount Creation unsuccessful")
        #Exit bank management system
        elif user == '3':
            print("\n-------------------")
            print("Exiting the system")
            print("-------------------\n")
            repeat = 0

        else:
            print("\nPlease enter a valid input")