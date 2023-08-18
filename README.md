Phone Number Information Lookup

This is a Python script that allows you to retrieve location, service provider, and geographic coordinates information for a given phone number with a country code. The script uses the phonenumbers library to parse and gather information about the phone number, and the opencage.geocoder library to obtain geographic coordinates from location information.

1) Prerequisites
  Before you run the script, make sure you have the following dependencies installed:
	  1.1) phonenumbers
  	1.2) opencage
  	1.3)webbrowser

You can install these dependencies using the following command:
	pip install phonenumbers opencage

2) How to Use

	2.1)Clone this repository to your local machine or download the phone_number_info.py script.
	2.2)Open a terminal or command prompt and navigate to the directory where the script is located.
	2.3)Run the script using the following command:
		python phone_number_info.py
	2.4) You will be prompted to enter a phone number, including the country code (e.g., +1 for the United States).
	2.5) The script will display the following information:
		2.5.1) Location: The location associated with the phone number.
		2.5.2) Service Provider: The service provider associated with the phone number.
		2.5.3) Latitude: The latitude coordinate of the location.
		2.5.4) Longitude: The longitude coordinate of the location.
		2.5.5) Google Map Link: A link to open the location on Google Maps.
	2.6) The Google Map link will automatically open in your default web browser.

3) Important Note

	3.1)The script uses the OpenCageGeocode API to obtain geographic coordinates from location information. Make sure you have an API key from OpenCage and replace the opencage_key variable in the script with your API key.
	3.2)Please be aware that the accuracy of the location information may vary based on the phone number and data availability.

4) License

	4.1)This project is licensed under the MIT License - see the LICENSE file for details.
