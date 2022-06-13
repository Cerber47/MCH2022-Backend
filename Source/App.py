from flask import Flask
from flask import Blueprint
from pymongo import MongoClient
from Routers.Router import AppRouter
from Controllers.Partners import PartnersController
from Models.Partners import PartnersModel


PARTNERSBP = "/partners"


if __name__ == "__main__":
    # Запуск серверного приложения
    print("STARTING AN APPLICATION")
    app = Flask(__name__)

    # Создают раутинг
    bp = Blueprint(PARTNERSBP, __name__)

    # Подключаем базу данных
    router = AppRouter(bp)
    client = MongoClient("localhost", 27017)
    db = client.db

    # Контролеры
    partners_model = PartnersModel(client)
    controller = PartnersController(partners_model)

    # Прописываем контролерам раутинг
    router.route_partners(controller)
    app.register_blueprint(bp, url_prefix="/partners")
    print(app.url_map)
    app.run(host="0.0.0.0")