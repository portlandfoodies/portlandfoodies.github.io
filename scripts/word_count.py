import json
import csv
import operator

def main():
    with open('../data/reviews.json') as reviews_json:
      data = json.load(reviews_json)
      total_str = ""
      for bs in data['business_reviews']:
        total_str += " " + bs['text']
    odata = word_count(total_str)
    #with open('wordcount.json', 'w+', encoding='utf-8') as ofile:
      #json.dump(odata, ofile, ensure_ascii=False, indent=4)
    
    with open('../data/word_count.csv', 'w+') as ofile:
      for key in odata.keys():
        ofile.write("%s,%s\n"% (key, odata[key]))
    
   

def word_count(str):
    sentence = dict()
    words = str.split()

    for word in words:
      if word in sentence:
        sentence[word] += 1
      else:
        sentence[word] = 1
    return sentence

main()