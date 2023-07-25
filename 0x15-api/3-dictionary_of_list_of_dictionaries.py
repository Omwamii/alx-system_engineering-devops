#!/usr/bin/python3
""""
script that returns info on user completed tasks
"""
import json
import requests


if __name__ == "__main__":
    emp_url = 'https://jsonplaceholder.typicode.com/users'
    emp_list = requests.get(emp_url).json()
    file_name = "todo_all_employees.json"
    json_data = dict()
    for employee in emp_list:
        emp_id = employee.get('id')
        do_url = f'https://jsonplaceholder.typicode.com/todos?userId={emp_id}'
        todo_list = requests.get(do_url).json()
        user_tasks = list()
        for todo in todo_list:
            task = dict()
            task['task'] = todo['title']
            task['completed'] = todo['completed']
            task['username'] = str(employee.get('username'))
            user_tasks.append(task)
        print(f"{employee.get('id')}: {user_tasks}")
        json_data[employee.get('id')] = user_tasks

    with open(file_name, 'w') as f:
        json.dump(json_data, f)
