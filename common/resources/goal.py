from gwa_framework.resource.base import BaseResource
from gwa_framework.utils.decorators import validate_schema

from common.models.goal import GoalModel
from common.repositories.goal import GoalRepository
from common.schemas.goal import GoalInputSchema, GoalOutputSchema


class GoalResource(BaseResource):
    method_decorators = {
        'create': [validate_schema(GoalInputSchema)],
        'retrieve': [validate_schema(GoalInputSchema)],
        'list': []
    }

    def create(self, request_model: 'GoalInputSchema'):
        goal = GoalRepository.create(GoalModel(request_model))
        schema = GoalOutputSchema()
        schema.goal_id = goal.id
        schema.description = goal.description
        return schema.to_primitive()

    def list(self, args=None, kwargs=None):
        goals = GoalRepository.get(kwargs)
        results = []
        for goal in goals:
            schema = GoalOutputSchema()
            schema.goal_id = goal.id
            schema.description = goal.description
            results.append(schema.to_primitive())
        return results

    def retrieve(self, filter, filter2, kwargs=None):
        return {'filter': filter, 'filter2': filter2, 'args': kwargs, 'kwargs': kwargs}
