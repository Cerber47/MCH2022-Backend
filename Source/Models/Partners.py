

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
        return self.dao.insert({
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
            "production": productionField
        })

    def read(self):
        return self.dao.find()

    #def

#
