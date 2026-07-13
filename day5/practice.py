balance = 50000000000
amount = int(input("Enter the amount to withdraw: "))
if amount <=balance and amount%100==0:
    balance -= amount
    print("Money is withdrawn successfully")
else:
    print("Insufficient balance or invalid amount. Please enter a valid amount in multiples of 100.")