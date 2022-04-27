from requests import get, post, delete
import datetime


print(get('http://localhost:5000/api/users').json())
print(post('http://localhost:5000/api/users', json={
    'id': 5,
    'surname': 'Testov',
    'name': 'Test',
    'age': 0,
    'sex': 'male',
    'position': '123',
    'speciality': '123',
    'address': 'module_1',
    'email': 't@t.t',
    'password': 'qwerty'
}).json())
print(get('http://localhost:5000/api/users/5').json())
print(post('http://localhost:5000/api/users/5', json={
    'surname': 'Testov',
    'name': 'Test',
    'age': 999,
    'sex': 'male',
    'position': '12345',
    'speciality': '12345',
    'address': 'module_1',
    'email': 't@t.t',
    'password': 'qwerty'
}).json())
print(get('http://localhost:5000/api/users/5').json())
print(delete('http://localhost:5000/api/users/5').json())
print(get('http://localhost:5000/api/users').json())