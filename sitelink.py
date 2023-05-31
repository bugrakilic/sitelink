import csv
import requests
import socket
from datetime import datetime 

status_dict = {}

def main():
    now = datetime.now()
    timestamp = now.strftime("%Y/%m/%d-%H:%M")

    # reading destination addresses from file, and sending requests. 
    with open("destinations.txt", "r") as fr:
        for line in fr:
            website = line.strip()
            destIP = socket.gethostbyname(website)
            status = requests.get("https://" + website).status_code
            if status == 200: 
                status_dict["https://" + website + ", " + destIP] = "OK"
                print(f"{website} ({destIP}) link --> OK.")
            else: 
                status_dict["https://" + website + ", " + destIP] = "NOT OK"
                print(f"{website} ({destIP}) link --> NOT OK.")

                            
    # writing the status of the requests. 
    with open("statuslog.csv", "a", newline="") as fw:
        csv_writers = csv.writer(fw)
        for key in status_dict.keys():
            csv_writers.writerow([timestamp, key, status_dict[key]])

if __name__ == "__main__":
    main() 