import controllers
from flask import Blueprint

shows = Blueprint("shows", __name__)

@shows.route("/shows-and-actors", methods=["POST"])
def add_show():
    return controllers.add_show()

@shows.route("/view-all-shows-and-actors", methods=["GET"])
def get_all_shows():
    return cotrollers.get_all_shows()

@shows.route("/view-single-show-and-actor/<id>", methods=["GET"])
def get_show_by_id(id):
    return controllers.get_show_by_id()

@shows.route("/update-show-and-actor/<id>", methods=["PUT"])
def edit_show(id):
    return controllers.edit_show()

@shows.route("/delete-show-and-actor/<id>", methods=["DELETE"])
def delete_show(id):
    return controllers