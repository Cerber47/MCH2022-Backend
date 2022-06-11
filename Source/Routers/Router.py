

class AppRouter:

    def __init__(self, bp):
        self.bp = bp

    def route_partners(self, controller):
        print("ROUTING")
        self.bp.route("/", methods=["GET"])(controller.get_all)
        self.bp.route("/<int:id>", methods=["GET"])(controller.get_one)
        self.bp.route("/", methods=["POST"])(controller.store)
