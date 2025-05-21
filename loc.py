import requests
import os
import time

SERVER_URL = "https://error4o4.pythonanywhere.com/update_location" 

def get_location():
    location = os.popen("termux-location -p network").read()  # Agar GPS fail ho raha hai toh network pe switch karna
    print("Raw Location Data:", location)  # Debug ke liye print karo
    try:
        return eval(location)  # JSON Parse kar raha hai
    except Exception as e:
        print("Error parsing location:", e)
        return None

def send_location():
    loc = get_location()
    if loc:
        data = {
            "device_id": "my_phone_1",
            "latitude": loc.get("latitude", 0),
            "longitude": loc.get("longitude", 0)
        }
        print("Sending Data:", data)  # Debug ke liye print karo
        try:
            response = requests.post(SERVER_URL, json=data)
            print("Server Response:", response.text)
        except Exception as e:
            print("Error sending request:", e)

while True:
    send_location()
    time.sleep(10)  # Har 10 second me location send karega

