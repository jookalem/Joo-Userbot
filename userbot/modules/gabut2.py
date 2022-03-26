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
    await typew.edit("`i love u more than my self🥰🤍`")
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
    "oi": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}joo`\
    \n↳ : perkenalan joo\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}sayang`\
    \n↳ : Gombalan maut`\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}semangat`\
    \n↳ : Tetap Semangat."
})
