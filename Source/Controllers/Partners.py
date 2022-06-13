from flask import request
from Encoder import CustomJSONEncoder
import json


# Основной контролер
class PartnersController:
    def __init__(self, model):
        self.model = model

    # Чтение всех записей бизнеса
    def get_all(self):
        data = self.model.read()
        return CustomJSONEncoder().encode(data)

    # Чтение одной записи бизнеса
    def get_one(self, _id):
        data = self.model.read_one(_id)
        return CustomJSONEncoder().encode(data)

    # Регистрация новой записи
    def store(self):
        content = request.get_json()

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

        return insert
