import pymysql
from database import connection
import numpy as np

# 해야 할 일 내용 가져오기
# 최근에 작성된 순서대로

def get_todolist(id, pw):
    conn = connection.get_connection()

    sql = '''
        select mID, mPW, mname
        from manager
    '''

    cursor = conn.cursor()
    cursor.execute(sql)
    row = cursor.fetchall()

    data_list = []

    for obj in row :
        data_dic = {'id' : obj[0],
                    'pw' : obj[1],
                    'name' : obj[2]
                    }
        data_list.append(data_dic)

    conn.close


    result=[]
    for list in data_list:
        if list['id'] == id and list['pw'] == pw:
            result.append(list['name'])

    return result

def imgInfo(year, month, day):
    conn = connection.get_connection()

    sql = '''
        select mID, mPW, mname
        from manager
    '''

    cursor = conn.cursor()
    cursor.execute(sql)
    row = cursor.fetchall()
    return
