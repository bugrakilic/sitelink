from flask import Flask, render_template, request, jsonify
import requests
import threading
import time
import csv

app = Flask(__name__)

website_data = {
    "name": "", 
    "status": "Unknown", 
    "check_period": 10,
}

csv_file = 'results.csv'

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Timestamp', 'Website Name', 'Status'])

def check_website_status():
    while True:
        try:
            response = requests.get(f"https://{website_data['name']}")
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
            if response.status_code == 200:
                website_data['status'] = 'Healthy'
            else:
                website_data['status'] = 'Unhealthy'

            # Log the result to the CSV file
            with open(csv_file, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([timestamp, website_data['name'], website_data['status']])
        except requests.exceptions.RequestException as e:
            website_data['status'] = 'Unhealthy'
            print(f"Error: {e}")

        time.sleep(website_data['check_period'])

@app.route('/')
def index():
    return render_template('index.html', website_data=website_data)

@app.route('/update_status', methods=['POST'])
def update_status():
    website_name = request.form.get('website_name')
    check_period = int(request.form.get('check_period'))

    website_data['name'] = website_name
    website_data['check_period'] = check_period

    return jsonify({'status': website_data['status']})

if __name__ == '__main__':
    status_thread = threading.Thread(target=check_website_status)
    status_thread.daemon = True
    status_thread.start()
    app.run(host="127.0.0.1", port=3333, debug=True)