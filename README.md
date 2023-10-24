# Sitelink
Sitelink is a simple tool that checks the status of the host address periodically. It sends a request to the destination host, and receives a response about its status. 

## Requirements: 
- Flask 
- Python libs incl. requests, socket, csv, time, threading 

## Usage: 
1. Clone the repository. 
2. Install the required dependencies mentioned above. 
3. List your destination host addresses without 'http://' or 'https://' in Host field.  
4. Run the app.py. 
5. The output will be recorded in "results.csv" file. 

*This is a hobby project and does not represent any professional intends.*