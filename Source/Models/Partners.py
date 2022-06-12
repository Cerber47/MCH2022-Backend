import time


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
        insert = self.dao.insert({
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
        print(insert)
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

    #def

#
