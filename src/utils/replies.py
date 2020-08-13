from .emoji import random_emoji


async def user_cannot_score_to_itself(event):
    await event.reply(
        "نمیتونی به خودت امتیاز بدی D:"
    )


async def report_updated_score(replied, score):
    await replied.reply(
        f"امتیاز شما: {score} {random_emoji()}"
    )


async def user_cannot_use_emoji(replier):
    await replier.reply(
        "فقط افراد خاص میتونن با ایموجی نمره بدن"
    )


async def something_wrong_happened(event):
    await event.reply("نمیتونم اینکارو انجام بدم, نمیدونم چرا")


async def cannot_update_score(event):
    await event.reply("نمیتونم امتیاز رو اپدیت کنم , نمیدونم چرا")


async def user_did_not_reply_on_valid_user(event):
    await event.reply("مطمینی روی کاربر ریپلای کردی؟")
