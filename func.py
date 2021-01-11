def unpucking(value):
  answer = ''
  for i in value:
    answer += f'\n {i['first_value']} - {i['second_value']}'
  return answer
