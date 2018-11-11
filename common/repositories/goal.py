from typing import List

from common.database import async_session
from common.models.goal import GoalModel


class GoalRepository:

    @staticmethod
    def create(goal: 'GoalModel'):
        with async_session() as session:
            session.add(goal)
            session.commit()
            session.expunge(goal)
            session.close()
            return goal

    @staticmethod
    def get(kwargs=None) -> List:
        with async_session() as session:
            return session.query(GoalModel)

