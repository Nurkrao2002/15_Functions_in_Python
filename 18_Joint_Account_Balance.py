""" A joint bank account has 2 users and initially the amount balance is 0. 
user_A credited 500 and user_B credited 600 what will be the account balance.
keep the balance as global variable and try to create different functions for each
user and credit the amounts from each user. Finally, print the total amount.  """

x=(int(input("Enter the Amount to be Credited in USER_A Account:")))
y=(int(input("Enter the Amount to be Credited in USER_B Account:")))

balance=0
balance=x+y

def user_A(x):
    global balance
    balance+=x 

def user_B(y):
    global balance
    balance+=y

print(balance)
