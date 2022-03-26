# 🍀 © @tofik_dn
# ⚠️ Do not remove credits


from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP
from userbot.utils import joo_cmd
import random
from userbot import owner
from telethon.tl.types import InputMessagesFilterVideo


@joo_cmd(pattern="asupan$")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@AsupanKyyUserbot", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"ᴀsᴜᴘᴀɴ ʙʏ [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan video asupan.")

@joo_cmd(pattern="desah(?: |$)(.*)")
async def _(event):
    try:
        desahnya = [
            desah
            async for desah in event.client.iter_messages(
                "@punyakenkan", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(desahnya),
            caption=f"**Nih Lord Desahannya🤗** [{DEFAULTUSER}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak Bisa Menemukan Desahan.")
        
@joo_cmd(pattern="ayang(?: |$)(.*)")
async def _(event):
    try:
        ayangnya = [
            ayang
            async for ayang in event.client.iter_messages(
                "@CeweLogoPack", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ayangnya),
            caption=f"**Nih Cantiknya Aku** 🥰 [{DEFAULTUSER}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Gaada Yang Mau Sama Kamu Karena Kamu Jele🤪")

CMD_HELP.update(
    {
        "asupan": f"**Plugin : **`asupan`\
        \n\n  •  **Syntax :** `{cmd}asupan`\
        \n  •  **Function : **Untuk Mengirim Video Asupan Secara random.\
        \n\n  •  **Syntax :** `{cmd}desah`\
        \n  •  **Function : **Untuk Mengirim Suara Desah Buat Lu Yang Sange.\
        \n\n  •  **Syntax :** `{cmd}ayang`\
        \n  •  **Function : **Untuk Mencari Ayang Buat Cowok Yang Jomblo.\
    "
    }
)
