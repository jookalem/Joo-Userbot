from userbot import owner, CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import joo_cmd


@joo_cmd(pattern="p(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`assalamualaikum ngentod`")
# Salam


@joo_cmd(pattern="l(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`waalaikumsalam ngentod`")
# Menjawab Salam


@joo_cmd(pattern="istigfar(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit("`astaghfirullah ngentod`")
# Istigfar


@joo_cmd(pattern="perkenalan(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`hi anak ngentod, kenalin nama gua {owner}`")
    sleep(2)
    await event.edit(f"`gua tinggal di {WEATHER_DEFCITY}`")
    sleep(2)
    await event.edit("`salam kenal ya...`")
    sleep(2)
    await event.edit("`senang bertemu denganmu`")
# Perkenalan


CMD_HELP.update({
    "gabut": f"**Modules** - `Gabut`\
    \n\n Cmd : `{cmd}l`\
    \nUsage : Untuk Menjawab Salam\
    \n\n Cmd : `{cmd}perkenalan`\
    \nUsage : Memperkenalkan Diri\
    \n\n Cmd : `{cmd}p`\
    \nUsage : Untuk Memberi Salam."
})
