import unittest


class HotelService:
    def __init__(self):
        self.hotels = {}

    def add_hotel(self, hotel_id, name):
        """Create a hotel with given ID.

        Throws an exception when a hotel with that ID already exists."""

    def set_room(self, hotel_id, number, room_type):
        """Insert or update a room with given number and type.

        Throws an exception if the hotel does not exist."""

    def get_rooms(self, hotel_id):
        """Get all information for a hotel with the given ID."""


class CompanyService:
    def add_employee(self, company_id, employee_id):
        """Create an employee.

        Throws an exception when an employee with that ID already exists."""

    def delete_employee(self, employee_id):
        """Delete an employee, along with their bookings and policies."""


class BookingPolicyService:
    def set_company_policy(self, company_id, room_types):
        """Indicate which types of rooms may be booked by given company."""

    def set_employee_policy(self, employee_id, room_types):
        """Indicate which types of rooms may be booked by a specific employee.

        Has higher precedence than company policies."""

    def is_booking_allowed(self, employee_id, room_type) -> bool:
        """Return whether given employee is allowed to book a room of given type."""
        
        #Context for later: employee policy checked first, then company policy
        #No policy -> allowed
        return True


class BookingService:
    def book(self, employee_id, hotel_id, room_type, check_in_date, check_out_date):
        """Book a room at a hotel."""

        #Context for later: check_out_date >= check_in_date, hotel must exist and room type must be valid,
        #booking must conform to booking policies
        #room bookings must be sensible, with no overlaps in dates
        #Function returns a booking confirmation or raises an error


class HotelServiceTests(unittest.TestCase):
    def test_valid_booking(self):
        hs = HotelService()
        hs.add_hotel(1, "First Hotel")
        hs.set_room(1, 1, "Single")

        cs = CompanyService()
        cs.add_employee(1, 1)

        bps = BookingPolicyService()
        bps.set_employee_policy(1, ["Single"])

        bs = BookingService()
        booking = bs.book(1, 1, "Single", "20/01/2003", "22/01/2003")
        self.assertEqual(booking, {
                "id": 1,
                "hotel_id": 1,
                "employee_id": 1,
                "room_type": "Single",
                "check_in": "20/01/2003",
                "check_out": "22/01/2003",
            })
        


if __name__=="__main__":
    unittest.main()

