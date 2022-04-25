from requests import get, post, delete
import datetime


print(delete('http://localhost:5000/api/jobs/4').json())