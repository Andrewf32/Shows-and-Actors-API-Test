from models.shows import Shows, show_schema, shows_schema

def add_show():
    actor_name = request.json['actor_name']
    character_name = request.json['character_name']
    title = request.json['title']
    year_released = request.json['year_released']

    record = Shows(actor_name, character_name, title, year_released)

    db.session.add(record)
    db.session.commit()

    return show_schema.jsonify(record)


def get_all_shows():
    all_results = Shows.query.all()
    record = shows_schema.dump(all_results)

    return jsonify(record)


def get_show_by_id(id):
    record = Shows.query.get(id)
    return show_schema.jsonify(record)


def edit_show(id):
    show = Shows.query.get(id)

    actor_name = request.json['actor_name']
    character_name = request.json['character_name']
    title = request.json['title']
    year_released = request.json['year_released']

    show.actor_name = actor_name
    show.character_name = character_name
    show.title = title
    show.year_released = year_released

    db.session.commit()
    return show_schema.jsonify(show)


def delete_show(id):
    record = Shows.query.get(id)
    db.session.delete(record)
    db.session.commit()

    return "Actor and Show successfully deleted"