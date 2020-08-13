from .engine import Base, session
from sqlalchemy import Column, Integer
import logging


class UserScore(Base):
    __tablename__ = "score"

    def __init__(self, user_id, chat_id):
        super(UserScore, self).__init__()
        self.user_id = user_id
        self.chat_id = chat_id

    id = Column(Integer, primary_key=True)

    # each user has its own unique id which is immutable
    user_id = Column(Integer, nullable=False)

    # each user will have isolated score in each telegram's group
    # each telegram group will have it's own unique id
    chat_id = Column(Integer, nullable=False)

    score = Column(Integer, default=1)

    def __repr__(self):
        return f"user: {self.user_id} from chat {self.chat_id} with score {self.score}"


# if user doesn't exist, find_user() will get out of index because
# array = [] and function tries to get first item -> array[0]
# which will raise index error
UserDoesNotExist = IndexError
InvalidData = TypeError


def find_user(user_id, chat_id):
    return session.query(UserScore).filter(
        UserScore.user_id == user_id,
        UserScore.chat_id == chat_id
    ).all()[0]


def create_user(user_id, chat_id):
    """
    create user with default score of 1
    """
    try:
        user = UserScore(
            user_id=user_id,
            chat_id=chat_id
        )

        session.add(user)
        session.commit()

        return user

    except Exception as error:
        logging.warning(error)
        return


def increment_score(user_id, chat_id):
    """
    try to find user and increment score by 1,
    if user doesn't exit, make one (automatically set new user score to 1)
    """

    try:
        user = find_user(user_id, chat_id)
        user.score += 1
        session.add(user)
        session.commit()

        return user

    except UserDoesNotExist:

        # not null or None
        if user_id and chat_id:
            user = create_user(user_id, chat_id)
            return user

        else:
            return None


def decrement_score(user_id, chat_id):
    """
    try to find user and decrement score by -1,
    if user doesn't exit, make one (automatically set new user score to 1)
    """

    try:
        user = find_user(user_id, chat_id)

        # user score can't be less than 0
        if user.score <= 0:
            return user

        user.score -= 1
        session.add(user)
        session.commit()

        return user

    except UserDoesNotExist:

        # not null or None
        if user_id and chat_id:
            user = create_user(user_id, chat_id)
            return user

        else:
            return None
