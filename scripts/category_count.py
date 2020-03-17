import json
import csv
import operator

def main():
  with open('../data/portland.json') as portland_json:
    data = json.load(portland_json)
    categories = dict()
    for bs in data['businesses']:
      for cg in bs['categories']:
        categ = cg['title']
        if cg['title'] in categories:
          categories[categ] += 1
        else:
          categories[categ] = 1
<<<<<<< HEAD
  with open('category_count.csv', 'w+') as ofile:
=======
  with open('../data/category_count.csv', 'w+') as ofile:
>>>>>>> a25779841bfcd3096b4f1111f9ce011cac226943
    for key in categories.keys():
      ofile.write("%s,%s\n"% (key, categories[key]))
  
main()