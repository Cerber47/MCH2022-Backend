from flask import request
from Source.Encoder import CustomJSONEncoder
import json


class PartnersController:
    def __init__(self, model):
        self.model = model

    def get_all(self):
        data = self.model.read()
        return json.encode(data, cls=CustomJSONEncoder)

    def get_one(self, id):
        pass

    def store(self):
        content = request.get_json()
        print(content)

        INN = content["INN"]
        name = content["companyName"]
        legalAddress = content["legalAddress"]
        realAddress = content["realAddress"]
        telephone = content["telephone"]
        webPage = content["web"]
        email = content["email"]
        field = content["field"]
        production = content["production"]

        insert = self.model.insert(
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
        print(insert)
        return insert

    def update(self, id, json):
        pass