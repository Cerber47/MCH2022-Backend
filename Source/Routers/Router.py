

class AppRouter:

    def __init__(self, bp):
        self.bp = bp

    def route_partners(self, controller):
        self.bp.route("/", method=["GET"])(controller.get_all)
        self.bp.route("/<int:id>", method=["GET"])(controller.get_one)
        self.bp.route("/", method=["POST"])(controller.store)
