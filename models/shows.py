from app import db

class Shows(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    actor_name = db.Column(db.String(50))
    character_name = db.Column(db.String(50), unique=False)
    title = db.Column(db.String(150), unique=False)
    year_released = db.Column(db.Integer, unique=False)

    def __init__(self, actor_name, character_name, title, year_released):
        self.actor_name = actor_name
        self.character_name = character_name
        self.title = title
        self.year_released = year_released


class ShowsSchema(ma.Schema):
    class Meta:
        fields = ('actor_name', 'character_name', 'show', 'year_released')

show_schema = ShowsAndActorsSchema()
shows_schema = ShowsAndActorsSchema(many=True)