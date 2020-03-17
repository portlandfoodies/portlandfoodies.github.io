import requests
import json
import operator



def main():
  review_count_id = {}
  name = "burgerville-portland-cleaned"
  with open('../data/' + name + '.json') as ifile:
    data = json.load(ifile)

  for business in data["businesses"]:
    review_count_id[business['id']] = business['review_count']
  sorted_item_id = sorted(review_count_id.items(), key=operator.itemgetter(1), reverse=True)
  
  api_key = "Bearer XdBia7yU2QMsgurA7Tyzm_A9lxiTDOqp-MW7lQYi0-6AMD7zc4odwN6FtDB-LvD0bAxLQCS6OPboZ38sEQ2LtpfRaVjaTHeIqZtt87sXe-Oxfr865KbbTT9ocn8nXnYx"
  headers = {'Authorization' : api_key}

  
  review_data = {

  }
  review_data['business_reviews'] = []
  for reviews in sorted_item_id:
    url='https://api.yelp.com/v3/businesses/' + reviews[0] + '/reviews'
    params = {'limit': 50}
    req = requests.get(url, params = params, headers = headers)
    data = json.loads(req.text)
    for rw in data['reviews']:
      review_data['business_reviews'].append(rw)
  
  # writing reviews to file at the end. not the best way to do it
  with open( name + '-reviews.json', 'w+', encoding='utf-8') as ofile:
     json.dump(review_data, ofile, ensure_ascii=False, indent=4)
  


main()