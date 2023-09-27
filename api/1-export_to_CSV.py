#!/bin/bash/python3
"""this module make a return de information API"""

import csv
import requests

def export_file_csv(employee_id):
    """GET date of employe from API"""
    response1 = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(employee_id))
    """convertir response in format json"""
    employee = response1.json()
    """GET date of task about employe_id"""
    response2 = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id))
    """convertir reponse in format json"""
    todos = response2.json()
    """open our create a csv file with the name USER_ID.csv"""
    with open(f"{employee_id}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        """write each task to the CSV file"""
        for todo in todos:
            writer.writerow([employee_id, employee['username'], todo['completed'], todo['title']])

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        export_file_csv(int(sys.argv[1]))
