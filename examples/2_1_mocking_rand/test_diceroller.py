from unittest.mock import patch
import diceroller


@patch("diceroller.randint")
def test_8_success(mock_randint):
    # Arrange
    mock_randint.return_value = 8
    expected = 'Success'
    # Act
    actual = diceroller.roll_dice()
    # Asset
    assert actual == expected


@patch("diceroller.randint")
def test_7_fail(mock_randint):
    # Arrange
    mock_randint.return_value = 7
    expected = 'Failure'
    # Act
    actual = diceroller.roll_dice()
    # Asset
    assert actual == expected
