import requests
import time

SERVER_URL = "https://error4o4.pythonanywhere.com/update_location"

def get_location():
    try:
        # Using free IP geolocation API
        response = requests.get("http://ip-api.com/json/")
        data = response.json()
        if data['status'] == 'success':
            return {
                "latitude": data.get("lat", 0),
                "longitude": data.get("lon", 0)
            }
        else:
            print("Failed to get location:", data.get("message", "Unknown error"))
            return None
    except Exception as e:
        print("Error fetching location:", e)
        return None

def send_location():
    loc = get_location()
    if loc:
        data = {
            "device_id": "my_windows_pc",
            "latitude": loc["latitude"],
            "longitude": loc["longitude"]
        }
        print("Sending Data:", data)
        try:
            response = requests.post(SERVER_URL, json=data)
            print("Server Response:", response.text)
        except Exception as e:
            print("Error sending request:", e)

if __name__ == "__main__":
    while True:
        send_location()
        time.sleep(10)
