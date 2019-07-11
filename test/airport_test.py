import unittest
from src.Airport import (Airport)
from src.airport_status import (AirportStatus)

class AirportStatusTest(unittest.TestCase):
	def setUp(self):
		self.airport_status = AirportStatus()
		self.iah = Airport("George Bush Intercontinental/houston", 'IAH',None,None,None,None)
		self.iad = Airport("Dulles Airport", 'IAD',None,None,None,None)
		self.ord = Airport("Chicago Airport", 'ORD',None,None,None,None)

	def test_canary(self):
		self.assertTrue(True)

	def test_sort_list_with_no_airports(self):
		self.assertEqual(self.airport_status.sort_airports([]), [])

	def test_sort_list_with_one_airport(self):
		self.assertEqual(
		  self.airport_status.sort_airports([self.iah]), [self.iah])

	def test_sort_list_with_two_airports_in_non_sorted_order(self):
		self.assertEqual(
		  self.airport_status.sort_airports([self.iah, self.iad]),
		  [self.iad, self.iah])

	def test_sort_list_with_two_airports_appended_in_sorted_order(self):
		self.assertEqual(
		  self.airport_status.sort_airports([self.iah, self.iad]),
		  [self.iad, self.iah])

	def test_sort_list_of_three_airports(self):
		self.assertEqual(
		  self.airport_status.sort_airports([self.iah, self.iad, self.ord]),
		  [self.ord, self.iad, self.iah])

	def test_pass_empty_list_return_empty_name_list(self):
		self.assertEqual(
		self.airport_status.get_airports_status([], None), ([], []))

	def test_pass_list_of_one_airport_code_return_its_respective_name(self):
		service = lambda code: {'IAH': self.iah}[code]

		self.assertEqual(
		self.airport_status.get_airports_status(['IAH'], service), ([self.iah], []))

	def test_pass_list_of_two_airports_code_return_their_respective_names(self):
		service = lambda code: {'IAH': self.iah, 'IAD': self.iad}[code]

		self.assertEqual(
    self.airport_status.get_airports_status(['IAD', 'IAH'], service),
			([self.iad, self.iah],[]))
                         
	def test_pass_list_of_two_airports_code_return_their_respective_names_sorted(self):
		service = lambda code: {'IAH': self.iah, 'IAD': self.iad}[code]

		self.assertEqual(
    self.airport_status.get_airports_status(['IAH', 'IAD'], service),
			([self.iad, self.iah],[]))

	def test_pass_list_of_three_airports_code_return_their_respective_names_sorted(self):
		service = lambda code: {'IAH': self.iah, 'IAD': self.iad, 'ORD': self.ord}[code]

		self.assertEqual(
			([self.ord, self.iad, self.iah],[]),
    self.airport_status.get_airports_status(['IAH', 'IAD','ORD'], service))

	def test_one_airport_code_is_invalid(self):
		service = lambda code: {'IAH': self.iah, 'IAD': self.iad, 'ORD': self.ord}[code]

		self.assertEqual(self.airport_status.get_airports_status(['IA'],service),
		([], ['IA']))

	def test_two_airport_codes_are_given_second_invalid(self):
		service = lambda code: {'IAH': self.iah, 'IAD': self.iad, 'ORD': self.ord}[code]

		self.assertEqual(self.airport_status.get_airports_status(['IAH','OR'], service), ([self.iah],['OR']))

	def test_three_airport_codes_are_given_second_invalid(self):
		service = lambda code: {'IAH': self.iah, 'IAD': self.iad, 'ORD': self.ord}[code]

		self.assertEqual(self.airport_status.get_airports_status(['IAH', 'OR', 'IAD'], service), ([self.iad,self.iah],['OR']))

	def test_three_airport_codes_are_given_first_invalid_third_network_error(self):
		service = lambda code: {'IAH': self.iah, 'IAD': self.iad, 'ORD': self.ord}[code]

		self.assertEqual(([self.ord],['IA','']), self.airport_status.get_airports_status(['IA', 'ORD', ''], service))


if __name__ == '__main__':
	unittest.main()
