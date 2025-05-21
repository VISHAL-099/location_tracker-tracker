from flask import Flask, request, jsonify

app = Flask(__name__)

# Device ki location store karne ke liye dictionary
locations = {}


@app.route('/update_location', methods=['POST'])
def update_location():
    data = request.get_json()
    device_id = data.get("device_id")
    latitude = data.get("latitude")
    longitude = data.get("longitude")

    locations[device_id] = {
        "latitude": latitude,
        "longitude": longitude
    }
    return jsonify({"message": "Location updated successfully"}), 200


# 📌 Location ko Google Maps link ke sath show karne ke liye
@app.route('/show_location/<device_id>', methods=['GET'])
def show_location(device_id):
    if device_id in locations:
        location = locations[device_id]
        latitude = location['latitude']
        longitude = location['longitude']
        maps_link = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"

        return f"""
        <h2>Device ID: {device_id}</h2>
        <p>Latitude: {latitude}</p>
        <p>Longitude: {longitude}</p>
        <p><a href="{maps_link}" target="_blank">Open in Google Maps</a></p>
        """
    return "Device not found", 404


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
