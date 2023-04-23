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
