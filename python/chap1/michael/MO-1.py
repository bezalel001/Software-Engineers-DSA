'''
chapter 1
excercise 1
Problem:
Find average of all the elements in a list.

'''


def avg(elements):
  if len(elements) > 0:
    average = sum(elements) / len(elements)
    return round(average, 2)
  return None

if __name__ == '__main__':
  numbers = [1, 3, 4, 5, 6, 6]
  average = avg(numbers)
  print(f'Average: {average}')