import pymysql as db


def get_points(country, points):
    connection = db.connect('localhost', 'user', 'pass', 'db')
    cursor = connection.cursor(db.cursors.DictCursor)
    query = "SELECT * FROM winners WHERE country LIKE %s AND points = %s"
    cursor.execute(query, (country, points))
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows
