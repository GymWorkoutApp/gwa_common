from datetime import datetime

from gwa_common.app import db


class BaseModel(db.Model):
    __abstract__ = True

    deleted = db.Column(db.Boolean(), default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

