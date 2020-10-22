from flask import *
from database import connection, todo_list_dao
import numpy as np
from datetime import datetime

today = datetime.today()

app = Flask(__name__)
app.secret_key = "amustring"

@app.route('/')
def login():
    return render_template("login2.html")


@app.route('/main', methods=["POST"])
def main():
    try:
        id = int(request.form['id']) # request는 string으로 받기 때문에 int형으로 바꿔준다
        pw = request.form['pass']
    except:
        return render_template('login_fail.html')

    content_list=todo_list_dao.get_todolist(id, pw) # Manager 테이블의 데이터를 2차원 배열로 가져옴

    try:
        if request.method == "POST" and content_list:
            session['id'] = id

        if 'id' in session:
            manager = content_list[0]
            return render_template('main.html', name=manager, date=today)
        else:
            return render_template('login_fail.html')
    except:
        return render_template('login_fail.html')


@app.route('/logout')
def logout():
    if 'id' in session:
        session.pop('id', None)  # pop 메소드로 세션 변수 제거
        return render_template('logout.html')
    else:
        return render_template('session_error')

@app.route('/profile')
def profile():
    if 'email' in session:
        email = session['email']
        return render_template('profile.html', name=email)
    else:
        return '<p>Please login first</p>'

if __name__ == '__main__':
    app.run(debug=True)
