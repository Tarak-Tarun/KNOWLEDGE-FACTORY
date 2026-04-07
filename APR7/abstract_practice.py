from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class CreditCardPayment(Payment):
    def pay(self):
        print("Payment is Done With Credit Card")
class UPI(Payment):
    def pay(self):
        print("Payment is Done with UPI")
class Crypto(Payment):
    def pay(self):
        print("Payment is Done With Crypto Currency")
credit=CreditCardPayment()
credit.pay()
upi=UPI()
upi.pay()
crypto=Crypto()
crypto.pay()