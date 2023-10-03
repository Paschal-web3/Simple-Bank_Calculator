import math

# A simple Balance sheet
print(
    "The introduction to this little software source code \n This depict the new offsprings of codez line"
)
balance = 0
while True:
    try:
        num = float(input("Deposit: "))
        break
    except ValueError:
        print("Enter the correct Quantity")
Balance = balance + num

print("Amount Deposited: " + (str(Balance)))
# user wants to withdraw some money
if Balance > 90000:
    print("Alert EFCC")
else:
    print("Thank you for banking with us")

withdraw = int(input("Amount to withdraw: "))
if withdraw > int(Balance):
    print("Insufficient funds")
else:
    print("Transfer Successful")
total = withdraw

Account_Statement = Balance - total  # initial balance
while True:
    if ValueError:
        print("Recheck")
        break
if withdraw > Balance:
    Account_Statement1 = (
        "You dont have: " + str(Account_Statement) + " To Complete this transaction"
    )
    print(Account_Statement1)
print("Thanks for Banking with us ")
