from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect the database to our Flask app."""

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Creates a db model showcasing pets and their features"""
    __tablename__= "pets"

    id = db.Column(db.Integer, 
                   primary_key=True, 
                   autoincrement=True)
    name=db.Column(db.Text, 
                   nullable=False)
    species=db.Column(db.Text,
                    nullable=False)
    photo_url=db.Column(db.Text, 
                        nullable=True)
    age=db.Column(db.Integer, 
                  nullable=True)
    notes=db.Column(db.Text, 
                    nullable=True)
    available=db.Column(db.Boolean, 
                        default=True,
                        nullable=False)
    

    def __repr__(self):
        """Returns representation of self"""
        return f"I am {self.name}, a {self.age} year old {self.species}. Id={self.id} Available? {self.available} "
    

    