from abc import ABC, abstractmethod

class BankAccount():
    bankName = "Mandlik Bank of Pune"

    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder
        self.__balance = balance

    class BankAccountAbstraction(ABC):
        @abstractmethod
        def deposit(self, amount):
            pass

    def withdraw(self, amount):
        pass

    def get_balance(self):
        pass

    @classmethod
    def bank_name(cls):
        return cls.bankName

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount can't be negative")
        self.__balance += amount
        print(f"{amount} is deposited in {self.__account_holder}'s account and current balance is {self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount to be withdrawn must be more than 0")
        self.__balance -= amount
        print(f"{amount} is withdrawn and balance is {self.__balance}")

    def get_balance(self):
        return self.__balance


# Inheritance
class SavingAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.__interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.get_balance() * (self.__interest_rate / 100)
        print(f"Interest is {interest}")


# Multi-level inheritance
class PremiumSavingAccount(SavingAccount):
    def __init__(self, account_holder, balance, interest_rate, premium_services):
        super().__init__(account_holder, balance, interest_rate)
        self.premium_services = premium_services

    def show_premium_services(self):
        print(f"The premium services available are {self.premium_services}")


# polymorphism : Method overriding in saving account
class AccountHolder:
    def __init__(self, name):
        self.name = name

    def show_account_details(self, account):
        print(f"Account holder: {self.name}")
        print(f"Account balance: {account.get_balance()}")

    def perform_deposit(self, account, amount):
        account.deposit(amount)

    def perform_withdrawn(self, account, amount):
        account.withdraw(amount)


# Main loop to demonstrate OOP concepts
while True:
    print("*" * 20)
    print("OOPs concept in bank management system")
    print("*" * 20)
    print("1. Inheritance \n2. Encapsulation \n3. Abstraction \n4. Polymorphism \n5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("*" * 20)
        print("Demo Inheritance")
        print("*" * 20)

        while True:
            print(
                "1. Single level Inheritance \n2. Multi-level Inheritance \n3. Multiple Inheritance \n4. Hybrid Inheritance \n5. Exit")
            choice_1 = int(input("Enter inheritance type out of above: "))
            if choice_1 == 1:
                print("*" * 20)
                print("Single Inheritance")
                print("*" * 20)
                sa = SavingAccount("Aparna", 5000, 8)
                sa.deposit(2000)
                sa.calculate_interest()
            elif choice_1 == 2:
                print("*" * 20)
                print("Multi-level Inheritance")
                print("*" * 20)
                psa = PremiumSavingAccount("Aparna", 4000, 5, "Free ATM withdrawls")
                psa.deposit(500)
                psa.show_premium_services()
                psa.calculate_interest()
            elif choice_1 == 3:
                print("*" * 20)
                print("Multiple Inheritance")
                print("*" * 20)


                # Multiple inheritance can be demonstrated by combining more than one parent class
                class CreditAccount:
                    def __init__(self, credit_limit):
                        self.credit_limit = credit_limit


                class BusinessAccount(BankAccount, CreditAccount):
                    def __init__(self, account_holder, balance, credit_limit):
                        BankAccount.__init__(self, account_holder, balance)
                        CreditAccount.__init__(self, credit_limit)


                business_acc = BusinessAccount("Mandlik co.", 4000, 50000)
                business_acc.deposit(30000)

                print(f"Credit limit: {business_acc.credit_limit}")

            elif choice_1 == 4:
                print("*" * 20)
                print("Hybrid Inheritance")
                print("*" * 20)


                # Hybrid Inheritance: combining multiple inheritance hierarchies
                class LoanAccount(BankAccount):
                    def __init__(self, account_holder, balance, loan_amount):
                        super().__init__(account_holder, balance)
                        self.loan_amount = loan_amount


                class BusinessLoanAccount(BusinessAccount, LoanAccount):
                    def __init__(self, account_holder, balance, credit_amount, loan_amount):
                        BusinessAccount.__init__(self, account_holder, balance, credit_amount)
                        LoanAccount.__init__(self, account_holder, balance, loan_amount)

                loan_acc = LoanAccount("Techno corp", 40000, 500000)
                print(f"loan amount is: {loan_acc.loan_amount}")

            elif choice_1 == 5:
                exit(1)
            else:
                print("Enter valid choice")

    elif choice == 2:
        print("*" * 20)
        print("Demo Encapsulation")
        print("*" * 20)
        ba = BankAccount("Aparna", 2000)
        ba.deposit(3000)
        ba.withdraw(1000)
        print(f"Balance after amount withdrawn {ba.get_balance()}")

    elif choice == 3:
        print("*" * 20)
        print("Demo Abstraction")
        print("*" * 20)
        #We can't instantiate abstract class directly; it's meant to be subclassed
        #Uncomment below line to show error
        # bank_account_abstract = BankAccountAbstraction() #Error: Can't instantiate abstract class

    elif choice == 4:
        print("*" * 20)
        print("Demo Polymorphism")
        print("*" * 20)
        acc_holder = AccountHolder("Aparna")
        saving_acc = SavingAccount("Aparna", 2000)

        acc_holder.show_account_details(saving_acc)
        acc_holder.perform_deposit(saving_acc,1000)
        acc_holder.perform_withdrawn(saving_acc,300)

    elif choice == 5:
        exit(1)
    else:
        print("Enter valid choice")





