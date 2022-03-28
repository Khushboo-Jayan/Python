# Python
When a user uses a bank management system, there are 3 options displayed on screen,
there is log in, create a new account and exit. Users must login first to use the services if the
user doesn't have an account number, please choose option 2 to create a new account. To
create a new bank account, the user must enter his/her first name, surname, age, phone
number, funds, and password then system assign IBAN and account number for the user.
After that, the user can use the bank system to deposit, withdraw, transfer it to other account,
check balance, check transaction record, open saving account, and open checking account.
However, the savings account could be opened by anybody older than 14 but users must
know that if they open a saving account that only allows one withdrawal or one transfer in one
month. If a user opens a checking account that only allows users who are 18 years or older
and this account allows the user to have a maximum - €50 negative balance in a bank account
as credit account. Otherwise, if the user already has a bank account, please choose option
one and login using and password. After that the user can use all the bank services in the
bank system. If the user does not want to use any other service they need to logout of their
current logged in account. As a result, somebody else or the same user can login using
another account number and password. If no further use of the system is noticed than the
entire system can be shut down using the third option in the main i.e, Exit
As the checking and savings account and the child classes of parent class account it
allows us to use the parents class functions using dot operator.

USER MANUAL / DESCRIPTION OF FUNCTIONS

1) Login –
 If a user does already have an account of any type then they can login using the
account_number that they are provided while creation of their account.
 Once the user enters the value it is then passed to the function login in the class Account that
is a general type. Then the class parses through the entire account.txt file that thenchecks the
entered account_number and password and returns the list that matches the credentials.
 This returned value is stored in a list that is later appended with the customer details as well.
In case the user wants to create another account and there is no need to ask the user to enter
all the details again. This retured list from the class then is stored in the logged_details list in
the main and later passed to create_savings account class or create_checking account_class.
 If incorrect username or password is entered than the user is redirected to the menu to
choose the login option and re-enter the values.
 If everything is fine then the user can use the services provided by bank

![image](https://user-images.githubusercontent.com/79542266/160455951-32650ad0-8297-46b8-9481-b2f7a9d1d3ff.png)
![image](https://user-images.githubusercontent.com/79542266/160456020-034a52bb-348f-4ff8-9ceb-17fb85c5ed93.png)

2) Create a new General Account
 If the user already does not have a general account with TUD bank, then they can create a new
one. When the user selects ‘2’ option it enters the elif ‘2’ part. After which the customer is
prompted a bunch of questions that are required while account creation these details are then
stored in variables that are then passed to the register function in account class that is general
type.
 The entered details are then written to a file.
 There is no age limit for general account anybody can have a general account.
 Standardized phone number should be 10 digits.
 The general account has no such limit for the account hence, the user is asked what amount
he/she wants in the account while creating that can start from zero to increasing.
 After this the account details are printed however and the creation is done, however, to use
the services the user needs to login

![image](https://user-images.githubusercontent.com/79542266/160456113-130e38e0-5394-4c3a-8977-e80c3fc1f961.png)

3) Exit
 If no further use of system is to be made than the user can select the third function that
makes the logged_details to 0 and hence making the while loop false and exiting the
system and making the entire system to shut down and program terminates.

![image](https://user-images.githubusercontent.com/79542266/160456228-69a94d16-2821-492e-ac45-a891e31dee86.png)

4) Services once you are logged in / have a valid general account:
a) Deposit :
 The user is promped to enter an amount this amount is stored in a variable that is then
passed to the deposit function in account class. As the details of logged in person are
stored in the list account_details the function first look for the sentence where it matches
the account_number and password then grabs the funds from list updates it and again
writes to the file. However, this was achieved by opening the files twice once to read and
once to write
 Moreover, this deposit made is also written to a third file called accountTransactions.txt
 This function adds the deposited money to the current logged in account and updates
both the accountTransactions.txt and account.txt and after depositing the value it
redirects to the services menu

Before using the deposit service:

![image](https://user-images.githubusercontent.com/79542266/160456299-bcf6297e-3f2f-4fdd-b3e7-2d9b5963e44c.png)
![image](https://user-images.githubusercontent.com/79542266/160456324-1d792cbc-3c02-4fac-b9db-d7f3f7b93baf.png)

After using the deposit service:

![image](https://user-images.githubusercontent.com/79542266/160456414-481270dd-5722-4c24-838e-d0cecb81777b.png)
![image](https://user-images.githubusercontent.com/79542266/160456453-67321db9-4f44-4d46-9749-aba7809e8cdf.png)

![image](https://user-images.githubusercontent.com/79542266/160456503-3a31b6b2-1009-4adf-ae0d-47b317d85cc3.png)

b) Withdraw :
 The user is promped to enter an amount this amount is stored in a variable that is then
passed to the deposit function in account class. As the details of logged in person are
stored in the list account_details the function first look for the sentence where it matches
the account_number and password then grabs the funds from list updates it and again
writes to the file.
 This function subtracts the required money to the current logged in account and updates
both the accountTransactions.txt and account.txt and after depositing the value it
redirects to the services menu. However, it works differently for all three different
accounts.
 General type : The user can withdraw as much as they want as long as it does not make
the net balance less than 0.
 Saving type: allows the user to withdraw money only once every month.
 Checking type: The user can withdraw as much as they want as long as it does not make
the net balance less than -50.

c) Transfer:
 This function allows the user to transfer money between two accounts. Here, the user need
to know the account_number to which they want to sent the money.
 The user is prompted to enter the account_number and how much money they want to
send to the receiver however, there transfer cannot make their new balance less than 0
hence, the if statement at the beginning.
 We read the customer funda from our list account_details[] and update the everything.
Then parse through the file looking for account number matching the current account
number subtract and update from that look for the receiver add and update in that and the
update this transaction to accountTransactions.txt file.
 For example : - Account number 29 Transfer 50 euro to account nunber 18 both of balance
is changed

![image](https://user-images.githubusercontent.com/79542266/160456675-6fdf0459-b081-4aed-9408-bfc877675b4b.png)
![image](https://user-images.githubusercontent.com/79542266/160456744-090372ed-4f47-4444-a63b-078332322a64.png)
![image](https://user-images.githubusercontent.com/79542266/160456804-7a094c18-4051-45ab-887e-51da8a09e51f.png)

d) Balance:
 Simply print the balance available, the account number, customer name and account
type using the account_details list that stores the details of the current object i.e.,
current logged in user.
![image](https://user-images.githubusercontent.com/79542266/160456860-4cce0514-a140-4cf8-a1a4-b09032c42337.png)

e) Open Savings Account:
 User can create as many savings account as they want as long as they have a valid
general account.
 It will prompt if the user is younger than 14

![image](https://user-images.githubusercontent.com/79542266/160456957-2c352db6-ce02-4804-a585-915092b7f2e5.png)

f) Open Checking Account:
![image](https://user-images.githubusercontent.com/79542266/160457026-aada430d-1135-4f64-a3cd-a75c75bd4e88.png)

g) Check Transaction record:
 This is transaction record parses through the accountTransaction.txt file and prints all
the sentences that match the logged in account_number. Prints all the transactions
made by current account.
 If no transactions were made then print prompt “NO transaction made”

![image](https://user-images.githubusercontent.com/79542266/160457090-aa2b5226-0fe8-4364-a6a9-93e4aecaa94b.png)
![image](https://user-images.githubusercontent.com/79542266/160457133-922c0a86-de8d-4fcc-a0a4-ad19d7bc4703.png)

h) Delete Account:
 Parses through a file and then deletes the sentence that match the current account
number. However, before deleting asks the user for confirmation and deleted only if
entered ‘y’
 After the user selects the delete account option. To delete the currently logged in
account then the user is automatically logged out and returned to the menu. If wished
here the user can exit the system.
 For example: Delete account number 200

![image](https://user-images.githubusercontent.com/79542266/160457241-27b5f00e-f6fd-4305-809e-b645e8e2cba7.png)
![image](https://user-images.githubusercontent.com/79542266/160457291-0d99127b-12b2-435b-a8b7-45231104ecc4.png)

i) Logout:
 Choose a log out to log out account service to back main menu
 Makes the logged_details variable value to zero so that it makes the while loop condition false
and it exits the loop.
![image](https://user-images.githubusercontent.com/79542266/160457365-2c28adc9-6733-4f8d-bdc1-9f1aa336ef64.png)

INDIVIDUAL CONTRIBUTIONS
We both contributed to the project equally however, the part where we invested most of our time is
mentioned below.
YUJIAO KAN
My main contribution was the transaction functions like deposit, withdrawal, transfer, and check
transaction record. Moreover, I also updated the account.txt accountTransactions.txt and
customer.txt. For updating the txt file after every change used seek() function. I also added
comments to the file as well as added the docstrings that Khushboo sent. I created the
documentation template whereas khushboo explained the individual functions.
KHUSHBOO JAYAN
My main contribution was creating main, making inheritance between classes, creation and update
and logging out of the account, however, I also added the conditions for the withdrawal once per
month and a certain negative amount for savings and checking type accounts respectively. I created
all the docstrings in a txt file that later yujiao added to the .py file.
OVERALL DIFFICULTIES
In beginning, we had a discussion about what it bank system is best for this project. We did all
class together, after I did withdraw function, deposit function and transaction function and Khushboo
did login function and register function and main function. we all work very hard to try our best for
this project.
To be honest, CA2 is changeling for us but when we done this project, we had learned a lot as this
project aggregation what we learned in this semester. I consider most difficult part is transfer money
to another account, because we need consider that when transfer money to anther account, we need
change both of account balance in account text. how to use account number to find balance then
replace new balance in account txt that is very difficult.
However, the most difficult part of them all was updating the money in txt files after every service
was used. To be honest it took as 2 days and 25 hours to figure out how to update the values in lists
and write in a file.

















