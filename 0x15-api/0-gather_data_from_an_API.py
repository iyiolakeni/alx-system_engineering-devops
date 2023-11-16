#!/usr/bin/python3
"""
Accessing a REST API for todo lists of employees
"""

import requests
import sys

def fetch_todo_progress(employee_id):
    """
    Fetch and display the employee's TODO list progress.
    
    Args:
    - employee_id (int): The ID of the employee.
    """
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = f"{base_url}/{employee_id}"

    try:
        # Fetch user data
        response = requests.get(url)
        response.raise_for_status()
        employee_name = response.json().get('name')

        # Fetch TODO list data
        todo_url = f"{url}/todos"
        response = requests.get(todo_url)
        response.raise_for_status()
        tasks = response.json()

        # Filter completed tasks
        done_tasks = [task for task in tasks if task.get('completed')]
        num_completed_tasks = len(done_tasks)

        # Display information
        print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{len(tasks)}):")
        for task in done_tasks:
            print(f"\t {task.get('title')}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_todo_progress(employee_id)
