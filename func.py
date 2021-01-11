def unpucking(value):
  answer = ''
  num = 0
  for i in value:
    num += 1
    answer += f'\n {num}. {i["first_value"]} - {i["second_value"]}\n_'
  return answer
