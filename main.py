import unittest 
import cardReader

class TestCardReader(unittest.TestCase):
  def test_emptyLog(self):
    logs = [("Paul", "enter")]
    expected = ([], [])
    actual = cardReader.find_missing_entries(logs)
    self.assertCountEqual(expected, actual)

  def test_ReturnsFaultyExitsWhenPresent(self):
    input = [
      ('Paul', 'enter'),
      ('Mary', 'enter'),
      ('Mary', 'exit'),
      ('Paul', 'enter'),
      ('Paul', 'exit'),
    ]
    expected = (['Paul'], [])
    actual = cardReader.find_missing_entries(input)
    self.assertCountEqual(expected[0], actual[0])
    self.assertCountEqual(expected[1], actual[1])

  def test_ReturnsFaultyExitsAndEntriesWhenPresent(self):
    input = [
      ('Paul', 'exit'),
      ('Mary', 'enter'),
      ('Mary', 'exit'),
      ('Ignatius', 'exit'),
      ('Benedict', 'enter'),
      ('Benedict', 'enter'),
      ('Benedict', 'exit'),
      ('Mary', 'enter'),
      ('Mary', 'exit'),
      ('Ignatius', 'enter'),
    ]
    expected = (
      ['Benedict', 'Ignatius'],
      ['Ignatius', 'Paul'],
    )
    actual = cardReader.find_missing_entries(input)
    self.assertCountEqual(expected[0], actual[0])
    self.assertCountEqual(expected[1], actual[1])

  def test_ReturnsOnlyOneFaultyExitPerEmployeeWhenPresent(self):
    input = [
      ('Paul', 'enter'),
      ('Paul', 'enter'),
      ('Paul', 'exit'),
      ('Paul', 'enter'),
    ]
    expected = (['Paul'], [])
    actual = cardReader.find_missing_entries(input)
    self.assertCountEqual(expected[0], actual[0])
    self.assertCountEqual(expected[1], actual[1])

  def test_ReturnsOnlyOneFaultyEntryPerEmployeeWhenPresent(self):
    input = [
      ('Paul', 'exit'),
      ('Paul', 'enter'),
      ('Paul', 'exit'),
      ('Paul', 'exit'),
      ('Paul', 'enter'),
      ('Paul', 'exit'),
    ]
    expected = ([], ['Paul'])
    actual = cardReader.find_missing_entries(input)
    self.assertCountEqual(expected[0], actual[0])
    self.assertCountEqual(expected[1], actual[1])

  def test_ReturnsOnlyOneFaultyEntryAndExitPerEmployeeWhenPresent(self):
    input = [
      ('Paul', 'exit'),
      ('Paul', 'enter'),
      ('Paul', 'exit'),
      ('Paul', 'exit'),
      ('Paul', 'enter'),
      ('Paul', 'exit'),
      ('Paul', 'enter'),
      ('Paul', 'enter'),
      ('Paul', 'exit'),
      ('Paul', 'enter'),
    ]
    expected = (['Paul'], ['Paul'])
    actual = cardReader.find_missing_entries(input)
    self.assertCountEqual(expected[0], actual[0])
    self.assertCountEqual(expected[1], actual[1])

if __name__ == '__main__':
    unittest.main(verbosity=2)
    
  