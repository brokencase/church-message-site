import pymysql.cursors
import os

#db connection
DB_HOST = os.environ.get('DB_HOST')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_NAME = os.environ.get('DB_NAME')

def db_init():
    return pymysql.connect(host= DB_HOST,
                             user= DB_USER,
                             password= DB_PASSWORD,
                             db= DB_NAME,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

def display_recent_sermons(number):
    connection = db_init()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM Sermons WHERE SermonStatus = 1 ORDER BY SermonDate DESC LIMIT %s"
            cursor.execute(sql, (number))
            result = cursor.fetchall()
            connection.commit()
    finally:
        cursor.close()
        connection.close()
    return result 

def display_all_series():
    connection = db_init()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM SermonSeries ORDER BY SeriesName"
            cursor.execute(sql)
            result = cursor.fetchall()
            connection.commit()
    finally:
        cursor.close()
        connection.close()
    return result 

def display_all_preachers():
    connection = db_init()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT DISTINCT PreacherName FROM Sermons ORDER BY PreacherName"
            cursor.execute(sql)
            result = cursor.fetchall()
            connection.commit()
    finally:
        cursor.close()
        connection.close()
    return result 

def sermon_search(title,date,preacher,series):
    if len(date) > 0:
        sql = f"SELECT * FROM Sermons WHERE SermonStatus = 1 AND SermonDate BETWEEN DATE_ADD('{date}', INTERVAL -8 DAY) AND DATE_ADD('{date}', INTERVAL 8 DAY) ORDER BY SermonDate LIMIT 3"
    else:
        sql = f"SELECT * FROM Sermons WHERE SermonStatus = 1 AND (TITLE LIKE '%{title}%' AND PreacherName LIKE '%{preacher}%' AND SeriesTitle LIKE '%{series}%') ORDER BY SermonDate DESC"
    connection = db_init()
    try:
        with connection.cursor() as cursor:
            print(sql) 
            cursor.execute(sql)
            result = cursor.fetchall()
            connection.commit()
    finally:
        cursor.close()
        connection.close()
    return result 

def get_sermon_by_id(id):
    connection = db_init()
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM Sermons WHERE SermonStatus = 1 AND Id = {id}"
            print(sql)
            cursor.execute(sql)
            result = cursor.fetchone()
            connection.commit()
    finally:
        cursor.close()
        connection.close()
    return result

# try:
#     with connection.cursor() as cursor:
#         # Create a new record
#         sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
#         cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

#     # connection is not autocommit by default. So you must commit to save
#     # your changes.
#     connection.commit()

#     with connection.cursor() as cursor:
#         # Read a single record
#         sql = "SELECT * FROM Sermons WHERE Id =%s"
#         cursor.execute(sql, ('5',))
#         result = cursor.fetchone()
#         print(result)
# finally:
    #connection.close()