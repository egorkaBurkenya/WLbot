import random
from loguru import logger

def unpucking(value):
  answer = ''
  num = 0
  for i in value:
    num += 1
    answer += f'\n {num}. {i["first_value"]} - {i["second_value"]}'
  return answer

def unpucking_random_value(value):
  logger.debug(value)
  logger.debug(len(value))
  logger.error(random.randint(0, len(value)))
  value = value[random.randint(0, len(value))]
  return f'{value["first_value"]} - {value["second_value"]}'
