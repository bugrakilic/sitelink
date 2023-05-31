# Sitelink
Sitelink is a tool that checks the status of the destination host addresses periodically or manually. It sends a request to the destination host, and receives a response about its status and IP addresses. 

## Requirements: 
requests
socket
csv 
datetime

## Usage: 
- Clone the repository. 
- Install the required dependencies. 
- List your destination host addresses without 'http://' or 'https://' in "destination.txt" file. 
- Run the "sitelink.py" script. 
- The output recorded in "statuslog.csv" file. 

## Additional Notes: 
- A simple UI (aka. status page) can be developed via Flask or Django. So the latest status of the hosts would be shown on the frontend. 
- This script can be used on cloud functions, like AWS Lambda. Likewise it is easier to configure its trigger, either synchronous or asynchronous. 
- If a problem occurs while checking the status, the user can be informed via email notification. 