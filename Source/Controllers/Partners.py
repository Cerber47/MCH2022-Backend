from flask import request

class PartnersController:
    def __init__(self, model):
        self.model = model

    def get_all(self):
        return self.model.read()

    def get_one(self, id):
        pass

    def store(self, json):
        content = request.json

        INN = content["INN"]
        name = content["companyName"]
        legalAddress = content["legalAddress"]
        realAddress = content["realAddress"]
        telephone = content["telephone"]
        webPage = content["web"]
        email = content["email"]
        field = content["field"]
        production = content["production"]

        return self.model.insert(
               INN=INN,
               companyName=name,
               legalAddress=legalAddress,
               realAddress=realAddress,
               fieldOfWork=field,
               productionField=production,
               telephone=telephone,
               email=email,
               web=webPage
               )

    def update(self, id, json):
        pass