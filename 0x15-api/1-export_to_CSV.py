#!/usr/bin/python3
""""
script that returns info on user completed tasks
"""
import csv
import requests
import sys


if __name__ == "__main__":
    usr_id = sys.argv[1]
    todo_url = f'https://jsonplaceholder.typicode.com/todos?userId={usr_id}'
    emp_url = f'https://jsonplaceholder.typicode.com/users?id={usr_id}'
    todos = requests.get(todo_url).json()
    user_name = requests.get(emp_url).json()[0].get('username')
    file_name = f"{usr_id}.csv"
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todos:
            completed = str(todo['completed'])
            title = str(todo['title'])
            u_id = str(usr_id)
            u_name = str(user_name)
            writer.writerow([u_id, u_name, completed, title])
