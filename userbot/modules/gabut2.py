from time import sleep
from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import joo_cmd


@joo_cmd(pattern='joo(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`hi, nama gua joo`")
    sleep(3)
    await typew.edit("`16 tahun`")
    sleep(1)
    await typew.edit("`tinggal di bogor, salam kenal ngentod`")
# Create by myself @localheart


@joo_cmd(pattern='sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`cuma mau bilang`")
    sleep(3)
    await typew.edit("`aku sayang kamu`")
    sleep(1)
    await typew.edit("`i love u more than my selfπ₯°π€`")
# Create by myself @localheart


@joo_cmd(pattern='semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`apapun yang terjadi`")
    sleep(3)
    await typew.edit("`tetaplah bernapas`")
    sleep(1)
    await typew.edit("`karena tanpa bernapas kita akan mati`")
# Create by myself @localheart


CMD_HELP.update({
    "oi": f"πΎπ€π’π’ππ£π: `{cmd}joo`\
    \nβ³ : perkenalan joo\
    \n\nπΎπ€π’π’ππ£π: `{cmd}sayang`\
    \nβ³ : Gombalan maut`\
    \n\nπΎπ€π’π’ππ£π: `{cmd}semangat`\
    \nβ³ : Tetap Semangat."
})
