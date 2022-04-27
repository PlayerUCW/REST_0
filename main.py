from flask import Flask
from flask import render_template, make_response, request, redirect, jsonify
from flask_login import LoginManager, login_user, login_required,\
    current_user, logout_user
from data import db_session
from data.__all_models import *
from data.forms import *
import requests
import datetime
import random
import api
import users_api


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
lm = LoginManager()
lm.init_app(app)


@lm.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/')
def index():
    base = db_session.create_session()
    raw = base.query(Jobs)
    jobs = []
    for job in raw:
        res = []
        res.append(job.job)
        user = base.query(User).filter(User.id == job.team_leader).first()
        res.append(user.surname + '' + user.name)
        res.append(job.work_size)
        res.append(job.collaborators)
        if job.is_finished:
            res.append('Завершено')
        else:
            res.append('Не завершено')
        jobs.append(res)
    return render_template('jobs.html',
                           title='MARS', jobs=jobs)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = UserForm()
    if form.validate_on_submit():
        if form.password.data != form.pwc.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Почта занята")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            sex=form.sex.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address='module_' + str(random.choice(range(43))),
            email=form.email.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/add_job',  methods=['GET', 'POST'])
@login_required
def add_news():
    form = JobsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = Jobs()
        job.job = form.job.data
        job.team_leader = form.tl.data
        job.work_size = form.duration.data
        job.collaborators = form.loc.data
        job.start_date = form.start.data
        job.end_date = form.start.data + datetime.timedelta(hours=form.duration.data)
        job.is_finished = False
        db_sess.add(job)
        db_sess.commit()
        return redirect('/')
    return render_template('redactor.html', title='Добавление работы',
                           form=form)


@app.route('/users_show/<int:user_id>')
def nostalgee(user_id):
    user = requests.get(f'http://localhost:5000/api/users/{user_id}').json()['users']
    coords = requests.get(f'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&'
                          f'geocode={user["city_from"]}&format=json').json()["response"][
        "GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
    with open('static/map.png', 'wb') as img:
        img.write(requests.get(f'http://static-maps.yandex.ru/1.x/?ll={coords.replace(" ", ",")}&spn=0.1,0.1&l=sat').content)
    return render_template('show.html', title='Родной город', city=user['city_from'],
                           fname=user['name'] + ' ' + user['surname'])


def main():
    db_session.global_init("db/mars.db")
    app.register_blueprint(api.blueprint)
    app.register_blueprint(users_api.blueprint)
    app.run()


if __name__ == '__main__':
    main()