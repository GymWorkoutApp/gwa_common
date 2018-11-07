from common.resources.goal import GoalResource

resources_v1 = [
    {'resource': GoalResource, 'urls': ['/goals'], 'endpoint': 'Goals', 'methods': ['POST', 'GET', 'PUT']}
]
