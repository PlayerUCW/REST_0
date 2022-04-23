import flask
from flask import jsonify, request
from data import db_session
from data.__all_models import *

blueprint = flask.Blueprint(
    'api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).all()
    return jsonify(
        {
            'news': [item.to_dict() for item in news]
        }
    )


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['GET'])
def get_one_job(jobs_id):
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).get(jobs_id)
    if not news:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {'jobs': news.to_dict()}
    )


@blueprint.route('/api/jobs', methods=['POST'])
def create_job():
    print('\n', 'gae', '\n')
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['team_leader', 'job', 'work_size', 'collaborators',
                  'start_date', 'end_date', 'is_finished']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    jobs = Jobs(
        team_leader=request.json['team_leader'],
        job = request.json['job'],
        work_size = request.json['work_size'],
        collaborators = request.json['collaborators'],
        start_date = datetime.datetime.strptime(request.json['start_date'], "%m/%d/%Y, %H:%M:%S"),
        end_date = datetime.datetime.strptime(request.json['end_date'], "%m/%d/%Y, %H:%M:%S"),
        is_finished = request.json['is_finished'],
    )
    db_sess.add(jobs)
    db_sess.commit()
    return jsonify({'success': 'OK'})