from schematics.types import StringType

from common.schemas.base import BaseSchema


class GoalInputSchema(BaseSchema):
    goal_id = StringType(required=False, serialized_name='goalId')
    description = StringType(required=True, serialized_name='description', max_length=100, min_length=0)


class GoalOutputSchema(BaseSchema):
    goal_id = StringType(required=True, serialized_name='goalId')
    description = StringType(required=True, serialized_name='description')
