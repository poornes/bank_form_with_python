money = 150300
num = (input("Enter your bank account number: "))
print("Your account is " + num)
if len(num) == 19:
    number = (input("Enter your mobile number linked with bank: "))
    print(number)
    if len(number) == 10:
        name = (input("Enter your Full name: "))
        print(name)
    else:
        print("Your number is not linked with any account ! please check the number and try again!")
        input("Enter correct mobile number: ")
    print("Choose the payment method Withdraw or Credit")
    method = input("Enter your payment method: ")
    if method == 'Withdraw':
        amount = (input("Enter the amount: "))
        print(amount + "$" + " is debited from your account " + num + " Your account balance: $")
        sum = float(money) - float(amount)
        print(sum)
    elif method == 'credit' or 'Credit':
        credit = input("Enter the amount to Credit: ")
        sum1 = float(money) + float(credit)
        print(credit + "$ is credit for your account" + num + " your account balance is $:")
        print(sum1)
else:
    print("Enter correct account number and try again!")
    loop = 1
    while loop < 5:
        print("Bank form")
        money = 150300
        num = (input("Enter your bank account number: "))
        print(len(num))
        if len(num) == 19:
            number = (input("Enter your mobile number linked with bank: "))
            print(number)
            if len(number) == 10:
                name = (input("Enter your Full name: "))
                print(name)
            else:
                print("Your number is not linked with any account ! please check the number and try again!")
                input("")
            print("Choose the payment method Withdraw or Credit")
            method = input("Enter your payment method: ")
            if method == 'Withdraw':
                amount = (input("Enter the amount: "))
                print(amount + "$" + " is debited from your account " + num + " Your account balance: $")
                sum = float(money) - float(amount)
                print(sum)
            elif method == 'credit' or 'Credit':
                credit = input("Enter the amount to Credit: ")
                sum1 = float(money) + float(credit)
                print(credit + "$ is credit for your account" + num + " your account balance is $:")
                print(sum1)