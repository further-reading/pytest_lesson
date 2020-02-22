from unittest.mock import patch
import database_example


@patch("database_example.db")
def test_db_connection_steps(mock_db):
    # Arrange
    mock_connection = mock_db.connect()
    country = 'country'
    points = 123
    db_host = 'localhost'
    db_user = 'user'
    db_password = 'pass'
    db_name = 'db'

    # Act
    database_example.get_points(country, points)

    # Assert
    mock_db.connect.assert_called_with(db_host, db_user, db_password, db_name)
    assert mock_connection.close.call_count == 1
    assert mock_connection.commit.call_count == 0


@patch("database_example.db")
def test_db_cursor_steps(mock_db):
    # Arrange
    mock_connection = mock_db.connect()
    mock_cursor = mock_connection.cursor()
    query = "SELECT * FROM winners WHERE country LIKE %s AND points = %s"
    country = 'country'
    points = 123

    # Act
    database_example.get_points(country, points)

    # Assert
    mock_cursor.execute.assert_called_with(query, (country, points))
    assert mock_cursor.fetchall.call_count == 1
    assert mock_cursor.close.call_count == 1
