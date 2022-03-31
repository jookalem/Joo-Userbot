from time import sleep

from userbot import CMD_HELP, CMD_HANDLER as cmd

from userbot.utils import edit_or_reply, joo_cmd

@joo_cmd(pattern='maaf(?: |$)(.*)')

async def typewriter(typew):

    typew.pattern_match.group(1)

    sleep(1)

    jo = await edit_or_reply(typew, "**Selamat Menyambut Bulan Suci Ramadhan**")

    sleep(1)

    await jo.edit("**Saya Memohon Maaf Sebesar Besarnya**")

    sleep(1)

    await jo.edit("**Apabila Saya Ada Salah**")

    sleep(1)

    await jo.edit("**Baik Yang Di Sengaja**")

    sleep(1)

    await jo.edit("**Ataupun Tidak Di Sengaja**")

    sleep(1)

    await jo.edit("**Apabila Pernah Kasar**")

    sleep(1)

    await jo.edit("**Apabila Pernah Menuduh**")

    sleep(1)

    await jo.edit("**Apabila Pernah Memfitnah**")

    sleep(1)

    await jo.edit("**Apabila Pernah Menghina**")

    sleep(1)

    await jo.edit("**Mohon Di Maafkan Sebesar Besarnya 😇**")

# Create by myself @ikhsanntarjo

@joo_cmd(pattern='nyemen(?: |$)(.*)')

async def typewriter(typew):

    typew.pattern_match.group(1)

    sleep(1)

    jo = await edit_or_reply(typew, "`jangan nyemen mulu`")

    sleep(1)

    await jo.edit("`nanti lu dapet dosa bro`")

    sleep(1)

    await jo.edit("`malu broo`")

    sleep(1)

    await jo.edit("`udah gede gabisa puasa full`")

    sleep(1)

    await jo.edit("`istighfar bro`")


# Create by myself @ikhsanntarjo

@joo_cmd(pattern='puasa(?: |$)(.*)')

async def typewriter(typew):

    typew.pattern_match.group(1)

    sleep(1)

    jo = await edit_or_reply(typew, "`semangat ya kak puasanya`")

    sleep(1)

    await jo.edit("`jangan tidur mulu`")

    sleep(1)

    await jo.edit("`nanti puasanya ga di terima`")

    sleep(1)

    await jo.edit("`jangan nonton bokep dulu ya kak`")

    sleep(1)

    await jo.edit("`nanti burungnya bangun:'v`")

    sleep(1)

    await jo.edit("`tahan ya kak colinya:v`")



# Create by myself @ikhsanntarjo

@joo_cmd(pattern='saur(?: |$)(.*)')

async def typewriter(typew):

    typew.pattern_match.group(1)

    sleep(1)

    jo = await edit_or_reply(typew, "`WOII SAURRR`")

    sleep(1)

    await jo.edit("`SAURR SAURRR`")

    sleep(1)

    await jo.edit("`SSAAUURR SSAAUURR`")

    sleep(1)

    await jo.edit("`AYOO KITA SAURR`")

    sleep(1)

    await jo.edit("`IBU IBU BAPA BAPA`")

    sleep(1)

    await jo.edit("`YOO KITA SAURRR SAURR`")

    sleep(1)

    await jo.edit("`ESOKNYA KITA AKAN BERPUASA`")

    sleep(1)

    await jo.edit("`BERPUASA MENDAPAT PAHALA`")

    sleep(1)

    await jo.edit("`TIDAK BERPUASA MENDAPATKAN DOSA`")

    sleep(1)

    await jo.edit("`SELAMAT SAUR SAYANG 🤗`")

# Create by myself @ikhsanntarjo

@joo_cmd(pattern="imsak(?: |$)(.*)")

async def typewriter(typew):

    typew.pattern_match.group(1)

    sleep(1)

    jo = await edit_or_reply(typew, "**IMSAKKK**")

    sleep(1.5)

    await jo.edit("**WOI IMSAKKK..**")

    sleep(1.5)

    await jo.edit("**MAKAN MULU ETTDAH**")

    sleep(1.5)

    await jo.edit("**MINUM DULU BRO**")

    sleep(1.5)

    await jo.edit("**BIAR SIANG GA HAUS**")

    sleep(1.5)

    await jo.edit("**KALO PERLU SEGALON**")

    sleep(1.5)

    await jo.edit("**BIAR LU GA LEMES**")

    sleep(1.5)

    await jo.edit("**AWOKAWOKAWOK**")

    sleep(1.5)

    await jo.edit("**KALO UDAH MINUM*")

    sleep(1.5)

    await jo.edit("**JANGAN LUPA NIAT PUASA YA KAK<3**")

    sleep(1.5)

    await jo.edit("**SEMANGAT YA KAK 🤗**")

    sleep(1.5)

CMD_HELP.update({

    "puasa": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}nyemen`\

    \n↳ : Cobain aja\

    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}maaf`\

    \n↳ : Cobain aja\

    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}puasa`\

    \n↳ : Cobain aja\

    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}saur`\

    \n↳ : Cobain aja\

    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{cmd}imsak`\

    \n↳ : Cobain aja."

})
