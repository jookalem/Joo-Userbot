# Credits @renprx
# FROM https://randi356.github.io/Vegeta-Userbot

""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

import random
import time


from datetime import datetime

from userbot import (
    DEVS, 
    StartTime,
)
    
from userbot.events import register

# CPING

cping = [
    "**Hadir, Pingers** `101.678` ",
    "**Hadir Speed** `999.999` ",
    "**Hadir, Boosted** `567.765` ",
    "**Hadir, Pingers Power** `789.212` ",
]

brb = [
    "**Sial Lord Joo!😈** ",
    "**Siap Lord!🙏** ",
    "**See U Next Time Lord!🤗** ",
]

afk = [
    "**Laporan Di Terima Lord!👿**! ",
    "**Baik Lord**!🙏 ",
    "**Fuck You Joo!🤪** ",
]

async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 50
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(incoming=True, from_users=DEVS, pattern=r"^.cping$")
async def _(joo):
    await joo.reply(random.choice(cping))
    

@register(incoming=True, from_users=DEVS, pattern=r"^brb$")
async def _(joo):
    await joo.reply(random.choice(brb))
                      
@register(incoming=True, from_users=DEVS, pattern=r"^afk$")
async def _(joo):
    await joo.reply(random.choice(afk))
