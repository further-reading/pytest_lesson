from _login import INFO
import pymysql as db
import pytest


@pytest.fixture
def cursor():
    # Build up
    connection = db.connect(*INFO)
    cur = connection.cursor()
    # output
    yield cur
    # Tear down
    cur.close()
    connection.close()


def test_db_ireland_info(cursor):
    # Arrange
    country = 'Ireland'
    year = 1970
    expected = ((1970, 'Ireland', 'All Kinds of Everything', 'Dana (the witch)', 32),)
    query = "SELECT * FROM winners WHERE country LIKE %s AND year LIKE %s"

    # Act
    cursor.execute(query, (country, year))
    actual = cursor.fetchall()

    # Assert
    assert actual == expected


def test_db_sweden_info(cursor):
    # Arrange
    country = 'Sweden'
    year = 1974
    expected = ((1974, 'Sweden', 'Waterloo', 'ABBA', 24),)
    query = "SELECT * FROM winners WHERE country LIKE %s AND year LIKE %s"

    # Act
    cursor.execute(query, (country, year))
    actual = cursor.fetchall()
    # Assert
    assert actual == expected
