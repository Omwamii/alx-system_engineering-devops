#!/usr/bin/python3
""""
script that returns info on user completed tasks
"""
import json
import requests
import sys


if __name__ == "__main__":
    usr_id = sys.argv[1]
    todo_url = f'https://jsonplaceholder.typicode.com/todos?userId={usr_id}'
    emp_url = f'https://jsonplaceholder.typicode.com/users?id={usr_id}'
    todos = requests.get(todo_url).json()
    user_name = requests.get(emp_url).json()[0].get('username')
    file_name = f"{usr_id}.json"
    json_data = dict()
    tasks = list()
    for todo in todos:
        task = dict()
        task['task'] = todo['title']
        task['completed'] = todo['completed']
        task['username'] = str(user_name)
        tasks.append(task)
    json_data[usr_id] = tasks

    with open(file_name, 'w') as f:
        json.dump(json_data, f)
