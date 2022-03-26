from time import sleep

from userbot import CMD_HELP, CMD_HANDLER as cmd
from userbot.utils import edit_or_reply, joo_cmd


@joo_cmd(pattern='alfatihah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    xnxx = await edit_or_reply(typew, "**SURAT ALFATIHAH**")
    sleep(1)
    await xnxx.edit("**bismillāhir-raḥmānir-raḥīm**")
    sleep(1)
    await xnxx.edit("**al-ḥamdu lillāhi rabbil-'ālamīn**")
    sleep(1)
    await xnxx.edit("**ar-raḥmānir-raḥīm**")
    sleep(1)
    await xnxx.edit("**māliki yaumid-dīn**")
    sleep(1)
    await xnxx.edit("**iyyāka na'budu wa iyyāka nasta'īn**")
    sleep(1)
    await xnxx.edit("**ihdinaṣ-ṣirāṭal-mustaqīm**")
    sleep(1)
    await xnxx.edit("**ṣirāṭallażīna an'amta 'alaihim gairil-magḍụbi 'alaihim wa laḍ-ḍāllīn**")
    sleep(1)
    await xnxx.edit("**Amin..**")


@joo_cmd(pattern='ayatkursi(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await xnxx.edit("**Bismillahir'-rahmanir-rahim**")
    sleep(1)
    await xnxx.edit("**Allaahu Laailaaha illa huwal hayyul qayyuum**")
    sleep(1)
    await xnxx.edit("**Laa ta'khudzuhu sinatuw walaa nauum**")
    sleep(1)
    await xnxx.edit("**Lahuu maa fissamaawaati wamaa fil ardhi**")
    sleep(1)
    await xnxx.edit("**Mangdzalladzii yasyfa'u 'indahuu illai bi idznih**")
    sleep(1)
    await xnxx.edit("**Ya'lamu maa baina aiydiihim wamaa kholfahum**")
    sleep(1)
    await xnxx.edit("*walaa yukhiithuuna bisyayin min 'ilmihii illaa bimaa syaaa**")
    sleep(1)
    await xnxx.edit("**wasi'a kursiyyuhus samaawaati wal ardho**")
    sleep(1)
    await xnxx.edit("**Walaa yauduhuu khifdhuhumaa wa huwal'aliyyul 'adhiim**")
    sleep(1)
    await xnxx.edit("**Alhamdulillah..**")


# Create by myself @localheart


CMD_HELP.update({
    "surat":
    f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}alfatihah`\
    \n↳ : Surat Alfatihah."
})

CMD_HELP.update({
    "surat2":
    f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}ayatkursi`\
    \n↳ : Ayat Kursi."
})
