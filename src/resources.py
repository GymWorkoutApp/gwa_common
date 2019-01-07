from uuid import uuid4

from gwa_framework.resource.base import BaseResource
from gwa_framework.utils.decorators import validate_schema

from src.cache import cache
from src.models import GoalModel
from src.repositories import GoalRepository
from src.schemas import GoalInputSchema, GoalOutputSchema


class GoalResource(BaseResource):
    cache = cache
    method_decorators = {
        'create': [validate_schema(GoalInputSchema)],
        'update': [validate_schema(GoalInputSchema)],
    }

    def create(self, request_model: 'GoalInputSchema'):
        goal = GoalModel()
        goal.id = request_model.goal_id or str(uuid4())
        goal.description = request_model.description
        goal = GoalRepository.create(goal)
        return GoalOutputSchema(goal_id=goal.id, description=goal.description).to_primitive()

    def update(self, request_model: 'GoalInputSchema'):
        goal = GoalModel()
        goal.id = request_model.goal_id or str(uuid4())
        goal.description = request_model.description
        goal = GoalRepository.create(goal)
        return GoalOutputSchema(goal_id=goal.id, description=goal.description).to_primitive()

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

    def delete(self, filter, filter2, kwargs=None):
        return {'filter': filter, 'filter2': filter2, 'args': kwargs, 'kwargs': kwargs}


resources_v1 = [
    {'resource': GoalResource, 'urls': ['/goals'], 'endpoint': 'Goals',
     'methods': ['POST', 'GET', 'PUT', 'PATCH', 'DELETE']}
]
