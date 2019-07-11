import unittest

from unittest.mock import *
from src.FAAAirportInfoService import (AirportInfoService, json)

class FAAAirportInfoServiceTest(unittest.TestCase):
  def setUp(self):
    self.valid_json = '{"Name":"George Bush Intercontinental/houston","City":"Houston","State":"TX","ICAO":"KIAH","IATA":"IAH","SupportedAirport":false,"Delay":false,"DelayCount":0,"Status":[{"Reason":"No known delays for this airport"}],"Weather":{"Weather":[{"Temp":["Partly Cloudy"]}],"Visibility":[10.00],"Meta":[{"Credit":"NOAAs National Weather Service","Url":"http://weather.gov/","Updated":"Last Updated on Feb 24 2019, 6:53 am CST"}],"Temp":["49.0 F (9.4 C)"],"Wind":["North at 11.5"]}}'
    self.invalid_json = '"SupportedAirport":false,"Delay":false,"DelayCount":0,"Status":[{"Type":"","AvgDelay":"","ClosureEnd":"","ClosureBegin":"","MinDelay":"","Trend":"","MaxDelay":"","EndTime":""}]}'
    self.airport_info_service = AirportInfoService()

  def test_given_code_return_JSON_from_url(self):
    json_string = self.airport_info_service.get_json('IAH')
    self.assertEqual('"City":"Houston"', json_string[47:63])

  def test_create_airport_from_valid_json(self):
    airport = self.airport_info_service.create_airport(self.valid_json)
    json_temp = json.loads(self.valid_json)

    self.assertEqual('George Bush Intercontinental/houston', airport.name)
    self.assertEqual('IAH', airport.code)
    self.assertEqual('Houston', airport.city)
    self.assertEqual('TX', airport.state)
    self.assertEqual(json_temp['Weather']['Temp'], airport.temp)
    self.assertEqual(json_temp['Delay'], airport.delay)
  
  def test_invalid_json_exception(self):
    with self.assertRaises(ValueError):
      self.airport_info_service.create_airport(self.invalid_json)
      
  @patch('src.FAAAirportInfoService.AirportInfoService.get_json', return_value='{"Name":"George Bush Intercontinental/houston","City":"Houston","State":"TX","ICAO":"KIAH","IATA":"IAH","SupportedAirport":false,"Delay":false,"DelayCount":0,"Status":[{"Reason":"No known delays for this airport"}],"Weather":{"Weather":[{"Temp":["Partly Cloudy"]}],"Visibility":[10.00],"Meta":[{"Credit":"NOAAs National Weather Service","Url":"http://weather.gov/","Updated":"Last Updated on Feb 24 2019, 6:53 am CST"}],"Temp":["49.0 F (9.4 C)"],"Wind":["North at 11.5"]}}')
  def test_fetch_data_calls_get_json(self, mock_get_json):
    assert self.airport_info_service.fetch_data('IAH')
    mock_get_json.assert_called_once_with('IAH')


if __name__ is "__main__":
  unittest.main()


