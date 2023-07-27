# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 11:37:21 2023

@author: SemanurSancar
"""

import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        # Create a test client using the Flask app
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page_get(self):
        # Test GET request for the home page
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

        # Check if certain elements are present in the HTML response
        self.assertIn(b'Latitude:', response.data)
        self.assertIn(b'Longitude:', response.data)
        self.assertIn(b'Installed Power [kW]:', response.data)
        self.assertIn(b'Get Average Generation', response.data)

    def test_home_page_post_invalid_latitude_input(self):
        # Test POST request with invalid latitude input value
        response = self.app.post('/', data={'num1': '100', 'num2': '38', 'num3': '5'})
        self.assertEqual(response.status_code, 200)
        error_message = 'Geçersiz koordinat girişi.'.encode('utf-8')  # Convert the string to bytes-like object
        self.assertIn(error_message, response.data)

    def test_home_page_post_invalid_longitude_input(self):
        # Test POST request with invalid longitude input value
        response = self.app.post('/', data={'num1': '40', 'num2': '200', 'num3': '5'})
        self.assertEqual(response.status_code, 200)
        error_message = 'Geçersiz koordinat girişi.'.encode('utf-8')  # Convert the string to bytes-like object
        self.assertIn(error_message, response.data)

    def test_home_page_post_invalid_peak_power_input(self):
        # Test POST request with invalid peak power input value
        response = self.app.post('/', data={'num1': '40', 'num2': '38', 'num3': '-5'})
        self.assertEqual(response.status_code, 200)
        error_message = 'Geçersiz kurulu güç girişi.'.encode('utf-8')  # Convert the string to bytes-like object
        self.assertIn(error_message, response.data)

    def test_home_page_post_zero_peak_power_input(self):
        # Test POST request with zero peak power input value
        response = self.app.post('/', data={'num1': '40', 'num2': '38', 'num3': '0'})
        self.assertEqual(response.status_code, 200)
        error_message = 'Geçersiz kurulu güç girişi.'.encode('utf-8')  # Convert the string to bytes-like object
        self.assertIn(error_message, response.data)

    def test_home_page_post_valid_input(self):
        # Test POST request with valid input values
        response = self.app.post('/', data={'num1': '37', 'num2': '38', 'num3': '5'})
        self.assertEqual(response.status_code, 200)
        # Assert other expected output based on the input values

    # You can write more test cases for other functionalities

if __name__ == '__main__':
    unittest.main()
