from requests import get, post
import datetime


print(post('http://localhost:5000/api/jobs',
           json={'team_leader': 1,
                 'job': 'lol',
                 'work_size': 5,
                 'collaborators': 1,
                 'start_date': datetime.datetime.strftime(datetime.datetime.now(), format="%m/%d/%Y, %H:%M:%S"),
                 'end_date': datetime.datetime.strftime(datetime.datetime.now(), format="%m/%d/%Y, %H:%M:%S"),
                 'is_finished': True}).json())