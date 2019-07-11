from operator import attrgetter

class AirportStatus:
	def sort_airports(self, airports):
		return sorted(airports, key = attrgetter('name'))

	def get_airports_status(self, airport_codes, service):
		airports = []
		invalid_codes = []
		for code in airport_codes:
			try:
				airports.append(service(code))
			except:
				invalid_codes.append(code)
		return self.sort_airports(airports), invalid_codes


