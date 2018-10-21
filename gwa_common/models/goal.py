import uuid

from sqlalchemy.dialects.postgresql import UUID

from gwa_common.app import db
from gwa_common.models.base import BaseModel


class GoalModel(BaseModel):
    __tablename__ = 'goals'

    id = db.Column(UUID(as_uuid=True), nullable=False, unique=True, default=uuid.uuid4())
    description = db.Column(db.String(100), nullable=False)



