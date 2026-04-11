from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class Note(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(db.String(200))
    content: Mapped[str] = mapped_column(db.Text)

    def to_dict(self):
        return {'id': self.id, 'title': self.title, 'content': self.content}