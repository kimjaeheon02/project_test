import pymysql

def get_connection():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='root', db='Wanbee', charset='utf8')
    return conn
