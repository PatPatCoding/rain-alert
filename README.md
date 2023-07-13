# rain-alert
A program that sends a daily notification when it's going to rain.

The program is scheduled to run every morning at 9am with a use of PythonAnywhere. The weather forecast is checked with openweathermap API. If the weather codes match the rain codes, an email is sent with smtplib.
