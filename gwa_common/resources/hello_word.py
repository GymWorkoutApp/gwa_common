from gwa_framework.resource.base import BaseResource


class HelloWorld(BaseResource):
    def get(self):
        return {'hello': 'world'}
