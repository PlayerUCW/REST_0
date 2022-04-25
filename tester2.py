from requests import get, post, delete
import datetime


print(get('http://localhost:5000/api/jobs').json())


print(delete('http://localhost:5000/api/jobs/999').json())
print(delete('http://localhost:5000/api/jobs/-42').json())
print(delete('http://localhost:5000/api/jobs/3').json())


print(get('http://localhost:5000/api/jobs').json())