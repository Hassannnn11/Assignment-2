"""
Test Cases for Royal Stay Hotel Management System
This file tests all features of the system with user inputs and exception handling.
"""


from guest import Guest
from room import Room
from hotel import Hotel
from booking import Booking
from feedback import Feedback
from servicerequest import ServiceRequest
from invoice import Invoice


"""
Creates a hotel object and adds sample rooms.
"""
def create_hotel_with_rooms():
    hotel = Hotel("Royal Stay", "Dubai Marina", "+971500000000")
    hotel.add_room(Room(101, "Single", ["WiFi", "TV"], 300.0))
    hotel.add_room(Room(102, "Double", ["WiFi", "Mini-Bar"], 500.0))
    hotel.add_room(Room(103, "Suite", ["WiFi", "Jacuzzi", "TV"], 800.0))
    return hotel


"""
Creates a guest account by taking user input.
Handles exceptions if input is invalid.
"""
def create_guest(hotel):
    try:
        guest_id = int(input("Enter Guest ID: "))
        name = input("Enter Name: ")
        contact = input("Enter Contact Info: ")
        email = input("Enter Email: ")
        points = int(input("Enter Loyalty Points: "))
        status = input("Enter Membership Status: ")
        
        # Create and add guest
        guest = Guest(guest_id, name, contact, email, points, status)
        hotel.add_guest(guest)
        print("Guest created successfully:\n", guest)
        return guest
    except Exception as e:
        print("Error creating guest:", e)
        return None


"""
Searches for available rooms based on user input criteria.
Handles invalid inputs.
"""
def search_available_rooms(hotel):
    try:
        room_type = input("Enter Room Type to Search (or leave blank): ").strip()
        amenities_input = input("Enter Required Amenities (comma-separated or leave blank): ").strip()
        amenities = [a.strip() for a in amenities_input.split(",")] if amenities_input else []
        
        # Search rooms
        rooms = hotel.search_available_rooms(room_type if room_type else None, amenities)
        print("Available Rooms:")
        for r in rooms:
            print(r)
        return rooms
    except Exception as e:
        print("Error searching rooms:", e)
        return []


"""
Creates a room booking for a guest.
Handles invalid input and availability status.
"""
def make_booking(hotel, guest, rooms):
    try:
        booking_id = int(input("Enter Booking ID: "))
        check_in = input("Enter Check-in Date (YYYY-MM-DD): ")
        check_out = input("Enter Check-out Date (YYYY-MM-DD): ")
        room_numbers = input("Enter Room Numbers to Book (comma-separated): ")
        room_list = []
        
        # Verify selected rooms
        for r in hotel.get_rooms():
            if str(r.get_room_number()) in room_numbers.split(",") and r.get_availability():
                r.set_availability(False)
                room_list.append(r)

        if not room_list:
            print("No valid or available rooms selected.")
            return None
        
        # Create booking
        booking = Booking(booking_id, check_in, check_out, guest, room_list)
        guest.add_booking(booking)
        print("Booking created successfully:\n", booking)
        return booking
    except Exception as e:
        print("Error during booking:", e)
        return None


"""
Generates and adds an invoice to a booking.
"""
def add_invoice_to_booking(booking):
    try:
        invoice_id = int(input("Enter Invoice ID: "))
        amount = float(input("Enter Amount: "))
        method = input("Enter Payment Method: ")
        discount = float(input("Enter Discount Applied (0 if none): "))
        invoice = Invoice(invoice_id, amount, method, discount)
        booking.generate_invoice(invoice)
        print("Invoice generated:\n", invoice)
    except Exception as e:
        print("Error generating invoice:", e)



"""
Adds a service request to an existing booking.
"""
def add_service_request(booking):
    try:
        request_id = int(input("Enter Request ID: "))
        service_type = input("Enter Service Type: ")
        request_date = input("Enter Request Date (YYYY-MM-DD): ")
        request = ServiceRequest(request_id, service_type, request_date)
        booking.add_service_request(request)
        print("Service request added:\n", request)
    except Exception as e:
        print("Error adding service request:", e)



"""
Adds feedback for a guest after their stay.
"""
def leave_feedback(guest):
    try:
        feedback_id = int(input("Enter Feedback ID: "))
        rating = int(input("Enter Rating (1-5): "))
        comment = input("Enter Comment: ")
        date = input("Enter Date (YYYY-MM-DD): ")
        feedback = Feedback(feedback_id, rating, comment, date)
        guest.add_feedback(feedback)
        print("Feedback submitted:\n", feedback)
    except Exception as e:
        print("Error submitting feedback:", e)



"""
Cancels an existing booking and updates room availability.
"""
def cancel_booking(booking):
    try:
        confirm = input("Are you sure you want to cancel this booking? (yes/no): ").lower()
        if confirm == "yes":
            booking.cancel_booking()
            print("Booking cancelled.")
            for r in booking.get_rooms():
                print(f"Room {r.get_room_number()} is now {'Available' if r.get_availability() else 'Not Available'}")
        else:
            print("Cancellation aborted.")
    except Exception as e:
        print("Error cancelling booking:", e)

