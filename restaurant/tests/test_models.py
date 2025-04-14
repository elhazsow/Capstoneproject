from django.test import TestCase
from restaurant.models import Booking, Menu 
from decimal import Decimal
from datetime import datetime
from datetime import date
from django.utils import timezone



class MenuTest(TestCase):

    def setUp(self):
        # Create a test menu item before each test
        self.menu_item = Menu.objects.create(title="Test Item", price=9.99, inventory=10)
    
    def test_get_item(self):
        menu = Menu.objects.get(title="Test Item")
        # Check if the menu item is created with the correct attributes
        self.assertEqual(menu.title, "Test Item")
        self.assertEqual(menu.inventory, 10)
        self.assertEqual(menu.price, Decimal('9.99'))
        self.assertIsNotNone(menu.created_at)
        # Assuming the __str__ method is implemented in the Menu model
        self.assertEqual(str(menu), "Test Item : 9.99")
        # Check if the menu ID is auto-generated
        self.assertIsNotNone(menu.id)
        # Check if the menu ID is an integer
        self.assertIsInstance(menu.id, int)
        # Check if the menu ID is greater than 0
        self.assertGreater(menu.id, 0)
        # Check if the menu ID is unique
        self.assertEqual(Menu.objects.filter(id = menu.id).count(), 1)
        # Check if the menu ID is not None
        self.assertIsNotNone(menu.id)
        # Check if the menu ID is not empty
        self.assertNotEqual(menu.id, "")
        
   

class BookingTest(TestCase):
    time=timezone.now().time()
    
    def setUp(self):
        # Create a test booking before each test
        self.booking = Booking.objects.create(name="Test Booking", date = date.today(), time = self.time, no_of_guests=6)

    def test_booking_creation(self):
        booking = Booking.objects.get(name="Test Booking")
        # Check if the booking is created with the correct attributes
        self.assertEqual(booking.name, "Test Booking")
        self.assertEqual(booking.date, date.today())
        self.assertEqual(booking.time, self.time)
        self.assertEqual(booking.no_of_guests, 6)
        self.assertIsNotNone(booking.created_at)
        # Assuming the __str__ method is implemented in the Booking model
        self.assertEqual(str(booking), f"Test Booking -- 6 -- {date.today()}")
        # Check if the booking ID is auto-generated
        self.assertIsNotNone(booking.id)
        # Check if the booking ID is an integer
        self.assertIsInstance(booking.id, int)
        # Check if the booking ID is greater than 0
        self.assertGreater(booking.id, 0)
        # Check if the booking ID is unique
        self.assertEqual(Booking.objects.filter(id = booking.id).count(), 1)
        # Check if the booking ID is not None
        self.assertIsNotNone(booking.id)
        # Check if the booking ID is not empty
        self.assertNotEqual(booking.id, "")