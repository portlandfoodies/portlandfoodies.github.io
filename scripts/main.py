import requests
import json




def main():
  term = "wendys"
  api_key = "Bearer XdBia7yU2QMsgurA7Tyzm_A9lxiTDOqp-MW7lQYi0-6AMD7zc4odwN6FtDB-LvD0bAxLQCS6OPboZ38sEQ2LtpfRaVjaTHeIqZtt87sXe-Oxfr865KbbTT9ocn8nXnYx"
  headers = {'Authorization' : api_key}
  url='https://api.yelp.com/v3/businesses/search'
  params = {'catagory':'food', 'location':'portland,or', 'term' : term, 'limit': '50', 'offset': '0', 'radius':40000}
  req = requests.get(url, params = params, headers = headers)
  data = json.loads(req.text)

  for offs in range(1, 20):
    params = {'catagory':'food', 'location':'portland,or', 'term' : term, 'radius': 40000, 'limit': '50', 'offset': (offs*50)}
    req = requests.get(url, params = params, headers = headers)
    temp = data['businesses']
    temp2 = json.loads(req.text)
    for bs in temp2["businesses"]:
      temp.append(bs)

  with open( term + '.json', 'w+', encoding='utf-8') as ofile:
     json.dump(data, ofile, ensure_ascii=False, indent=4)


main()