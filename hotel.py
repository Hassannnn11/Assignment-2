
"""
Hotel Class 
This module contains the definition of the Hotel class 
"""

from room import Room
from guest import Guest


class Hotel:
    """
    Represents a Hotel.
    """

    def __init__(self, hotel_name: str, address: str, contact_no: str):
        """
        Initializes a Hotel object.

        : hotel_name: Name of the hotel
        : address: Address of the hotel
        : contact_no: Contact number
        """
        self._hotel_name = hotel_name
        self._address = address
        self._contact_no = contact_no
        self._rooms = []
        self._guests = []

    # Getters and Setters
    def get_hotel_name(self) -> str:
        return self._hotel_name

    def get_address(self) -> str:
        return self._address

    def get_contact_no(self) -> str:
        return self._contact_no

    def get_rooms(self) -> list:
        return self._rooms

    def get_guests(self) -> list:
        return self._guests

    # Functional methods
    def add_room(self, room: Room):
        self._rooms.append(room)

    def add_guest(self, guest: Guest):
        self._guests.append(guest)

    def search_available_rooms(self, room_type: str = None, amenities: list = None) -> list:
        """
        Search for available rooms based on type and amenities.

        : room_type: Optional, room type
        : amenities: Optional, list of amenities
        :return: List of matching available rooms
        """
        available_rooms = []
        for room in self._rooms:
            if room.get_availability():
                if room_type and room.get_type() != room_type:
                    continue
                if amenities:
                    if not all(item in room.get_amenities() for item in amenities):
                        continue
                available_rooms.append(room)
        return available_rooms

    def __str__(self):
        return f"Hotel: {self._hotel_name}, Address: {self._address}, Contact: {self._contact_no}, Rooms: {len(self._rooms)}, Guests: {len(self._guests)}"
