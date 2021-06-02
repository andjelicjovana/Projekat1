import json
'''
K O R I S N I C I
'''
def import_users():
    with open('users_load.txt') as json_file:
        data = json.load(json_file)
        return data

def add_users(data):
    with open('users_load.txt','r+') as json_file:
        json.dump(data, json_file,indent=4)

'''
K NJ I G E
'''
def import_data():
    with open('books_load.txt') as json_file:
        data = json.load(json_file)
        return data

def add_data(data):
    with open('books_load.txt','r+') as json_file:
        json.dump(data, json_file,indent=4)

def change_data(data):
    with open('books_load.txt','w') as json_file:
        json.dump(data, json_file,indent=4)

'''
A K C I J S K E  P O N U D E
'''

def import_akcije():
    with open('akcije_load.txt') as json_file:
        data = json.load(json_file)
        return data

def add_akcije(data):
    with open('akcije_load.txt','r+') as json_file:
        json.dump(data, json_file,indent=4)