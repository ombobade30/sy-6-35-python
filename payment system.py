from abc import ABC, abstractmethod


class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(PaymentStrategy):
    def pay(self, amount):
        pin = input("Enter UPI PIN: ")
        print(f"UPI PIN Verified.")
        print(f"Payment of ₹{amount} successful using UPI.")


class Card(PaymentStrategy):
    def pay(self, amount):
        pin = input("Enter Card PIN: ")
        print("Card PIN Verified.")
        print(f"Payment of ₹{amount} successful using Debit/Credit Card.")


class Cash(PaymentStrategy):
    def pay(self, amount):
        print(f"Payment of ₹{amount} received in Cash.")



class PaymentProcessor:

    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def make_payment(self, amount):
        self.strategy.pay(amount)



print("===== Payment Processing System =====")
print("1. UPI")
print("2. Card")
print("3. Cash")

choice = int(input("Enter your choice: "))
amount = float(input("Enter payment amount: "))

if choice == 1:
    payment_method = UPI()
elif choice == 2:
    payment_method = Card()
elif choice == 3:
    payment_method = Cash()
else:
    print("Invalid Choice!")
    exit()

processor = PaymentProcessor(payment_method)
processor.make_payment(amount)