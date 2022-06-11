from flask import Flask
from flask import Blueprint
from pymongo import MongoClient
from Source.Routers.Router import AppRouter
from Source.Controllers.Partners import PartnersController
from Source.Models.Partners import PartnersModel


PARTNERSBP = "/patners"


if __name__ == "__main__":
    print("STARTING AN APPLICATION")
    app = Flask(__name__)
    router = AppRouter(Blueprint(PARTNERSBP, __name__))
    client = MongoClient("localhost", 27017, username="username", password="password")
    db = client.db

    partners_model = PartnersModel()

    controller = PartnersController(partners_model)

    router.route_partners(controller)

    app.run(host="0.0.0.0")