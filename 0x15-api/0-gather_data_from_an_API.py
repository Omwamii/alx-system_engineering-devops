#!/usr/bin/python3
""""
script that returns info on user completed tasks
"""
import requests
import sys


if __name__ == "__main__":
    usr_id = sys.argv[1]
    todo_url = f'https://jsonplaceholder.typicode.com/todos?userId={usr_id}'
    emp_url = f'https://jsonplaceholder.typicode.com/users?id={usr_id}'
    todos = requests.get(todo_url).json()
    emp_name = requests.get(emp_url).json()[0].get('name')
    completed = list()
    count = total = 0
    for todo in todos:
        if todo['completed']:
            completed.append(todo['title'])
            count += 1
        total += 1
    print(f"Employee {emp_name} is done with tasks({count}/{total}):")
    for task in completed:
        print(f"\t {task}")
