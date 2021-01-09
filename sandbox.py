from pymongo import MongoClient
import json


def json_to_mongodb(name_file):
    client = MongoClient("mongodb://localhost:27017/")

    list_dblp = list(open(name_file, 'r'))

    percent_count = 0
    absolute_count = 0
    error_count = 0

    for line in list_dblp:
        try:
            client.DBLP.publis.insert_one(json.loads(line))
        except:
            error_count += 1
            print(error_count, "error(s)")
            pass
        absolute_count +=1
        if int((absolute_count / len(list_dblp)) * 100) > percent_count:
            percent_count += 1
            print(percent_count, "%")

    print("done")
json_to_mongodb("Database/dblp.json")