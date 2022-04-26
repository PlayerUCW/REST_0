from requests import get, post, delete
import datetime


print(post('http://localhost:5000/api/jobs/4',json={
    'team_leader': 1,
    'job': 'EDITED',
    'work_size': 5,
    'collaborators': 1,
    'start_date': datetime.datetime.strftime(datetime.datetime.now(), format="%m/%d/%Y, %H:%M:%S"),
    'end_date': datetime.datetime.strftime(datetime.datetime.now(), format="%m/%d/%Y, %H:%M:%S"),
    'is_finished': True
}).json())