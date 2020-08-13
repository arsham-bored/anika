from .replies import (
    user_cannot_score_to_itself,
    something_wrong_happened
)

from . import (
    super_users,
    void
)

import logging


def score_updater(handler):
    """
    score_update takes a handler function which commit updates
    this decorator takes care of on exception which user tries to give score to themself
    also score_updater will extract necessary data from event object required for score update
    """

    async def wrapper(event):
        # user who replies to other's message
        replier_id = event.from_id

        if event.is_reply:
            # user who replier reply to it's message
            # replied by it's own is an Event object
            # replied.reply() will reply to replied user
            try:
                replied = await event.get_reply_message()

                replied_user_id = replied.from_id
                chat_id = replied.chat_id

                # users cannot give score to themselves
                if replier_id == replied_user_id:
                    # this will reply warn message
                    await user_cannot_score_to_itself(event)

                else:
                    # pass required data to update score
                    func = await handler(replied, replied_user_id, chat_id, event)
                    return func

            except Exception as error:

                logging.warning(error)
                await something_wrong_happened(event)
                # do nothing, return void, jobless function.
                return void

        return void

    return wrapper


def user_can_use_emoji(event):
    """
    check if user is in whitelist (user is superuser)
    """

    replier_id = event.from_id
    return True if replier_id in super_users else False
