from telethon import Button

from userbot import BOTLOG, BOTLOG_CHATID, LOGS, tgbot


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/02f87cca391f9b9d627d5.jpg",
                caption="**š„·į“ĻĻ-į“Ńį“ŹŠ²ĻŃš„· Has Been Actived**!!\nāāāāāāāāāāāāāāā\nā  **Userbot Version** - 8.0@master\nāāāāāāāāāāāāāāā\nā  **Powered By:** @ProjectJoni ",
                buttons=[(Button.url("ź±į“į“į“į“Źį“", "https://t.me/JoniSupport"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
