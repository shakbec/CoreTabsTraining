class ATM:

    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name
        self.withdrawls = []

    def withdraw(self, request):
        print("Welcome to "+self.bank_name)
        allowed_papers = [100, 50, 10, 5, 1]
        if request > self.balance:
            print("Can't give you all this money !!")

        elif request <= 0:
            print("More than zero plz!")

        else:
            self.balance = self.balance - request
            self.withdrawls.append(request)
            for i in allowed_papers:
                while request >= i:
                    print("Give "+str(i))
                    request-=i

    def show_withdrawls(self):
        for i in self.withdrawls:
            print(i)



atm1 = ATM(500, "Chakib's Bank")
atm2 = ATM(100, "Amal Bank")

atm1.withdraw(152)
atm1.withdraw(15)


atm2.withdraw(20)

atm2.withdraw(150)


atm1.show_withdrawls()
atm2.show_withdrawls()
