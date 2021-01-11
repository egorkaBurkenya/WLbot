import random

def unpucking(value):
  answer = ''
  num = 0
  for i in value:
    num += 1
    answer += f'\n {num}. {i["first_value"]} - {i["second_value"]}'
  return answer

def unpucking_random_value(value):
  value = value[random.randint(0, len(value))]
  return f'{value["first_value"]} - {value["second_value"]}'
