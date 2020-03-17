import requests
import json


def main():
    name = "burgerville-portland"
    out_data = {"businesses" : []}
    with open( name + '.json') as ifile:
        data = json.load(ifile)
    
    for business in data["businesses"]:
        if name in business["alias"]:
            out_data["businesses"].append(business)

    with open(name + '-cleaned.json', 'w+', encoding='utf-8') as ofile:
     json.dump(out_data, ofile, ensure_ascii=False, indent=4)


main()