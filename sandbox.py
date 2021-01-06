#Lister tous les livres (type “Book”) ;
#Lister tous les auteurs distincts
#Compter le nombre de publications depuis 2011 et par type ;

#publis_toru= db.publis.find({"authors":{'$regex':'Toru Ishida'}}, {"title":1, "_id":0})

from pymongo import MongoClient 
client = MongoClient('mongodb://localhost:27017')


myclient = MongoClient("mongodb://localhost:27017/")
mydb = myclient.DBLP
mycol = mydb.publis



#compter le nombre de publication 2011 et par type
#db.zips.distinct("state", db.zips.aggregate([ {$group:{_id:{state:"$state", city:"$city"},numberOfzipcodes:{$sum:1}}}, {$sort:{numberOfzipcodes:-1}}]))
a = mycol.find({"year":{"$gte": 2011}})
articles_types = a.distinct("type")
print(list(a.rewind()))



    



