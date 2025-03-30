"""
Booking Class
This module contains the definition of the Booking class 
"""

from servicerequest import ServiceRequest


class Booking:
    """
    Represents a Booking made by a guest.
    """

    def __init__(self, booking_id: int, check_in_date: str, check_out_date: str, guest, rooms: list, status: str = "Confirmed"):
        """
        Initializes a Booking object.

        : booking_id: Unique ID of the booking
        : check_in_date: Check-in date
        : check_out_date: Check-out date
        : guest: Guest who made the booking
        : rooms: List of rooms booked
        : status: Status of the booking (default is 'Confirmed')
        """
        self._booking_id = booking_id
        self._check_in_date = check_in_date
        self._check_out_date = check_out_date
        self._status = status
        self._guest = guest
        self._rooms = rooms
        self._service_requests = []
        self._invoice = None  # Will be assigned later

    # Getters and Setters
    def get_booking_id(self) -> int:
        return self._booking_id

    def get_check_in_date(self) -> str:
        return self._check_in_date

    def get_check_out_date(self) -> str:
        return self._check_out_date

    def get_status(self) -> str:
        return self._status

    def set_status(self, status: str):
        self._status = status

    def get_guest(self):
        return self._guest

    def get_rooms(self) -> list:
        return self._rooms

    def get_service_requests(self) -> list:
        return self._service_requests

    def get_invoice(self):
        return self._invoice

    # Functional methods
    def add_service_request(self, request: ServiceRequest):
        self._service_requests.append(request)

    def generate_invoice(self, invoice):
        """
        Assigns an invoice to this booking.
        """
        self._invoice = invoice

    def cancel_booking(self):
        """
        Cancels the booking.
        """
        self._status = "Cancelled"
        for room in self._rooms:
            room.set_availability(True)

    def __str__(self):
        """
        String representation of Booking.
        """
        room_numbers = [room.get_room_number() for room in self._rooms]
        return f"Booking ID: {self._booking_id}, Guest: {self._guest.get_name()}, Rooms: {room_numbers}, Status: {self._status}"
