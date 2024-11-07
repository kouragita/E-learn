from .. import models

class Role(models.Model):
    __tablename__ = 'roles'
    id = models.Column(models.Integer, primary_key=True)
    name = models.Column(models.String(50), nullable=False, unique=True)
    description = models.Column(models.String(150))

    users = models.relationship('User', back_populates='role')
