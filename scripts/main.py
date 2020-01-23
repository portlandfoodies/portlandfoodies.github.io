## this code is used for requesting restaurant infomation in Portland Oregon97266 using the Yelp Fusion API.
## Yelp Fusion has a limit of up to 50 results returned back in a single request and up to 1000 total with the use of offset. 
## 02/21/2020
## PSU CS410 Data Analysis - Team Portlandfoodies
import requests
import json




def main():
  api_key = "Bearer " + ""
  headers = {'Authorization' : api_key}
  url='https://api.yelp.com/v3/businesses/search'
  params = {'catagory':'food', 'location':'portland,or,97266', 'limit': '50', 'offset': '0', 'radius':40000}
  req = requests.get(url, params = params, headers = headers)
  data = json.loads(req.text)

  for offs in range(1, 20):
    params = {'catagory':'food', 'location':'portland,or,97266', 'radius': 40000, 'limit': '50', 'offset': (offs*50)}
    req = requests.get(url, params = params, headers = headers)
    temp = data['businesses']
    temp2 = json.loads(req.text)
    temp.append(temp2['businesses'])

  with open('portland97266.json', 'w+', encoding='utf-8') as ofile:
     json.dump(data, ofile, ensure_ascii=False, indent=4)


main()
