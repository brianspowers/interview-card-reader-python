""" Card Reader Log Parser
Takes a list of tuples where the first item is the name of the employee and the second is the type of log (enter or exit).
The log begins at the beginning of the day and ends at the end of the day.
The room is physically clear at the start and end of each day. Any bad pairs are a result of a faulty card or card reader, however each entry is true. Therefore, in the case of an exit with no preceding entry, the employee should be returned in the badEntries array, to note that their card did not read upon entry of the room.

Args:
  log (list): A list of tuples in the format ('employeeName', 'enter|exit')

Returns:
  tuple: A tuple of lists. (badExitsList, badEntriesList)
"""
def find_missing_entries(log):
  
  return ([], [])