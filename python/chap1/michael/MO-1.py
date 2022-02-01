'''
chapter 1
excercise 1
Problem:
Find average of all the elements in a list.

'''


def avg(elements):
  return sum(elements) / len(elements)

if __name__ == '__main__':
  numbers = [2, 45, 89, 12, 4, 7, 19]
  average = avg(numbers)
  print(f'Average: {round(average, 2)}')