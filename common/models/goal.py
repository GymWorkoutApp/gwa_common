from uuid import uuid4

from gwa_framework.models.base import BaseModel
from sqlalchemy import Column, String, text
from sqlalchemy.dialects.postgresql import UUID

from common.schemas.goal import GoalInputSchema


class GoalModel(BaseModel):
    __tablename__ = 'goals'

    def __init__(self, schema: GoalInputSchema = None):
        if schema:
            self.id = schema.goal_id
            self.description = schema.description

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    description = Column(String(100), nullable=False)
