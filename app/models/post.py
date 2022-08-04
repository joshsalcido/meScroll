from .db import db

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    photo = db.Column(db.String(255), nullable=False)
    caption = db.Column(db.String(2200), nullable=True)
    location = db.Column(db.String(500), nullable=True)


    users = db.relationship("User", back_populates="posts")
    comments = db.relationship("Comment", back_populates="post")

    def to_dict(self):
        return {
            'id' : self.id,
            'user_id' : self.user_id,
            'photo' : self.photo,
            'caption' : self.caption,
            'location' : self.location
        }