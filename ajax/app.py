from crypt import methods
from flask import (Flask, render_template, make_response, url_for, request,
                   redirect, flash, session, send_from_directory, jsonify)
from werkzeug.utils import secure_filename
app = Flask(__name__)

# one or the other of these. Defaults to MySQL (PyMySQL)
# change comment characters to switch to SQLite

import cs304dbi as dbi
# import cs304dbi_sqlite3 as dbi

import random

app.secret_key = 'your secret here'
# replace that with a random key
app.secret_key = ''.join([ random.choice(('ABCDEFGHIJKLMNOPQRSTUVXYZ' +
                                          'abcdefghijklmnopqrstuvxyz' +
                                          '0123456789'))
                           for i in range(20) ])

# This gets us better error messages for certain common request errors
app.config['TRAP_BAD_REQUEST_ERRORS'] = True

@app.route('/')
def index():
    return render_template('rate-movies-list-sp22.html')

@app.route('/set_UID/', methods=["GET", "POST"])
def set_UID():
    if request.method == 'POST':
        if 'uid' in request.form:
            UID = request.form['uid']
            session['UID'] = UID
    return redirect(url_for('rate_movie'))

@app.route('/tt/<movie_id_number>',methods=['GET'])
def get_movies(movie_id_number):
    conn = dbi.connect()
    movie = helper.get_movies(conn, movie_id_number)
    cast = helper.get_cast(conn, movie_id_number)
    if request.method == "GET":
        return render_template('movie_from.html', movie=movie, cast=cast)

@app.route('/nm/<person_id_number>',methods=['GET'])
def get_people(person_id_number):
    conn = dbi.connect()
    person = helper.get_people(conn, person_id_number)
    staff = helper.get_addedby(conn, person_id_number)
    credits = helper.get_credits(conn, person_id_number)
    print(staff)
    if request.method == "GET":
        return render_template('person_from.html', person=person,credits=credits, staff=staff)


@app.before_first_request
def init_db():
    dbi.cache_cnf()
    # set this local variable to 'wmdb' or your personal or team db
    db_to_use = 'socialfy_db' 
    dbi.use(db_to_use)
    print('will connect to {}'.format(db_to_use))

if __name__ == '__main__':
    import sys, os
    if len(sys.argv) > 1:
        # arg, if any, is the desired port number
        port = int(sys.argv[1])
        assert(port>1024)
    else:
        port = os.getuid()
    app.debug = True
    app.run('0.0.0.0',port)
