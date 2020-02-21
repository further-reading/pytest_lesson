from leap_year import is_leap_year


def test_2020_True():
    # Arrange
    expected = True
    input = 2020
    # Act
    actual = is_leap_year(input)
    # Assert
    assert expected == actual
