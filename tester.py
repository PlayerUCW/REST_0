from requests import get, post
import datetime


# 1
# Ошибка: неверный ID
print(post('http://localhost:5000/api/jobs',
           json={'id': 2,
                 'team_leader': 1,
                 'job': 'wtf',
                 'work_size': 5,
                 'collaborators': 1,
                 'start_date': datetime.datetime.strftime(datetime.datetime.now(), format="%m/%d/%Y, %H:%M:%S"),
                 'end_date': datetime.datetime.strftime(datetime.datetime.now(), format="%m/%d/%Y, %H:%M:%S"),
                 'is_finished': True}).json())


# 2
# Ошибка: неправильный тимлид
print(post('http://localhost:5000/api/jobs',
           json={'id': 5,
                 'team_leader': 696969,
                 'job': 'wtf',
                 'work_size': 5,
                 'collaborators': 1,
                 'start_date': datetime.datetime.strftime(datetime.datetime.now(), format="%m/%d/%Y, %H:%M:%S"),
                 'end_date': datetime.datetime.strftime(datetime.datetime.now(), format="%m/%d/%Y, %H:%M:%S"),
                 'is_finished': True}).json())


# 3
# Ошибка: даты не даты
print(post('http://localhost:5000/api/jobs',
           json={'id': 5,
                 'team_leader': 1,
                 'job': 'wtf',
                 'work_size': 5,
                 'collaborators': 1,
                 'start_date': 'того дня',
                 'end_date': 'вечор',
                 'is_finished': True}).json())


# 4
# Вроде всё верно
print(post('http://localhost:5000/api/jobs',
           json={'id': 5,
                 'team_leader': 1,
                 'job': 'wtf',
                 'work_size': 5,
                 'collaborators': 1,
                 'start_date': datetime.datetime.strftime(datetime.datetime.now(), format="%m/%d/%Y, %H:%M:%S"),
                 'end_date': datetime.datetime.strftime(datetime.datetime.now(), format="%m/%d/%Y, %H:%M:%S"),
                 'is_finished': True}).json())