"""
Guest Class 
This contains the definition of the Guest class, 
which inherits from Person and includes additional guest-related attributes.
"""

from person import Person
from LoyaltyAccount import LoyaltyAccount

class Guest(Person):
    """
    Represents a Guest in the hotel system.
    """

    def __init__(self, guest_id: int, name: str, contact_info: str, email: str, points: int, membership_status: str):
        """
        Initializes a Guest object.

        : guest_id: Unique ID of the guest
        : name: Name of the guest
        : contact_info: Contact information
        : email: Email address
        : points: Loyalty points
        : membership_status: Loyalty membership status
        """
        super().__init__(name, contact_info)
        self._guest_id = guest_id
        self._email = email
        self._loyalty_account = LoyaltyAccount(points, membership_status)
        self._bookings = []
        self._feedbacks = []

    # Getters and Setters
    def get_guest_id(self) -> int:
        return self._guest_id

    def set_guest_id(self, guest_id: int):
        self._guest_id = guest_id

    def get_email(self) -> str:
        return self._email

    def set_email(self, email: str):
        self._email = email

    def get_loyalty_account(self) -> LoyaltyAccount:
        return self._loyalty_account

    def get_bookings(self) -> list:
        return self._bookings

    def get_feedbacks(self) -> list:
        return self._feedbacks

    # Functional methods
    def add_booking(self, booking):
        self._bookings.append(booking)

    def add_feedback(self, feedback):
        self._feedbacks.append(feedback)

    def get_loyalty_points(self) -> int:
        return self._loyalty_account.get_points()

    def __str__(self):
        """
        String representation of Guest.
        """
        return f"Guest ID: {self._guest_id}, {super().__str__()}, Email: {self._email}, {self._loyalty_account}"
