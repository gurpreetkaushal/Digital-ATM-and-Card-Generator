#Digital ATM Machine & Card Generator
#Gurpreet Kaushal
import random as r
import string as s
name=input("Enter your name for Card Generation: ")

#Card Number
card_num=""
for i in range(16):
    card_num+=str(r.randint(0,9))

#Pin
pin=r.randint(1000,9999)

#Security code
code=''.join(r.choices(s.ascii_uppercase + s.digits,k=6))
card_detail=(card_num,pin,code)

trans=[]
balance=80000
print("1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Transaction History\n5. Card Details\n6. Close")
while 1:
    n=int(input("\nEnter your choice: "))
    print()
    match n:
        case 1:
            print("Total Balance: ",balance)
        case 2:
            amount=int(input("Enter the Deposit Amount:"))
            balance+=amount
            print("Amount succesfully deposit!")
            trans.append(f"Deposit Amount: {amount}")
        case 3:
            amount=int(input("Enter the Withdrawl Amount:"))
            balance-=amount
            print("Amount Successfully Withdrawl!")
            trans.append(f"Withdrawl Amount: {amount}")
        case 4:
            print("Transaction History: ")
            for t in trans:
                print(t)
        case 5:
            print("Card deatails: ")
            print("Card Number : ",card_detail[0])
            print("Pin : ",pin)
            print("Security Code : ",code)
        case 6:
            print("Thank You for the Transaction!")
            break
        case _:
            print("Please enter valid choice")

