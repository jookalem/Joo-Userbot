# @greyyvbss

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import joo_cmd
import random
from userbot import owner
from telethon.tl.types import InputMessagesFilterPhotos


@joo_cmd(pattern="ppcp$")
async def _(event):
    try:
        ayangnya = [
            ayang
            async for ayang in event.client.iter_messages(
                "@ppcpcilik", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ayangnya),
            caption=f" Nih kak PP Couple nya 🥰 [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("PPCP nya gaada karena lu jelek _-.")

   
CMD_HELP.update(
    {
        "ppcouple": f"**Plugin : **ppcouple\
        \n\n  •  **Syntax :** {cmd}ppcp\
        \n  •  **Function : **Untuk Mencari PP Couple secara random.\
    "
    }
)
