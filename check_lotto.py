import requests
import random

my_numbers = random.sample(range(1,46), 6)

url = 'http://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo='
res = requests.get(url).json()
drw_numbers = []
bonus_number = res['bnusNo']

for key, value in res.items():
  if 'drwtNo' in key:
    drw_numbers.append(value)


match_numbers = set(drw_numbers) & set(my_numbers) 
match_count = len(match_numbers)
print(match_count)

if match_count == 6:
  print('1등')
elif match_count == 5 and bonus_number in my_numbers:
  print('2등')
elif match_count == 5:
  print('3등')
elif match_count == 4:
  print('4등')
elif match_count == 3:
  print('5등')
else:
  print('꽝')
