#!/usr/bin/python3
''' Python script to extract employee info using the JSONPlaceholder API'''
import requests
import sys

if __name__ == '__main__':
    site = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(site, sys.argv[1])
    req = requests.get(user)
    json_o = req.json()
    print("Employee {} is done with tasks".format(json_o.get('name')), end='')

    todos = '{}todos?userId={}'.format(site, sys.argv[1])
    req = requests.get(todos)
    tasks = req.json()
    l_task = []
    for task in tasks:
        if task.get('completed') is True:
            l_task.append(task)

    print("({}/{}):".format(len(l_task), len(tasks)))
    for task in l_task:
        print("\t {}".format(task.get("title")))
