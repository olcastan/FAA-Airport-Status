import sys
from src.FAAAirportInfoService import (AirportInfoService)
from src.airport_status import AirportStatus

class Main:
  FAA_airport_service = AirportInfoService()
  airport_status = AirportStatus()
  def read_file(self):
    return open(sys.argv[1],'r')

  def text_to_list(self):
    return [line.strip() for line in self.read_file().readlines()]

  def create_all_airports(self):
    all_airports = list()
    invalid_codes = list()
    for code in self.text_to_list():
      temp_airport = self.FAA_airport_service.fetch_data(code)
      if temp_airport is not None:
        all_airports.append(temp_airport)
      elif temp_airport is None:
        invalid_codes.append(code)

    return self.airport_status.sort_airports(all_airports) , invalid_codes
  
  def set_delays(self, services):
    for airport in services:
      if airport.delay is True:
        airport.delay = "¤"
      else:
        airport.delay = ""
  
  def print_all_info(self, services, invalid_codes):
    self.set_delays(services)
    print("%-45s %-20s %-10s %-25s %s" % ("Name", "City", "State", "Temp", "Delay?"))
    for airports in services:
      print("%-45s %-20s %-10s %-25s %s" %(airports.name, airports.city, airports.state, airports.temp, airports.delay))

    if len(invalid_codes) > 0:
      print("\nError getting details for:")
      print("-------")
      print(invalid_codes)

if __name__ == "__main__":
  main = Main()
  services, invalid_co = main.create_all_airports()
  main.print_all_info(services,invalid_co)



