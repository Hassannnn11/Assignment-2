from test_cases import *

"""
Main function to run test cases with menu options and user input.
"""
def main():
    print("==== Royal Stay Hotel Test System ====")
    hotel = create_hotel_with_rooms()

    while True:
        print("\nMenu:")
        print("1. Create Guest Account")
        print("2. Search Available Rooms")
        print("3. Make a Booking")
        print("4. Add Invoice to Booking")
        print("5. Add Service Request")
        print("6. Leave Feedback")
        print("7. Cancel Booking")
        print("8. View Guest Reservation History")
        print("9. Exit")

        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                 # Create Guest Account
                guest = create_guest(hotel)
                
            elif choice == 2:
                # Search Available Rooms
                search_available_rooms(hotel)
                
            elif choice == 3:
                # Make Booking
                guest_id = int(input("Enter Guest ID to Book for: "))
                guest = next((g for g in hotel.get_guests() if g.get_guest_id() == guest_id), None)
                if guest:
                    make_booking(hotel, guest, hotel.get_rooms())
                else:
                    print("Guest not found.")
                    
            elif choice == 4:
                # Add Invoice to Booking
                guest_id = int(input("Enter Guest ID: "))
                guest = next((g for g in hotel.get_guests() if g.get_guest_id() == guest_id), None)
                if guest and guest.get_bookings():
                    booking = guest.get_bookings()[-1]
                    add_invoice_to_booking(booking)
                else:
                    print("Booking not found for guest.")
                    
            elif choice == 5:
                 # Add Service Request
                guest_id = int(input("Enter Guest ID: "))
                guest = next((g for g in hotel.get_guests() if g.get_guest_id() == guest_id), None)
                if guest and guest.get_bookings():
                    booking = guest.get_bookings()[-1]
                    add_service_request(booking)
                else:
                    print("Booking not found for guest.")
                    
            elif choice == 6:
                # Leave Feedback
                guest_id = int(input("Enter Guest ID: "))
                guest = next((g for g in hotel.get_guests() if g.get_guest_id() == guest_id), None)
                if guest:
                    leave_feedback(guest)
                else:
                    print("Guest not found.")
                    
            elif choice == 7:
                # Cancel Booking
                guest_id = int(input("Enter Guest ID: "))
                guest = next((g for g in hotel.get_guests() if g.get_guest_id() == guest_id), None)
                if guest and guest.get_bookings():
                    booking = guest.get_bookings()[-1]
                    cancel_booking(booking)
                else:
                    print("Booking not found.")
                    
            elif choice == 8:
                # View Reservation History
                guest_id = int(input("Enter Guest ID: "))
                guest = next((g for g in hotel.get_guests() if g.get_guest_id() == guest_id), None)
                if guest:
                    print("Reservation History:")
                    for b in guest.get_bookings():
                        print(b)
                else:
                    print("Guest not found.")
                    
            elif choice == 9:
                # Exit Program
                print("Exiting system.")
                break
            else:
                print("Invalid option. Please choose between 1-9.")
        except Exception as e:
            print("Input error:", e)


if __name__ == "__main__":
    main()
