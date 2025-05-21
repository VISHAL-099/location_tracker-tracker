from flask import Flask, request, jsonify, render_template
import datetime

app = Flask(__name__)

locations = {}  # Store device locations

@app.route('/update_location', methods=['POST', 'GET'])
def update_location():
    if request.method == 'GET':
        return jsonify({"error": "Use POST method to update location"}), 405

    try:
        data = request.get_json()
        device_id = data.get("device_id")
        latitude = data.get("latitude")
        longitude = data.get("longitude")

        if not all([device_id, latitude, longitude]):
            return jsonify({"error": "Missing required fields"}), 400

        locations[device_id] = {
            "latitude": latitude,
            "longitude": longitude,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return jsonify({"message": "Location updated successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/show_location')
def show_location():
    return render_template('map.html', locations=locations)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
