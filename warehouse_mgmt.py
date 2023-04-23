from abc import ABC, abstractmethod
from datetime import date
class Address:
    def __init__(self, country: str, city: str, postalcode: int, street: str, number: int):
        self.country = country
        self.city = city
        self.postalcode = postalcode
        self.street = street
        self.number = number
    def get_country(self):
        return self.country
    def get_city(self):
        return self.city
    def get_postalcode(self):
        return self.postalcode
    def get_street(self):
        return self.street
    def get_number(self):
        return self.number
    def get_full_address(self):
        return f"{self.street} {self.number}, {self.postalcode} {self.city}, {self.country}"
class ContactDetails:
    def __init__(self, first_name: str, last_name: str, email: str, phone_number: str):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_email(self):
        return self.email
    def get_phone_number(self):
        return self.phone_number
class Customer(ABC):
    @abstractmethod
    def get_contact_details(self):
        pass
    @abstractmethod
    def get_address(self):
        pass
    @abstractmethod
    def get_orders(self):
        pass
class Order(ABC):
    def __init__(self, date: date):
        self.date = date
    @abstractmethod
    def cancel(self):
        pass
    @abstractmethod
    def process(self):
        pass
    @abstractmethod
    def dispatch(self):
        pass
    @abstractmethod
    def calculate_total(self):
        pass
    @abstractmethod
    def calculate_total_weight(self):
        pass
class OrderDetail:
    def __init__(self, quantity: int):
        self.quantity = quantity
    @abstractmethod
    def calculate_subtotal(self):
        pass
    @abstractmethod
    def calculate_weight(self):
        pass
class Item:
    def __init__(self, price: float, weight: float, description: str):
        self.price = price
        self.weight = weight
        self.description = description
    @abstractmethod
    def get_price_for_quantity(self, quantity: int):
        pass
    @abstractmethod
    def in_stock(self):
        pass
class Payment(ABC):
    def __init__(self, amount: float):
        self.amount = amount
    @abstractmethod
    def authorized(self):
        pass

class Cash(Payment):
    def __init__(self, amount: float, cash_tendered: float):
        super().__init__(amount)
        self.cash_tendered = cash_tendered
    @abstractmethod
    def tender_cash(self):
        pass
    @abstractmethod
    def return_change(self):
        pass
class BankTransfer(Payment):
    def __init__(self, amount: float, recipient_name: str, IBAN: str, BIC: str):
        super().__init__(amount)
        self.recipient_name = recipient_name
        self.IBAN = IBAN
        self.BIC = BIC
    @abstractmethod
    def authorized(self):
        pass
class CreditCard(Payment):
    def __init__(self, amount: float, number: str, cardholder_name: str, expiration_date: date, type: str):
        super().init(amount)
        self.number = number
        self.cardholder_name = cardholder_name
        self.expiration_date = expiration_date
        self.type = type
def authorized(self):
    # Implement authorization logic here
    return True