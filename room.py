"""
Room Class Module
This module contains the definition of the Room class 
"""


class Room:
    """
    Represents a Room in the hotel.
    """

    def __init__(self, room_number: int, room_type: str, amenities: list, price_per_night: float, availability_status: bool = True):
        """
        Initializes a Room object.

        : room_number: Unique room number
        : room_type: Type of room (Single, Double, Suite, etc.)
        : amenities: List of amenities
        : price_per_night: Price per night
        : availability_status: Availability status (default is True)
        """
        self._room_number = room_number
        self._type = room_type
        self._amenities = amenities
        self._price_per_night = price_per_night
        self._availability_status = availability_status

    # Getters and Setters
    def get_room_number(self) -> int:
        return self._room_number

    def get_type(self) -> str:
        return self._type

    def get_amenities(self) -> list:
        return self._amenities

    def get_price_per_night(self) -> float:
        return self._price_per_night

    def get_availability(self) -> bool:
        return self._availability_status

    def set_availability(self, status: bool):
        self._availability_status = status

    def __str__(self):
        """
        String representation of Room.
        """
        availability = "Available" if self._availability_status else "Not Available"
        return f"Room No: {self._room_number}, Type: {self._type}, Price: {self._price_per_night}, Status: {availability}"
