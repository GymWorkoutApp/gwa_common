from typing import List

from src.database import async_session
from src.models import GoalModel


class GoalRepository:

    @staticmethod
    def get(kwargs) -> List:
        with async_session() as session:
            return session.query(GoalModel)

    @staticmethod
    def create(goal: GoalModel) -> GoalModel:
        with async_session() as session:
            session.save(goal)
            session.commit()

    @staticmethod
    def update(goal: GoalModel) -> GoalModel:
        with async_session() as session:
            session.save(goal)
            session.commit()

    @staticmethod
    def delete(goal_id) -> List:
        with async_session() as session:
            session.delete(GoalModel)
            session.commit()
