from ..storage.score_storage import (
    increment_score,
    decrement_score
)

from ..utils.score import (
    user_can_use_emoji,
    score_updater
)

from ..utils.replies import (
    report_updated_score,
    user_cannot_use_emoji,
    cannot_update_score,
    something_wrong_happened,
    user_did_not_reply_on_valid_user
)

import logging


@score_updater
async def achieve_score(replied, user_id, chat_id, event):
    """
    add +1 score to replied user
    """

    try:
        user = increment_score(user_id, chat_id)

        if user:
            await report_updated_score(replied, user.score)

        else:
            await user_did_not_reply_on_valid_user(event)

    except Exception as error:
        logging.warning(error)
        await cannot_update_score(event)


@score_updater
async def lose_score(replied, user_id, chat_id, event):
    """
    add -1 score to replied user
    """

    try:
        user = decrement_score(user_id, chat_id)

        if user:
            await report_updated_score(replied, user.score)

        else:
            await user_did_not_reply_on_valid_user(event)


    except Exception as error:
        logging.warning(error)
        await cannot_update_score(event)


async def achieve_score_by_emoji(event):
    """
    Only super-users can use emoji to assign score to users
    """

    try:
        if user_can_use_emoji(event):
            await achieve_score(event)

        else:
            await user_cannot_use_emoji(event)

    except Exception as error:
        logging.warning(error)
        await something_wrong_happened(event)


async def lose_score_by_emoji(event):
    """
    Only super-users can use emoji to assign score to users
    """

    try:
        if user_can_use_emoji(event):
            await lose_score(event)

        else:
            await user_cannot_use_emoji(event)

    except Exception as error:
        logging.warning(error)
        await something_wrong_happened(event)
