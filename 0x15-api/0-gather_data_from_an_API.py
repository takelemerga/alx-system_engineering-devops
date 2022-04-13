#!/usr/bin/python3
'''
Python script that returns information using REST API
'''
import requests
from sys import argv

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com"
    userId = argv[1]
    user = requests.get(url + "users/{}".
                        format(userId), verify=False).json()
    alltask = requests.get(url + "todos?userId={}".
                        format(userId), verify=False).json()
    completed_tasks = []
    for task in alltask:
        if task.get('completed') is True:
            completed_tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(completed_tasks), len(alltask)))
    print("\n".join("\t {}".format(task) for task in completed_tasks))
