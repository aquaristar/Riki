"""
    Models
    ~~~~~~
"""
from wiki.web import db

class Page(db.Model):
    """
    Create a Page table
    """

    __tablename__ = 'page'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), index=True, unique=True)
    title = db.Column(db.String(60))
    body = db.Column(db.String(1000))
    tags = db.Column(db.String(200))

    def __repr__(self):
        return 'Page: {}>'.format(self.title)
