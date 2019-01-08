from typing import Dict
from uuid import uuid4

from gwa_framework.resource.base import BaseResource
from gwa_framework.utils.decorators import validate_schema

from src.cache import cache
from src.database import master_async_session, read_replica_async_session
from src.models import GoalModel
from src.repositories import GoalRepository
from src.schemas import GoalInputSchema, GoalOutputSchema


class GoalResource(BaseResource):
    cache = cache
    method_decorators = {
        'create': [validate_schema(GoalInputSchema)],
        'update': [validate_schema(GoalInputSchema)],
    }

    def create(self, request_model: 'GoalInputSchema') -> Dict:
        goal = GoalModel()
        goal.id = request_model.goal_id or str(uuid4())
        goal.description = request_model.description
        with master_async_session() as session:
            session.add(goal)
            output = GoalOutputSchema()
            output.goal_id = goal.id
            output.description = goal.description
            output.validate()
            return output.to_primitive()

    def update(self, request_model: 'GoalInputSchema', goal_id=None):
        goal = GoalModel()
        goal.id = goal_id
        goal.description = request_model.description
        with master_async_session() as session:
            session.merge(goal)
            output = GoalOutputSchema()
            output.goal_id = goal.id
            output.description = goal.description
            output.validate()
            return output.to_primitive()

    def list(self, args=None, kwargs=None):
        with read_replica_async_session() as session:
            results = []
            for goal in session.query(GoalModel).all():
                schema = GoalOutputSchema()
                schema.goal_id = goal.id
                schema.description = goal.description
                results.append(schema.to_primitive())
        return results

    def retrieve(self, goal_id):
        with read_replica_async_session() as session:
            goal = session.query(GoalModel).filter_by(id=goal_id).first()
            schema = GoalOutputSchema()
            schema.goal_id = goal.id
            schema.description = goal.description
            return schema.to_primitive()

    def destroy(self, goal_id):
        with master_async_session() as session:
            session.query(GoalModel).filter_by(id=goal_id).delete()
            return None


resources_v1 = [
    {'resource': GoalResource, 'urls': ['/goals/<goal_id>'], 'endpoint': 'Goals GoalId',
     'methods': ['GET', 'PUT', 'PATCH', 'DELETE']},
    {'resource': GoalResource, 'urls': ['/goals'], 'endpoint': 'Goals',
     'methods': ['POST', 'GET']},
]
