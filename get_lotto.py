import requests

url = 'http://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo='
res = requests.get(url).json()
drw_numbers = []

for key, value in res.items():
  if 'drwtNo' in key:
    drw_numbers.append(value)

drw_numbers = sorted(drw_numbers)
bonus_number = res['bnusNo']
