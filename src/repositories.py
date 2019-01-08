from typing import List

from src.database import master_async_session, read_replica_async_session
from src.models import GoalModel


class GoalRepository:

    @staticmethod
    def get(kwargs) -> List:
        with read_replica_async_session() as session:
            return session.query(GoalModel)

    @staticmethod
    def create(goal: GoalModel) -> None:
        with master_async_session() as session:
            session.add(goal)

    @staticmethod
    def update(goal: GoalModel) -> None:
        with master_async_session() as session:
            session.add(goal)

    @staticmethod
    def delete(goal_id) -> None:
        with master_async_session() as session:
            session.delete(GoalModel)
