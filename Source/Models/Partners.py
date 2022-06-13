import time
from bson.objectid import ObjectId


class PartnersModel:
    def __init__(self, client):
        self.dao = client.db.patrners

    def insert(self,
               INN,
               companyName,
               legalAddress,
               realAddress,
               fieldOfWork,
               productionField,
               telephone,
               email,
               web
               ):

        # Дефолтный статус - 0
        # Также запоминаем время создания записи

        insert = self.dao.insert_one({
            "company": {
                "INN": INN,
                "name": companyName,
            },
            "contacts": {
                "telephone": telephone,
                "email": email,
                "web": web
            },
            "adress": {
                "realAddress": realAddress,
                "legalAddress": legalAddress
            },
            "field": fieldOfWork,
            "production": productionField,
            "status": 0,
            "creationDate": time.time()
        })
        return insert

    def read(self):
        cursor = self.dao.find()
        if cursor:
            partners = []
            for _partner in cursor:
                partners.append(_partner)
            return {"partners": partners}
        else:
            return {"Error": "No cursor founded"}

    def read_one(self, _id):
        cursor = self.dao.find_one({"_id": ObjectId(_id)})
        if cursor:
            return cursor
        else:
            return {"Error": "No data found"}

#
