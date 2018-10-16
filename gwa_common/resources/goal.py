from gwa_framework.resource.base import BaseResource


class GoalResource(BaseResource):

    def get(self):
        return {'hello': 'world'}
