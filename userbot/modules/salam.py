from platform import uname
from userbot import ALIVE_NAME, CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import joo_cmd

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@joo_cmd(pattern='^P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐀𝐬𝐬𝐚𝐥𝐚𝐦𝐮'𝐚𝐥𝐚𝐢𝐤𝐮𝐦...")


@joo_cmd(pattern='atg(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐀𝐬𝐭𝐚𝐠𝐡𝐟𝐢𝐫𝐮𝐥𝐥𝐚𝐡....")


@joo_cmd(pattern='^L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐖𝐚'𝐚𝐥𝐚𝐢𝐤𝐮𝐦𝐬𝐚𝐥𝐚𝐦...")


@joo_cmd(pattern='ast(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐀𝐬𝐭𝐚𝐠𝐡𝐟𝐢𝐫𝐮𝐥𝐥𝐚𝐡 𝐀𝐧𝐚𝐤 𝐍𝐠𝐞𝐧𝐭𝐨𝐭...")


CMD_HELP.update({
    "salam":
    "P\
\nUsage: Untuk Memberi salam.\
\n\nL\
\nUsage: Untuk Menjawab Salam."
})


CMD_HELP.update({
    "salam2":
    f"{cmd}atg\
\nUsage: Istighfar 1.\
\n\n{cmd}ast\
\nUsage: Istighfaf 2."
})
