"""
This module contains the definition of the Person class, 
which is a base class for all persons related to the hotel system.
"""

class Person:
    """
    Represents a Person with basic information.
    """
    def __init__(self, name: str, contact_info: str):
        self._name = name
        self._contact_info = contact_info

    # Getter and Setter for name
    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str):
        self._name = name

    # Getter and Setter for contact_info
    def get_contact_info(self) -> str:
        return self._contact_info

    def set_contact_info(self, contact_info: str):
        self._contact_info = contact_info

    def __str__(self):
        """
        String representation of Person.
        """
        return f"Name: {self._name}, Contact Info: {self._contact_info}"
