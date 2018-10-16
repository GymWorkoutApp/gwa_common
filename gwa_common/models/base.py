from datetime import datetime

from gwa_common.app import db


class BaseModel(object):

    deleted = db.Column(db.Boolean(), default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

