class Mpesa:
    def __init__(self,account_balance,phone_number):
        self.account_balance=account_balance
        self.phone_number=phone_number
    def send_money(self,amount,receipient):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES is sent to {receipient}.")
        else:
            print(f"Insufficient amount to send {amount}.")
class PersonalMpesa(Mpesa):
    def __init__(self,account_balance,phone_number,idno):
        self.account_balance=account_balance
        self.phone_number=phone_number
        self.idno=idno
    def buyairtime(self,amount):
         self.account_balance >= amount
         self.account_balance -= amount
         print(f"{amount} KES airtime bought successfully")

class BusinessMpesa(Mpesa):
    def __init__(self,account_balance,phone_number,business_name):
        super().__init__(account_balance,phone_number)
        self.business_name=business_name
    def receive_payment(self,amount):
        self.account_balance >= amount
        print(f"{amount} KES received from a customer.")
personal=PersonalMpesa(2000,113088530,22642266)
personal.send_money(3000,7166385238)
personal.buyairtime(150)
