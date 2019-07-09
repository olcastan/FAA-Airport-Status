import json
from src.Airport import Airport
import requests

class AirportInfoService:
  def get_json(self, airport_code):
      return requests.get("https://soa.smext.faa.gov/asws/api/airport/status/" + airport_code).text
    
  def create_airport(self, json_string):
    if 'Name' not in json_string:
      raise ValueError
    else:
      return Airport(json.loads(json_string)['Name'], json.loads(json_string)['IATA'], json.loads(json_string)['City'], json.loads(json_string)['State'], json.loads(json_string)['Weather']['Temp'], json.loads(json_string)['Delay'])
  
  def fetch_data(self, airport_code):
    try:
      return self.create_airport(self.get_json(airport_code))
    except (requests.ConnectionError,ValueError):
      pass
