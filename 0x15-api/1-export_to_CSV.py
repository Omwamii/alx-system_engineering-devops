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
    with open(file_name, 'w') as f:
        writer = csv.writer(f)
        for todo in todos:
            completed = todo['completed']
            title = todo['title']
            writer.writerow([f'{str(usr_id)}', f'{str(user_name)}',
                            f'{str(completed)}', f'{str(title)}'])
