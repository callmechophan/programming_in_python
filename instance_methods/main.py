class payslip:
    def __init__(self, name, payment = False, amount = 0):
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = True

    def status(self):
        if self.payment == True:
            return self.name + " is paid " + str(self.amount) + "."
        else:
            return self.name + " is not paid."

nathan = payslip("Nathan", False, 1000)
nathan.pay()
print(nathan.status())

roger = payslip("Roger", False, 3000)
print(roger.status())