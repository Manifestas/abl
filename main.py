import sqlite3
import os
from flask import Flask, render_template, request, g, flash, abort

from FDataBase import FDataBase

# config
DATABASE = '/tmp/abl.db'
DEBUG = True
SECRET_KEY = 'lakj9-8uqrolewnioqrklm'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(DATABASE=os.path.join(app.root_path, 'db', 'abl.db')))


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    # представление записей в виде словаря, а не кортежа
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    db = connect_db()
    with app.open_resource('db/sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    """ Cоединение с БД, если оно не установлено"""
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route('/')
def index():
    db = get_db()
    dbase = FDataBase(db)
    res = dbase.get_dkp1_list()
    return render_template('index.html',
                           dkp1_list=res, title='Список ДКП1')


@app.route('/add_dkp1', methods=['POST', 'GET'])
def add_dkp1():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == 'POST':
        if len(request.form['number']) > 0 and len(request.form['contract_date']) > 9:
            res = dbase.add_dkp1(request.form['number'], request.form['contract_date'])
            if not res:
                flash('Ошибка добавления договора', category='error')
            else:
                flash('Успешно добавлен', category='success')
        else:
            flash('Проверьте заполнение полей', category='error')
    return render_template('add_dkp1.html', title='Добавление ДКП1')


@app.route('/dkp1/<int:id_dkp1>', methods=['POST', 'GET'])
def show_dkp1(id_dkp1):
    db = get_db()
    dbase = FDataBase(db)
    if request.method == 'GET':
        dkp1_res = dbase.get_dkp1(id_dkp1)
        if not dkp1_res:
            abort(404)

        car_result = dbase.get_dkp1_car_list(id_dkp1)

        return render_template('dkp1.html',
                               dkp1=dkp1_res,
                               title='DKP1',
                               id=id_dkp1,
                               car_list=car_result)

    elif request.method == 'POST':
        number = request.form['number']
        contract_date = request.form['contract_date']
        if len(number) > 1 and len(contract_date) > 9:
            res = dbase.update_dkp1(id_dkp1, request.form['number'], request.form['contract_date'])
            if not res:
                flash('Ошибка записи договора', category='error')
            else:
                flash('Успешно записано', category='success')
        else:
            flash('Проверьте заполнение полей', category='error')
        return render_template('dkp1.html',
                               title='ДКП1',
                               number=number,
                               contract_date=contract_date,
                               id=id_dkp1)


@app.route('/cars/<int:car_id>', methods=['POST', 'GET'])
def show_car(car_id):
    db = get_db()
    dbase = FDataBase(db)
    if request.method == 'GET':
        car_result = dbase.get_car(car_id)
        if not car_result:
            abort(404)

        return render_template('cars.html',
                               title='Car',
                               car=car_result)


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
