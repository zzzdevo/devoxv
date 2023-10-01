import asyncio
import random
import time
import requests
import re
import sys
import json
import aiohttp
from pyrogram.types import *
from pyrogram import *
from pyrogram import Client, filters
from random import  choice, randint
from telegraph import upload_file
from asyncio import gather
from pyrogram.errors import FloodWait
from pyrogram.enums import ParseMode, ChatMemberStatus


api_id = 12962251 # Here Api Id
api_hash = "b51499523800add51e4530c6f552dbc8" # Here Api Hash
bot_token = "6050538180:AAEtIs6uWoHqI1V5t2qFi6YX23Hcb71XFRs" # Here Bot Token
app = Client("iiu", api_id=api_id,api_hash=api_hash, bot_token=bot_token)

OWNER_ID = "833360381"


@app.on_message(
    command(["فەرمان"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/bd98a0645138a96e63b23.jpg",
        caption=f"""**[⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - فەرمانی بۆتی گۆرانی🧑🏻‍💻🖤](t.me/MGIMT)**\n**••┉┉┉┉┉┉••🝢••┉┉┉┉┉┉••**\n
**⎙ بۆ پەخشکردن :(gorani,play,پلەی) + ناوی گۆرانی **
**⎙ بۆ وەستاندنی کاتی پەخشکردن :(وەستانی کاتی,وسبە,pause) **
**⎙ بۆ دەستپێکردنەوەی پەخشکردن :(دەستپێکردنەوە,د,resume) **      
**⎙ بۆ کۆتایی هێنان بە پەخشکردن :(end,stop,ڕاگرتن,وەستان) **  
**⎙ بۆ تێپەڕاندنی گۆرانی بۆ گۆرانی دواتر :(skip,تێپەڕاندن,دواتر)**
**⎙ بۆ دەرکردنی یاریدەدەر :(left,جێهێشتن,پەیوەندیەکان جێبهێڵە)**
**⎙ فەرمانە کوردیەکانی بۆت :(فەرمان)**
**⎙ بۆ داگرتنی گۆرانی :(گۆرانی,ڤیدیۆ,میوزیک,vsong)**
**⎙ بۆ گەڕان بە دوای هەر شتێك کەتۆ بتەوێت :(گەڕان) **
\n••┉┉┉┉┉••🝢••┉┉┉┉┉••""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𐇮 ﮼ﺣ‌ّــەمــە 🇧🇷 𐇮", url=f"https://t.me/IQ7amo"),
                ], [
                InlineKeyboardButton(
                    "𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌", url=f"t.me/MGIMT"),
            ],

            ]

        ),

    )


@app.on_message(
    command(["گۆرانی"])
)
async def music(client: Client, message: Message):
    rl = random.randint(1, 29)
    url = f"https://t.me/ZWZZ7/{rl}"
    await client.send_voice(message.chat.id, url,
                            caption="**[⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - 🧑🏻‍💻🖤 گۆرانی](t.me/MGIMT)**\n\n**••┉┉┉┉┉••🝢••┉┉┉┉┉••**\n**¦  گۆرانییەکانم➧♥️**\n**@IQMUC - کەناڵی گۆرانی**",
                            parse_mode=enums.ParseMode.MARKDOWN,
                            reply_markup=InlineKeyboardMarkup(
                                [
                                    [
                                        InlineKeyboardButton(
                                            message.from_user.first_name,
                                            url=f"https://t.me/{message.from_user.username}")
                                    ],
                                ]
                            )
                            )


@app.on_message(command(["وێنە", "وێنەکان"]))
async def ihd(client: Client, message: Message):
    rs = random.randint(1, 148)
    url = f"https://t.me/GTTUTY/{rs}"
    await client.send_photo(message.chat.id, url,
                            caption="**[⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - 🧑🏻‍💻🖤 وێنەکان](t.me/MGIMT)**\n**••┉┉┉┉┉••🝢••┉┉┉┉┉••**\n\n**¦ وێنەکە دیاریکرا ♥•**",
                            parse_mode=enums.ParseMode.MARKDOWN,
                            reply_markup=InlineKeyboardMarkup(
                                [
                                    [
                                        InlineKeyboardButton(
                                            message.from_user.first_name,
                                            url=f"https://t.me/{message.from_user.username}")
                                    ],
                                ]
                            )
                            )


@app.on_message(command(["وێنەی کچان", "کچان"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(1, 45)
    url = f"https://t.me/ZSZZW/{rl}"
    await client.send_photo(message.chat.id, url,
                            caption="**[⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - 🧑🏻‍💻🖤 کچان](t.me/MGIMT)**\n**••┉┉┉┉┉••🝢••┉┉┉┉┉••**\n\n**¦ وێنەی کچان➧♥️\n@ZSZZW - کەناڵی وێنە**",
                            parse_mode=enums.ParseMode.MARKDOWN,
                            reply_markup=InlineKeyboardMarkup(
                                [
                                    [
                                        InlineKeyboardButton(
                                            message.from_user.first_name,
                                            url=f"https://t.me/{message.from_user.username}")
                                    ],
                                ]
                            )
                            )


@app.on_message(
    command(["ق"])
)
async def voice(client: Client, message: Message):
    rl = random.randint(1, 102)
    url = f"https://t.me/IQQUR/{rl}"
    await client.send_voice(message.chat.id, url,
                            caption="**[⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - 🧑🏻‍💻🖤 قورئان](t.me/MGIMT)**\n**••┉┉┉┉┉••🝢••┉┉┉┉┉••**\n\n**¦ قورئانی پیرۆز➧♥️\n@IQQUR - کەناڵی قورئان**",
                            parse_mode=enums.ParseMode.MARKDOWN,
                            reply_markup=InlineKeyboardMarkup(
                                [
                                    [
                                        InlineKeyboardButton(
                                            message.from_user.first_name,
                                            url=f"https://t.me/{message.from_user.username}")
                                    ],
                                ]
                            )
                            )


@app.on_message(command([f"ڤیدیۆ", "v", "ڤ"])
                )
async def video(client: Client, message: Message):
    rl = random.randint(5, 32)
    u = await client.get_messages("IQVIDE", rl)
    if u.video:
        await client.send_video(message.chat.id, u.video.file_id,
                                caption="**[⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - 🧑🏻‍💻🖤 ڤیدیۆ](t.me/MGIMT)**\n**••┉┉┉┉┉••🝢••┉┉┉┉┉••**\n\n**¦ @xv7amo - کەناڵی ڤیدیۆ♥️•**",
                                parse_mode=enums.ParseMode.MARKDOWN,
                                reply_markup=InlineKeyboardMarkup(
                                    [
                                        [
                                            InlineKeyboardButton(
                                                message.from_user.first_name,
                                                url=f"https://t.me/{message.from_user.username}")
                                        ],
                                    ]
                                )
                                )

        @app.on_message(
            command(["/source", "سەرچاوە", "سۆرس", "گەشەپێدەران"])
        )
        async def huhh(client: Client, message: Message):
            await message.reply_photo(
                photo=f"https://graph.org/file/b4ace5c5aec2901efed59.jpg",
                caption=f"""**[ᯓ 𝗦𝗢𝗨𝗥𝗖𝞝 𝙄𝙌 - 🧑🏻‍💻🖤 گەشەپێدەران](t.me/MGIMT)**\n••┉┉┉┉┉••🝢••┉┉┉┉┉••\n**بەخێربێی ئەزیزم{message.from_user.mention} بۆ بەشی گەشەپێدەرانی بۆت🕷️•**\n**بۆ هەبوونی هەرکێشە و پرسیارێك پەیوەندی بە گەشەپێدەر بکە لەڕێگای دووگمەکانی خوارەوە♥•**""",
                parse_mode=enums.ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "᳒ᯓ محمد ✬", url=f"https://t.me/IQ7amo"),
                        ], [

                        InlineKeyboardButton(
                            "𐇮 ﮼ﺣ‌ّــەمــە 🇧🇷 𐇮", url=f"https://t.me/VTVIT"),
                    ], [

                        InlineKeyboardButton(
                            "⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌", url=f"https://t.me/MGIMT"),

                    ], [

                        InlineKeyboardButton(
                            "『𓏺کەناڵی سەرەکی』", url=f"https://t.me/xv7amo"),
                    ],

                    ]

                ),

            )

        @app.on_message(
            command(["حەمە", "@VTVIT", "گەشەپێدەر"])

        )
        async def yas(client, message):
            usr = await client.get_chat("VTVIT")
            name = usr.first_name
            photo = await app.download_media(usr.photo.big_file_id)
            await message.reply_photo(photo,
                                      caption=f"**[ᯓ 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - سەرچاوەی زیرەك 🧑🏻‍💻](t.me/MGIMT)**\n**زانیاری گەشەپێدەری دووەمی بۆت**\n↜︙Dev 𝐍𝐀𝐌𝐄 ↬:{name}\n↜︙Dev 𝐔𝐒𝐄𝐑 ↬ :@{usr.username}\n↜︙Dev 𝐈𝐃 ↬ :{usr.id}\n↜︙Dev 𝐁𝐈𝐎 ↬: {usr.bio}",
                                      parse_mode=enums.ParseMode.MARKDOWN,
                                      reply_markup=InlineKeyboardMarkup(
                                          [
                                              [
                                                  InlineKeyboardButton(
                                                      name, url=f"https://t.me/{usr.username}")
                                              ],
                                          ]
                                      ),
                                      )

        @app.on_message(
            command(["پڕۆگرامساز"])

        )
        async def yas(client, message):
            usr = await client.get_chat("IQ7amo")
            name = usr.first_name
            photo = await app.download_media(usr.photo.big_file_id)
            await message.reply_photo(photo,
                                      caption=f"**[ᯓ 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - سەرچاوەی زیرەك 🧑🏻‍💻](t.me/MGIMT)**\n**زانیاری پڕۆگرامسازی سەرچاوە**\n↜︙Dev 𝐍𝐀𝐌𝐄 ↬:{name}\n↜︙Dev 𝐔𝐒𝐄𝐑 ↬ :@{usr.username}\n↜︙Dev 𝐈𝐃 ↬ :{usr.id}\n↜︙Dev 𝐁𝐈𝐎 ↬: {usr.bio}",
                                      parse_mode=enums.ParseMode.MARKDOWN,
                                      reply_markup=InlineKeyboardMarkup(
                                          [
                                              [
                                                  InlineKeyboardButton(
                                                      name, url=f"https://t.me/{usr.username}")
                                              ], [
                                              InlineKeyboardButton(
                                                  "🝢 پەیوەندی کردن 🝢", url=f"https://t.me/{usr.username}"),
                                          ],
                                          ]
                                      ),
                                      )

        @app.on_message(
            command(["سەرۆک", "@IQ7amo"])

        )
        async def yas(client, message):
            usr = await client.get_chat("IQ7amo")
            name = usr.first_name
            photo = await app.download_media(usr.photo.big_file_id)
            await message.reply_photo(photo,
                                      caption=f"**[ᯓ 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - سەرچاوەی زیرەك 🧑🏻‍💻](t.me/MGIMT)**\n**زانیاری خاوەنی بۆت**\n↜︙Dev 𝐍𝐀𝐌𝐄 ↬:{name}\n↜︙Dev 𝐔𝐒𝐄𝐑 ↬ :@{usr.username}\n↜︙Dev 𝐈𝐃 ↬ :{usr.id}\n↜︙Dev 𝐁𝐈𝐎 ↬: {usr.bio} ",
                                      parse_mode=enums.ParseMode.MARKDOWN,
                                      reply_markup=InlineKeyboardMarkup(
                                          [
                                              [
                                                  InlineKeyboardButton(
                                                      name, url=f"https://t.me/{usr.username}")
                                              ], [
                                              InlineKeyboardButton(
                                                  "🝢 پەیوەندی کردن 🝢", url=f"https://t.me/{usr.username}"),
                                          ],
                                              [
                                                  InlineKeyboardButton(
                                                      "کەناڵی گەشەپێدەر", url=f"https://t.me/{SUPPORT_CHANNEL}"),
                                              ],
                                          ]
                                      ),
                                      )

        @app.on_message(
            command(["کەناڵ", "کەنال"])

        )
        async def yas(client, message):
            usr = await client.get_chat("MGIMT")
            photo = await app.download_media(usr.photo.big_file_id)
            await message.reply_photo(photo,
                                      caption=f"**[⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - کەناڵی سەرچاوە 🧑🏻‍💻](t.me/MGIMT)**\n**جۆینی کەناڵی بۆت بکە بۆ بینینی بابەتی جیاوازتر♥**\n\n** بەستەری کەناڵ :\nhttps://t.me/{usr.username}**",
                                      parse_mode=enums.ParseMode.MARKDOWN,
                                      reply_markup=InlineKeyboardMarkup(
                                          [
                                              [
                                                  InlineKeyboardButton(
                                                      "𝗦𝗢𝗨𝗥𝗖𝞝 𝙄𝙌 - سەرچاوەی زیرەك", url=f"https://t.me/{usr.username}")
                                              ],
                                          ]
                                      ),
                                      )

        @app.on_message(
            command(["زیرەکی دەستکرد"])

        )
        async def huhh(client: Client, message: Message):
            await message.reply_photo(
                photo=f"https://telegra.ph/file/7713aee1676f475d4ed21.jpg",
                caption=f"""**[⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - زیرەکی دەستکرد🧑🏻‍💻🖤](t.me/MGIMT)**\n\n**بەخێربێی ئەزیزم {message.from_user.mention} بۆ بەشی زیرەکی دەستکرد تایبەت بە سەرچاوەی زیرەك**\n** بۆ بەکارهێنانی بنووسە : iq + پرسیارەکەت ♥⚡**""",
                parse_mode=enums.ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "﮼محمد˹َّّ", url=f"https://t.me/IQ7amo"),
                        ], [

                        InlineKeyboardButton(
                            "⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌", url=f"https://t.me/MGIMT"),
                    ],

                    ]

                ),

            )

        @app.on_message(
            command(["قورئان"])

        )
        async def huhh(client: Client, message: Message):
            await message.reply_photo(
                photo=f"https://telegra.ph/file/78cefd067cff33d79edb7.jpg",
                caption=f"""**[⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - پەخشی قورئان🧑🏻‍💻🖤](t.me/MGIMT)**\n\n**بەخێربێی ئەزیزم {message.from_user.mention} بۆ بەشی پەخشکردنی قورئانی پیرۆز تایبەت بە سەرچاوەی زیرەك**\n** بۆ پەخشکردنی بنووسە : سوڕەتی یان سوڕەت + ناوی سوڕەت ♥⚡**""",
                parse_mode=enums.ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "﮼محمد˹َّّ", url=f"https://t.me/IQ7amo"),
                        ], [

                        InlineKeyboardButton(
                            "⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌", url=f"https://t.me/MGIMT"),
                    ],

                    ]

                ),

            )


@app.on_message(
    command(["ف1"])
 )
async def mmmezat(client, message):
        await message.reply_text(f"""**⧉ 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - فەرمانی بۆت🧑🏻‍💻🖤**\n••┉┉┉┉┉┉••🝢••┉┉┉┉┉┉••\n\n**بەخێربێی ئەزیزم {message.from_user.mention} بۆ بەشی داخستن و کردنەوەی فەرمان {MUSIC_BOT_NAME}**\n\n
** کردنەوەی + فەرمان 👾✅**

** ئایدی | وێنە **

** وەڵامدانەوە | ستیکەر **

      **زکر**

⩹⊶⊷⌯⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 •⧉⊶⊷⋗

** داخستنی + فەرمان 👾❎**

** ئایدی | وێنە **

** وەڵامدانەوە | ستیکەر **

      **زکر**

**نموونە : کردنەوەی ئایدی یان داخستنی ئایدی♥🧩**

**نموونە : کردنەوەی زکر یان داخستنی زکر♥🧩**

**@IQ7amo - 🖤👾باشترین بۆتی گۆرانی و پاراستن و وەڵامدانەوە**
**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 ", url=f"https://t.me/MGIMT"),
                 ],[
                InlineKeyboardButton(
                        "پڕۆگرامساز⚡", url=f"https://t.me/IQ7amo"),
               ],
          ]
        ),
    )



        GAME_MESSAGE = "**[⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - 🧑🏻‍💻 یاری](t.me/MGIMT)**\n**••┉┉┉┉┉••🝢••┉┉┉┉┉••**\n\n**👾¦ بەخێربێی ئەزیزم**\n**👾¦ بۆ بەشی یاری سەرچاوەی زیرەك**\n\n**⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌**"
        GAME_BUTTONS = [
            [
                InlineKeyboardButton('߷ یاریەکان ߷', callback_data='GAME1'),
            ], [
                InlineKeyboardButton('⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌', url=f"https://t.me/MGIMT")
            ], [
                InlineKeyboardButton(
                    "⟲ گـەڕانـەوە ⟳", callback_data="close"),
            ],
        ]

        nmla = []

        @app.on_message(command("رفع نمله"))
        async def rf3nmla(client, message):
            if not message.reply_to_message.from_user.mention in nmla:
                nmla.append(message.reply_to_message.from_user.mention)
            await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n نمله 😂♥️")

        @app.on_message(command("تنزيل نمله"))
        async def tnzelnmla(client, message):
            if message.reply_to_message.from_user.mention in nmla:
                nmla.remove(message.reply_to_message.from_user.mention)
            await message.reply_text(
                f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n نمله 😂♥️")

        @app.on_message(command("المرفوعين نمل"))
        async def nml(client, message):
            nq = ""
            for n in nmla:
                nq += n + "\n"
            await message.reply_text(nq)

        @app.on_message(command("رفع صرصار"))
        async def rf3srsar(client, message):
            await message.reply_text(
                f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n صرصار 😂♥️")

        @app.on_message(command("تنزيل صرصار"))
        async def tnzelsrar(client, message):
            await message.reply_text(
                f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n صرصار 😂♥️")

        @app.on_message(command("رفع رقاصه"))
        async def yasooo(client, message):
            await message.reply_text(
                f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n رقاصه حد يرمي فلوس عليها 😂💃")

        @app.on_message(command("تنزيل رقاصه"))
        async def yaso(client, message):
            await message.reply_text(
                f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n رقاصه تابت😂😔")

        @app.on_message(command("رفع متناك"))
        async def bjoiuyjk(client, message):
            await message.reply_text(
                f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n متناك حد يركبو 😂♥️")

        @app.on_message(command("تنزيل متناك"))
        async def kamal(client, message):
            await message.reply_text(
                f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n متناك اعرث تاب 😂♥️")

        @app.on_message(command("رفع نجس"))
        async def fdsa(client, message):
            await message.reply_text(
                f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n نجس بنجاح  😂♥️")

        @app.on_message(command("تنزيل نجس"))
        async def kophvc(client, message):
            await message.reply_text(
                f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n النجس استحمي 😂♥️")

        @app.on_message(command("رفع عره"))
        async def roky(client, message):
            await message.reply_text(
                f"تم رفع العض\n🗿 \n√و : {message.reply_to_message.from_user.mention}\n\n عره عالمجتمع 😂♥️")

        @app.on_message(command("تنزيل عره"))
        async def zerso(client, message):
            await message.reply_text(
                f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n عره خلاص 😂♥️")

        @app.on_message(command("رفع بقره"))
        async def vvvtyy(client, message):
            await message.reply_text(
                f"تم رفع العض\n🗿 \n√و : {message.reply_to_message.from_user.mention}\n\n بقا بقر حديحلبو 🐄🤭")

        @app.on_message(command("تنزيل بقره"))
        async def tttryuh(client, message):
            await message.reply_text(
                f"تم تنزيل العض\n🗿 \n√و : {message.reply_to_message.from_user.mention}\n\n خلاص خلص لبن 😂")

        @app.on_message(command("رفع قرد"))
        async def uiipppl(client, message):
            await message.reply_text(
                f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n قرد حد يديلو موزه 😂🐒")

        @app.on_message(command("تنزيل قرد"))
        async def bjhupq(client, message):
            await message.reply_text(
                f"تم تنزيل العض\n🗿 \n√و : {message.reply_to_message.from_user.mention}\n\n القرد بقا انسان🙊🧍")

        @app.on_message(command("رفع قلبي"))
        async def pooiejh(client, message):
            await message.reply_text(
                f"تم رفع العض\n🗿 \n√و : {message.reply_to_message.from_user.mention}\n\n خلاص بقيت قلبو 😂♥️")

        @app.on_message(command("تنزيل قلبي"))
        async def ttrqew(client, message):
            await message.reply_text(
                f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\nمبقتش قلبوو 😭💔")

        @app.on_message(command("رفع خدام"))
        async def qyui(client, message):
            await message.reply_text(
                f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n خدام تع خدم ع البار    😂🤓")

        @app.on_message(command("تنزيل خدام"))
        async def klhj(client, message):
            await message.reply_text(
                f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n الخدام ساب الشغل  😢🚶")

        @app.on_message(command("رفع معرص"))
        async def wqew(client, message):
            await message.reply_text(
                f"تم رفع العض\n🗿 \n√و : {message.reply_to_message.from_user.mention}\n\n معرص البار  😂🤓")

        @app.on_message(command("تنزيل معرص"))
        async def ohho(client, message):
            await message.reply_text(
                f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n المعرص بقا راجل   😂🧔")

        @app.on_message(command("رفع ارمله"))
        async def drsss(client, message):
            await message.reply_text(
                f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n  بقيتي ارمله وجوزك مات 🥹")

        @app.on_message(command("تنزيل ارمله"))
        async def gkvdr(client, message):
            await message.reply_text(
                f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n خلاث متبقيش قموصه جوزك عايش اهو 😂🫶🏻")

        @app.on_message(command("رفع مزه"))
        async def cgfyu6f(client, message):
            await message.reply_text(
                f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n يمزه خدي بالك من نفسك 🥹❤️")

        @app.on_message(command("تنزيل مزه"))
        async def hhhhug(client, message):
            await message.reply_text(
                f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n انتي صدقتي انك مزه ولا اي انا كنت بطبل 😂😝")

        @app.on_message(command("رفع ابني"))
        async def cbky(client, message):
            await message.reply_text(
                f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n  بقيت ابنو وكل حياتو🥹🖤")

        @app.on_message(command("تنزيل ابني"))
        async def ccgy(client, message):
            await message.reply_text(
                f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n حتي عيلتك مش طيقاك ورموك في الشارع ")

        @app.on_message(command("رفع خاينه"))
        async def mkloo(client, message):
            await message.reply_text(
                f"تم رفع العض\n🗿 \n√و : {message.reply_to_message.from_user.mention}\n\n  ي خاينه ي مهزأه ")

        @app.on_message(command("تنزيل خاينه"))
        async def fkijbh(client, message):
            await message.reply_text(
                f"تم تنزيل العض\n🗿 \n√و : {message.reply_to_message.from_user.mention}\n\n مين الاهبل للي كان مفكر القمر دا ممكن يبقي خاين 🥹🥹💕")

        @app.on_message(command("رفع بنتي"))
        async def yuhhss(client, message):
            await message.reply_text(
                f"تم رفع العض\n🗿 \n√و : {message.reply_to_message.from_user.mention}\n\n بقيتي بنتي وحته من قلبي 🥹❤️❤️❤️")

        @app.on_message(command("تنزيل بنتي"))
        async def hloih(client, message):
            await message.reply_text(
                f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\nكنت بهزر انا مخلفتش لسه🤡😂  ")

        @app.on_message(command("رفع خاين"))
        async def kloss(client, message):
            await message.reply_text(
                f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n خنتها كام مره قول متتكسفش يخاين")

        @app.on_message(command("تنزيل خاين"))
        async def fiihug(client, message):
            await message.reply_text(
                f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n ايدا طلع سوء تفاهم انت اشرف من الشرف يسالك😂❤️")

        @app.on_message(command("رفع خول"))
        async def dadr(client, message):
            await message.reply_text(
                f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n 😂 خول طول عمرك مش اول مره")

        @app.on_message(command("تنزيل خول"))
        async def hjj7gv(client, message):
            await message.reply_text(
                f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n  اهو يعم نزلتك 🙂💕")

        @app.on_message(command("رفع حمار"))
        async def cgfyu6f(client, message):
            await message.reply_text(
                f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n خلاص بقت حمار رسمي نظمي😹")

        @app.on_message(command("تنزيل حمار"))
        async def cxxv(client, message):
            await message.reply_text(
                f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n خلاث يعم كنا بنهزر معاك متبقاش قفوش 😂😝")

        @app.on_message(command("رفع غبي"))
        async def polkij(client, message):
            await message.reply_text(
                f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n غبي و هتفضل غبي😹🤞")

        @app.on_message(command("تنزيل غبي"))
        async def nbvcc(client, message):
            await message.reply_text(
                f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n غبي و بقي بيفهم😹🫶")

        @app.on_message(command("رفع مراتي"))
        async def ttttuhyp(client, message):
            await message.reply_text(
                f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n مراتك خد و عملو واحد😹😽")

        @app.on_message(command("تنزيل مراتي"))
        async def xxxxt(client, message):
            await message.reply_text(
                f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n طلقتها شوف غيرها 😂😝")

        @app.on_message(command("رفع زبال"))
        async def oooph(client, message):
            await message.reply_text(
                f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n زبال تع  نضف الجروب😹")

        @app.on_message(command("تنزيل زبال"))
        async def zzzas(client, message):
            await message.reply_text(
                f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n زبال تعب و استقال 😂😝")

        @app.on_message(command("رفع خدامه"))
        async def ggggop(client, message):
            await message.reply_text(
                f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n خدامه تع اغسلي رجلي 😹🤞")

        @app.on_message(command("تنزيل خدامه"))
        async def vvvuu(client, message):
            await message.reply_text(
                f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\nخدامه نزلت اجازه😹🫶")

        @app.on_message(command("رفع كلبه"))
        async def mmmuy(client, message):
            await message.reply_text(
                f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n كلبه خدي عضمه😹🤞")

        @app.on_message(command("تنزيل كلبه"))
        async def dfrewq(client, message):
            await message.reply_text(
                f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n خلاث كلبه تحولت الانسان😿😹")

        @app.on_message(command("رفع طيز"))
        async def ssoss(client, message):
            await message.reply_text(
                f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n طيز و كبيره كمان😹🤞")

        @app.on_message(command("تنزيل طيز"))
        async def nobo(client, message):
            await message.reply_text(
                f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n طيز متزعلش نزلتك😹🫶")

        @app.on_message(command("رفع حرامي"))
        async def llok(client, message):
            await message.reply_text(
                f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n حرامي وهبلغ عنه😹🚓")

        @app.on_message(command("تنزيل حرامي"))
        async def kaompj(client, message):
            await message.reply_text(
                f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n حرامي ربنا تاب عليه😂😔")

        @app.on_message(
            command(["یاری", "game"])

        )
        async def zohary(client: Client, message: Message):
            await message.reply_photo(
                photo=f"https://telegra.ph/file/ccd73a1b8fe26a88b404a.jpg",
                caption=f"""**[⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - 🧑🏻‍💻 یاری](t.me/MGIMT)**\n**••┉┉┉┉┉••🝢••┉┉┉┉┉••**\n\n**👾¦ بەخێربێی ئەزیزم**\n**👾¦ بۆ بەشی یاری سەرچاوەی زیرەك**\n\n**⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌**""",
                reply_markup=InlineKeyboardMarkup(GAME_BUTTONS)
            )

        @app.on_callback_query()
        async def callback_query(client, CallbackQuery):
            if CallbackQuery.data == "GAME1":

                GAME1_MESSAGE = "**[⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - 🧑🏻‍💻 یاری](t.me/MGIMT)**\n**••┉┉┉┉┉••🝢••┉┉┉┉┉••**\n\n**👾¦ بەخێربێی ئەزیزم**\n**👾¦ بۆ بەشی یاری سەرچاوەی زیرەك**\n**👾¦ یەکێك لەمانەی خوارەوە دابگرە**"

                GAME1_BUTTONS = [
                    [
                        InlineKeyboardButton(
                            "°باڵندە°", url=f"http://t.me/awesomebot?game=FlappyBird"),
                        InlineKeyboardButton(
                            "°گۆڕینی ئەستێرە°", url=f"http://t.me/gamee?game=Switchy"),
                    ], [
                        InlineKeyboardButton(
                            "°ماتۆڕ°", url=f"http://t.me/gamee?game=motofx"),
                        InlineKeyboardButton(
                            "°تەقەکردن بە ئاگر°", url=f"http://t.me/gamee?game=NeonBlaster"),
                    ], [
                        InlineKeyboardButton(
                            "°تۆپی پێ°", url=f"http://t.me/gamee?game=Footballstar"),
                        InlineKeyboardButton(
                            "°کۆکردنەوەی ڕەنگ°", url=f"http://t.me/awesomebot?game=Hextris"),
                    ], [
                        InlineKeyboardButton(
                            "°ئەڵماسەکان°", url=f"http://t.me/gamee?game=DiamondRows"),
                        InlineKeyboardButton(
                            "°لێدانی تۆپ°", url=f"http://t.me/gamee?game=KeepitUP"),
                    ], [
                        InlineKeyboardButton(
                            "°پاڵەوانێتی شکاندن°", url=f"http://t.me/gamee?game=SmashRoyale"),
                        InlineKeyboardButton(
                            "°2048°", url=f"http://t.me/awesomebot?game=g2048"),
                    ], [
                        InlineKeyboardButton(
                            "°باسکت بۆڵ°", url=f"http://t.me/gamee?game=BasketBoy"),
                        InlineKeyboardButton(
                            "°پشیلە°", url=f"http://t.me/gamee?game=CrazyCat"),
                    ], [
                        InlineKeyboardButton(
                            "⟲ گـەڕانـەوە ⟳", callback_data='GAME')
                    ],
                ]

                await CallbackQuery.edit_message_text(
                    GAME1_MESSAGE,
                    reply_markup=InlineKeyboardMarkup(GAME1_BUTTONS)
                )
            elif CallbackQuery.data == "GAME":

                RETURN_GAME = "**[⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌 - 🧑🏻‍💻 یاری](t.me/MGIMT)**\n**••┉┉┉┉┉••🝢••┉┉┉┉┉••**\n\n**👾¦ بەخێربێی ئەزیزم**\n**👾¦ بۆ بەشی یاری سەرچاوەی زیرەك**\n**👾¦ یەکێك لەمانەی خوارەوە دابگرە**"

                RETURN_BUTTON = [
                    [
                        InlineKeyboardButton('߷ یاریەکان ߷', callback_data='GAME1'),
                    ], [
                        InlineKeyboardButton('⧉• 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝙌', url=f"https://t.me/MGIMT")
                    ], [
                        InlineKeyboardButton(
                            "⟲ گـەڕانـەوە ⟳", callback_data="close"),
                    ],
                ]

                await CallbackQuery.edit_message_text(
                    RETURN_GAME,
                    reply_markup=InlineKeyboardMarkup(RETURN_BUTTON)
                )
            elif CallbackQuery.data == "GAME2":

                SOURCE_GAME = "🐰\n\n العاب ارنوب\nكت\nتويت\nاسال\nصراحه\nانا مين\nبايو\nمين في الكول\nسورس\nزخرفه\nاذكار\nانصحني\nكتبات\nافلام\nغنيلي\nرفع\nذكاء\nنكته\nكشف\nايدي\nميديا\nتحويل ملصق\n🐰."

                SORGAM_BUTTON = [
                    [
                        InlineKeyboardButton('⌞ ᥉᥆υᖇᥴᥱ ᥲ️ᖇꪀ᥆ρ⌝', url=f"https://t.me/mgimt")
                    ], [
                        InlineKeyboardButton('𝗁᥆ꪔᥱ', callback_data='GAME')
                    ]
                ]
                await CallbackQuery.edit_message_text(
                    SOURCE_GAME,
                    reply_markup=InlineKeyboardMarkup(SORGAM_BUTTON)
                )


url = 'https://us-central1-chat-for-chatgpt.cloudfunctions.net/basicUserRequestBeta'

def gpt(text) -> None:
    headers = {
        'Host': 'us-central1-chat-for-chatgpt.cloudfunctions.net',
        'Connection': 'keep-alive',
        'If-None-Match': 'W/"1c3-Up2QpuBs2+QUjJl/C9nteIBUa00"',
        'Accept': '*/*',
        'User-Agent': 'com.tappz.aichat/1.2.2 iPhone/15.6.1 hw/iPhone8_2',
        'Content-Type': 'application/json',
        'Accept-Language': 'en-GB,en;q=0.9'
    }

    data = {
        'data': {
            'message':text,
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    try:
        result = response.json()["result"]["choices"][0]["text"]
        return result
    except:
        return None

def reply_gpt(client, message:Message):
    text = message.text.split("iq")[1]
    reply_text = gpt(text)
    chat_id = message.chat.id
    if message.reply_to_message is not None:
        message_id = message.reply_to_message.id
    else:
        message_id = None
    client.send_message(chat_id=chat_id, text=reply_text + "<b>\n\n\n@IQ7amo نوێترین ڤێرژنی زیرەکی دەستکرد لەلایەن گەشەپێدەر</b>", reply_to_message_id=message_id)

@app.on_message(command("iq"))
def reply(client, message:Message):
    message.reply_text(f"<b>•⎆┊ بەخێربێیت ئەزیزم {message.from_user.mention}\n\nبۆ بەکارهێنانی ئەم فەرمانە فەرمان بنووسە لەگەڵئەو  پرسیارەکەی دەتەوێت♥·</b>")
    reply_gpt(client, message)


    @app.on_message(command(["بەستەر", "/link", "لینک", "لینك"]) & ~filters.bot & ~filters.private)
    async def invitelink(client, message):
        chid = message.chat.id
        try:
            invitelink = await client.export_chat_invite_link(chid)
        except:
            return await message.reply_text("**سەرەتا بمکە ئەدمین**", parse_mode=enums.ParseMode.MARKDOWN)
        await message.reply_text(f"**بە سەرکەوتوویی بەستەری گرووپ دروست کرا :**\n\n ``{invitelink}`")

        @app.on_message(command(["سەرۆکی گرووپ"]) & filters.group)
        async def gak_owne(client: Client, message: Message):
            if len(message.command) >= 2:
                return
            else:
                chat_id = message.chat.id

                async for member in client.get_chat_members(chat_id):
                    if member.status == ChatMemberStatus.OWNER:
                        id = member.user.id
                        key = InlineKeyboardMarkup([[InlineKeyboardButton(member.user.first_name, user_id=id)]])
                        m = await client.get_chat(id)
                        if m.photo:
                            photo = await app.download_media(m.photo.big_file_id)
                            return await message.reply_photo(photo,
                                                             caption=f"**✧ ¦زانیاری خاوەن گرووپ \n\n ✧ ¦ ناو ← {m.first_name} \n ✧ ¦ یوزەر ← @{m.username} \n ✧ ¦ بایۆ ← {m.bio}**", reply_markup=key)
                        else:
                            return await message.reply("•" + member.user.mention)

        @app.on_message(command(["گرووپ", "group"]) & filters.group)
        async def ginnj(client: Client, message: Message):
            chat_idd = message.chat.id
            chat_name = message.chat.title
            chat_username = f"@{message.chat.username}"
            photo = await client.download_media(message.chat.photo.big_file_id)
            await message.reply_photo(photo=photo,
                                      caption=f"""**🦩 ¦ ꪀᥲ️ꪔᥱ » {chat_name}\n🐉 ¦ Ꭵժ ᘜᖇ᥆υρ »  -{chat_idd}\n🐊 ¦ ᥣᎥꪀk » {chat_username}**""",
                                      reply_markup=InlineKeyboardMarkup(
                                          [
                                              [
                                                  InlineKeyboardButton(
                                                      chat_name, url=f"https://t.me/{message.chat.username}")
                                              ],
                                          ]
                                      ),
                                      )

        @app.on_message(command(["گۆڕین", "گۆڕینی ستیکەر"]))
        async def sticker_image(client: Client, message: Message):
            reply = message.reply_to_message
            if not reply:
                return await message.reply("**ڕپلەی ستیکەر بکە**")
            if not reply.sticker:
                return await message.reply("**ڕپلەی ستیکەر بکە**")
            m = await message.reply("**کەمێك چاوەڕێبە . .**")
            f = await reply.download(f"{reply.sticker.file_unique_id}.png")
            await gather(*[message.reply_photo(f), message.reply_document(f)])
            await m.delete()
            os.remove(f)

        @app.on_message(command(["ناوم", "ناو"]) & filters.group)
        async def vgdg(client: Client, message: Message):
            await message.reply_text(
                f"""•⎆┊** ناوت 🔥♥**»»  {message.from_user.mention()}""")

        array = []

        @app.on_message(command(["@all", "بانگکردن", "تاگ"]) & ~filters.private)
        async def nummmm(client: app, message):
            global rotba, photo
            if message.chat.id in array:
                return await message.reply_text(
                    f"•⎆┊**تاگکردن دەستی پێکرد♥**\n\n** لەلایەن ← ✧ ¦{message.from_user.mention}•**")
            dev = (OWNER_ID)
            haya = (1818734394, 833360381)
            get = await client.get_chat_member(message.chat.id, message.from_user.id)
            if message.from_user.id in haya:
                rotba = "پڕۆگرامساز"
            elif message.from_user.id in dev:
                rotba = "گەشەپێدەر"
            elif get.status in [ChatMemberStatus.OWNER]:
                rotba = "سەرۆك"
            elif get.status in [ChatMemberStatus.ADMINISTRATOR]:
                rotba = "ئەدمین"
            chek = await client.get_chat_member(message.chat.id, message.from_user.id)
            if not chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
                await message.reply(f"•⎆┊**ببورە تۆ ئەدمین نیت🗿 {message.from_user.mention}•**",
                                    parse_mode=enums.ParseMode.MARKDOWN)
                return
            await message.reply_text(
                f"•⎆┊**تاگکردن دەستی پێکرد♥🪐** \n\n** لەلایەن ← {rotba}✧ ¦{message.from_user.mention} **\n\n**بۆ کۆتایی هێنانی تاگ بنووسە وەستانی تاگ یان /cancel ♥🧩•**",
                parse_mode=enums.ParseMode.MARKDOWN)
            i = 0
            txt = ""
            zz = message.text
            if message.photo:
                photo_id = message.photo.file_id
                photo = await client.download_media(photo_id)
                zz = message.caption
            try:
                zz = zz.replace("@all", "").replace("تاگ", "").replace("وەرن", "")
            except:
                pass
            array.append(message.chat.id)
            async for x in client.get_chat_members(message.chat.id):
                if message.chat.id not in array:
                    return
                if not x.user.is_deleted:
                    i += 1
                    txt += f" {x.user.mention} ،"
                    if i == 5:
                        try:
                            if not message.photo:
                                await client.send_message(message.chat.id, f"{zz}\n{txt}")
                            else:
                                await client.send_photo(message.chat.id, photo=photo, caption=f"{zz}\n{txt}")
                            i = 0
                            txt = ""
                            await asyncio.sleep(2)
                        except FloodWait as e:
                            flood_time = int(e.x)
                            if flood_time > 200:
                                continue
                            await asyncio.sleep(flood_time)
                        except Exception:
                            array.remove(message.chat.id)
            array.remove(message.chat.id)

        @app.on_message(command(["وەستانی تاگ", "/cancel", "ڕاگرتنی تاگ"]))
        async def stop(client, message):
            global rotba
            dev = (OWNER_ID)
            haya = (833360381, 1818734394)
            get = await client.get_chat_member(message.chat.id, message.from_user.id)
            if get.status in [ChatMemberStatus.ADMINISTRATOR]:
                rotba = "ئەدمین"
            elif get.status in [ChatMemberStatus.OWNER]:
                rotba = "سەرۆك"
            elif message.from_user.id in haya:
                rotba = "پڕۆگرامساز"
            elif message.from_user.id in dev:
                rotba = "گەشەپێدەر"
            chek = await client.get_chat_member(message.chat.id, message.from_user.id)
            if not chek.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
                await message.reply(f"•⎆┊**ببورە تۆ ئەدمین نیت🗿 {message.from_user.mention}•**",
                                    parse_mode=enums.ParseMode.MARKDOWN)
                return
            if message.chat.id not in array:
                await message.reply(f"•⎆┊**تاگکردن وەستاوە ئەزیزم♥ {message.from_user.mention}•**",
                                    parse_mode=enums.ParseMode.MARKDOWN)
                return
            if message.chat.id in array:
                array.remove(message.chat.id)
                await message.reply(
                    f"•⎆┊**تاگکردن وەستێنرا **\n\n **لەلایەن ← {rotba}✧ ¦{message.from_user.mention}•**",
                    parse_mode=enums.ParseMode.MARKDOWN)
                return

            @app.on_message(command(["تێلەگراف", "telegraph"]))
            async def get_link_group(client, message):
                global local_path
                try:
                    text = await message.reply("•⎆┊**دروست دەکرێت ..**", parse_mode=enums.ParseMode.MARKDOWN)

                    async def progress(current, total):
                        await text.edit_text(f"•⎆┊**میدیا دروست کرا🕷  ... **{current * 100 / total:.1f}%",
                                             parse_mode=enums.ParseMode.MARKDOWN)

                    try:
                        location = f"./media/group/"
                        local_path = await message.reply_to_message.download(location, progress=progress)
                        await text.edit_text("•⎆┊**بەستەری میدیا لە هێناندایە ..🕷️•**",
                                             parse_mode=enums.ParseMode.MARKDOWN)
                        upload_path = upload_file(local_path)
                        await text.edit_text(f"•⎆┊**  𝒕𝒆𝒍𝒆 𝒍𝒊𝒏𝒌 **:\n\n<code>https://telegra.ph{upload_path[0]}</code>",
                                             parse_mode=enums.ParseMode.MARKDOWN)
                        os.remove(local_path)
                    except Exception as e:
                        await text.edit_text(f"•⎆┊**فایلەکە شکستی هێنا♥•**\n\n**هۆکار**: {e} ",
                                             parse_mode=enums.ParseMode.MARKDOWN)
                        os.remove(local_path)
                        return
                except Exception:
                    pass


dev = (OWNER_ID)

txt = [
    "<b>هەردەم پێبکەنە ♥️😻</b>",

    "😂😂😂😂😂😂😂",

    "<b>پیبکانا پیبکانە هەر دەم بە زەردەخەنە 😂😂</b>",

]
txt1 = [

    "<b>بمێنی گەشەپێدەر♥️😻</b>",

    "<b>هەموو کات زەردەخەنە😂😂</b>",

    "<b>احح لەو پیکنینە 😂😂</b>",

]


# noinspection PyTypeChecker
@app.on_message(command(["ههه", "😂😂", "😂😂😂", "😂🤣", "ههههههههههههههههههه", "😂😂😂😂😂😂"]))
async def cutt(client: Client, message: Message):
    dev = (OWNER_ID)
    if message.from_user.id in dev:

        b = random.choice(txt1)

        await message.reply(

            f"{b}")
    else:
        a = random.choice(txt)

        await message.reply(

            f"{a}")


iddof = []


@app.on_message(
    command(["داخستنی وەڵامدانەوە"])
    & filters.group

)
async def iddlock(client: Client, message: Message):
    dev = (OWNER_ID)

    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if message.from_user.id in dev:
        rotba = "پڕۆگرامساز"
    if get.status in [ChatMemberStatus.OWNER]:
        rotba = "سەرۆك"
    if get.status in [ChatMemberStatus.ADMINISTRATOR]:
        rotba = "ئەدمین"
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and dev:
        if message.chat.id in iddof:
            return await message.reply_text(f"<b> {message.from_user.mention}\n وەڵامدانەوە پێشتر داخراوە♥️❎•</b>")
        iddof.append(message.chat.id)
        return await message.reply_text(
            f"<b> بە سەرکەوتوویی فەرمانی وەڵامدانەوە داخرا\n\n لەلایەن {rotba} ←{message.from_user.mention}♥️❎•</b>")
    else:
        return await message.reply_text(f"<b> {message.from_user.mention} تۆ ئەدمین نیت لێرە💔•</b>")

@app.on_message(
    command(["کردنەوەی وەڵامدانەوە"])
    & filters.group
)
async def idljjopen(client: Client, message: Message):
    dev = (OWNER_ID)

    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if message.from_user.id in dev:
        rotba = "پڕۆگرامساز"
    if get.status in [ChatMemberStatus.OWNER]:
        rotba = "سەرۆك"
    if get.status in [ChatMemberStatus.ADMINISTRATOR]:
        rotba = "ئەدمین"
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and dev:
        if not message.chat.id in iddof:
            return await message.reply_text(f"<b> {message.from_user.mention}\n وەڵامدانەوە پێشتر کراوەتەوە♥️✅•</b>")
        iddof.remove(message.chat.id)
        return await message.reply_text(
            f"<b> بە سەرکەوتوویی فەرمانی وەڵامدانەوە کرایەوە\n\n لەلایەن {rotba} ←{message.from_user.mention}♥️✅•</b>")
    else:
        return await message.reply_text(f"<b> {message.from_user.mention} تۆ ئەدمین نیت لێرە💔•</b>")


# noinspection PyTypeChecker
@app.on_message(command(['وتە']))
def call_random_member(client: Client, message: Message):
    chat_id = message.chat.id
    members = [
        member for member in client.get_chat_members(chat_id)
        if not member.user.is_bot
    ]
    if chat_id in iddof:
        return
    random_member = random.choice(members)
    random_member_mention = f"[{random_member.user.first_name}](tg://user?id={random_member.user.id})"
    random_message = random.choice([
        f"<b>-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\nپێویستە سێ جار هەوڵبدەیت پێش ئەوەی نائومێدبیت🖤•</b>",
        f"<b>-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\nهەموو ڕۆژێك هەلێك بدە، بۆ ئەوەی ببێتە باشترین ڕۆژی ژیانت🖤•</b>",
        f"<b>-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\nدانایی دەزانێت کەی کەسەکان پشتگوێ بخەیت🖤•</b>",
        f"<b>-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\nئارامگرتن کلیلی قفڵێکی بەهێزە🖤•</b>",
        f"<b>-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\nتۆ بەرپرسیاریت لەوەی کە هەست بەچی دەکەیت، بەڵام تۆ بەرپرس نیت لەوەی ئەوانی تر دەیکەن🖤•</b>",
        f"<b>-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\nئەگەر بەو شێوەیە ناژیت کە دەتەوێت، دەبێت بیگۆڕیت🖤•</b>",
        f"<b>-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\nبراوەکان نھێنی ڕاهێنانیان باس ناکەن ئەوان بەرەو ئامانجی گەورە دەڕۆن🖤•</b>",
        f"<b>-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\nهیچ شتێک لە ژیاندا لە خۆشەویستی و بەختەوەری باشتر نییە🖤•</b>",
        f"<b>-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\nکاتێك با دەگۆڕێت، پێویستە ئاڕاستەی دەریاکە ڕێکبخەین لەجیاتی ئەوەی گەشت بوەستێنین🖤•</b>",
        f"<b>-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\nژیان وەك شەپۆل وایە، تۆ تەنها پێویستە هاوسەنگی خۆت بدۆزیتەوە بۆ ئەوەی نوقم نەبیت🖤•</b>",
        f"<b>-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\nئەو درەختەی کە لە بادا چەماوەتەوە، ئەو درەختەیە کە لە زریاندا دەشکێت🖤•</b>",
        f"<b>-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\n ئاواتی من ئەوەیە کە گۆشەی مەترسیداری تێدابێت هیچ شتێك ناتوانێت بەبێ بەرەنگاربوونەوە گەشەبکات🖤•</b>",
        f"<b>-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\nناتوانیت تاریکی لەبیربکەیت پێویستە مۆمێك دروست بکەیت🖤•</b>",
        f"<b>-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\nدووری تامێکی هەیە کە لە ئازارەوە دێت بۆ ئەو کەسەی کە لە خۆشەویستیدا نەدۆڕاوە🖤•</b>",
        f"<b>-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\nشتەکان لەسەر بنەمای تێپەڕبوونی بە باروودۆخ دیاری ناکرێت بەڵکو لەسەر بنەمای وەڵامەکانی ئەو باروودۆخە دیاری دەکرێت🖤•</b>",
        f"<b>-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\nهەڵبژاردن، لە کۆتاییدا، ڕێگایەک کە لە بەرژەوەندی تۆدا نەبوو ڕێگای تر بەجێبھێڵە کە نەدۆزراوەتەوە🖤•</b>",
        f"<b>-ئەم وتەیە بۆتۆیە♥•\n│ بـۆ {random_member_mention}\nهیچ شتێکی باشت نەبوو بۆ ئەوەی بیڵێیت، بۆیە بێدەنگ بە🖤•</b>"
    ])
    client.send_message(chat_id, random_message, reply_to_message_id=message.id)


@app.on_message(command(['وەسف', 'و']))
def call_random_member(client: Client, message: Message):
    chat_id = message.chat.id
    members = [
        member for member in client.get_chat_members(chat_id)
        if not member.user.is_bot
    ]
    if chat_id in iddof:
        return
    random_member = random.choice(members)
    random_member_mention = f"[{random_member.user.first_name}](tg://user?id={random_member.user.id})"
    random_message = random.choice([
        f"<b>لە مانڴ جوانتریت{random_member_mention}🌚🖤•**",
        f"<b>جوانی تۆ بەهیچ شێوازێك باس ناکرێت{random_member_mention}⚡♥•</b>",
        f"<b>خۆشەویستی لە دڵی هەموواندا{random_member_mention}🍭💞•</b>",
        f"<b>دەڵێی هەنگوینی وەرە با بتخۆم{random_member_mention}😂♥•</b>",
        f"<b>شار بە جوانی تۆ سەرسامبوو{random_member_mention}🙊🥰•</b>",
        f"<b>دانشە خوئری{random_member_mention}😂🤭•</b>",
        f"دەڵێی فیلی<b>{random_member_mention}😔😂•</b>",
        f"افف کە قشتی کئان<b>{random_member_mention}💘•</b>",
        f"<b>بڕەك کەلامزی بخۆ با قورس بیت{random_member_mention}🥰😂😂•</b>",
        f"<b>زۆڕ ناشڕینیی {random_member_mention}😂😳•</b>"
    ])
    client.send_message(chat_id, random_message, reply_to_message_id=message.id)

    @app.on_message(command("ز"))
    async def zahrafa(c: Client, m: Message):
        text_list = m.text.split(None, 1)
        if len(text_list) < 2:
            await m.reply_text("<b>◍ هەڵەیە دووبارە هەوڵبدەوە\n\nبەم شێوازە بینووسە : `ز محمد` √</b>",
                               reply_to_message_id=m.id)
            return
        text = text_list[1].split(None, 1)[1] if len(text_list[1].split()) > 1 else text_list[1]
        if len(text) > 20:
            await m.reply_text("<b>◍ ناتوانم زیاتر لە 𝟐𝟎 پیت دروست بکەم، دووبارە هەوڵبدەوە\n√</b>",
                               reply_to_message_id=m.id)
            return

        # هنا يتم تنفيذ زخرفة النص

        else:
            if re.match("\n", str(m.text)):
                await m.reply_text("<b>◍ ناتوانم دەقێك بڕازێنمەوە ئەگەر دوو دێڕ بێت\n√</b>", reply_to_message_id=m.id)
                return
        EmojeS = [
            ' 𓁻',
            ' 𓏴  ',
            ' 𓏶 ',
            ' 𓏡',
            ' 𓏢',
            ' 𓏣',
            ' ☽‘',
            ' 𖠱☂',
            '◑',
            ' ◌“',
            ' ★℡',
            ' ☆'
        ]
        Emoje = [
            ' ♕',
            ' 𖤍',
            '˛𖤓',
            '✾ ☫',
            ' ♫ ',
            ' ❈ ',
            ' ➽',
            ' ✺',
            '  ⚘',
            ' 𖤐',
            ' ❣',
            ' ❿  '
        ]

        zhrf = re.sub('ض', 'ضِٰـِۢ', text)
        zhrf = re.sub('ص', 'صِٰـِۢ', zhrf)
        zhrf = re.sub('ث', 'ثِٰـِۢ', zhrf)
        zhrf = re.sub('ق', 'قِٰـِۢ', zhrf)
        zhrf = re.sub('ف', 'فِٰ͒ـِۢ', zhrf)
        zhrf = re.sub('غ', 'غِٰـِۢ', zhrf)
        zhrf = re.sub('ع', 'عِٰـِۢ', zhrf)
        zhrf = re.sub('خ', 'خِٰ̐ـِۢ', zhrf)
        zhrf = re.sub('ح', 'حِٰـِۢ', zhrf)
        zhrf = re.sub('ج', 'جِٰـِۢ', zhrf)
        zhrf = re.sub('ش', 'شِٰـِۢ', zhrf)
        zhrf = re.sub('س', 'سِٰـِۢ', zhrf)
        zhrf = re.sub('ي', 'يِٰـِۢ', zhrf)
        zhrf = re.sub('ب', 'بِٰـِۢ', zhrf)
        zhrf = re.sub('ل', 'لِٰـِۢ', zhrf)
        zhrf = re.sub('ا', 'آ', zhrf)
        zhrf = re.sub('ت', 'تِٰـِۢ', zhrf)
        zhrf = re.sub('ن', 'نِٰـِۢ', zhrf)
        zhrf = re.sub('م', 'مِٰـِۢ', zhrf)
        zhrf = re.sub('ك', 'ڪِٰـِۢ', zhrf)
        zhrf = re.sub('ط', 'طِٰـِۢ', zhrf)
        zhrf = re.sub('ظ', 'ظِٰـِۢ', zhrf)
        zhrf = re.sub('ء', 'ء', zhrf)
        zhrf = re.sub('ؤ', 'ؤ', zhrf)
        zhrf = re.sub('ر', 'ر', zhrf)
        zhrf = re.sub('ى', 'ى', zhrf)
        zhrf = re.sub('ز', 'ز', zhrf)
        zhrf = re.sub('و', 'ﯛ̲୭', zhrf)
        zhrf = re.sub('ه', 'ۿۿہ', zhrf)
        zhrf = re.sub('a', '𝗮', zhrf)
        zhrf = re.sub('A', '𝗔', zhrf)
        zhrf = re.sub("b", "𝗯", zhrf)
        zhrf = re.sub("B", "𝗕", zhrf)
        zhrf = re.sub("c", "𝗰", zhrf)
        zhrf = re.sub("C", "𝗖", zhrf)
        zhrf = re.sub("d", "𝗱", zhrf)
        zhrf = re.sub("D", "𝗗", zhrf)
        zhrf = re.sub("e", "𝗲", zhrf)
        zhrf = re.sub("E", "𝗘", zhrf)
        zhrf = re.sub("f", "𝗳", zhrf)
        zhrf = re.sub("F", "𝗙", zhrf)
        zhrf = re.sub("g", "𝗴", zhrf)
        zhrf = re.sub("G", "𝗚", zhrf)
        zhrf = re.sub("h", "𝗵", zhrf)
        zhrf = re.sub("H", "𝗛", zhrf)
        zhrf = re.sub("i", "𝗹", zhrf)
        zhrf = re.sub("I", "𝗜", zhrf)
        zhrf = re.sub("j", "𝗝", zhrf)
        zhrf = re.sub("J", "𝗝", zhrf)
        zhrf = re.sub("k", "𝗸", zhrf)
        zhrf = re.sub("K", "𝗞", zhrf)
        zhrf = re.sub("l", "𝗹", zhrf)
        zhrf = re.sub("L", "𝗟", zhrf)
        zhrf = re.sub("m", "𝗺", zhrf)
        zhrf = re.sub("M", "𝗠", zhrf)
        zhrf = re.sub("n", "𝗻", zhrf)
        zhrf = re.sub("N", "𝗡", zhrf)
        zhrf = re.sub("o", "𝗼", zhrf)
        zhrf = re.sub("O", "𝗢", zhrf)
        zhrf = re.sub("p", "𝗽", zhrf)
        zhrf = re.sub("P", "𝗣", zhrf)
        zhrf = re.sub("q", "𝗾", zhrf)
        zhrf = re.sub("Q", "𝗤", zhrf)
        zhrf = re.sub("r", "𝗿", zhrf)
        zhrf = re.sub("R", "𝗥", zhrf)
        zhrf = re.sub("s", "𝘀", zhrf)
        zhrf = re.sub("S", "𝗦", zhrf)
        zhrf = re.sub("t", "𝘁", zhrf)
        zhrf = re.sub("T", "𝗧", zhrf)
        zhrf = re.sub("u", "𝘂", zhrf)
        zhrf = re.sub("U", "𝗨", zhrf)
        zhrf = re.sub("v", "𝘃", zhrf)
        zhrf = re.sub("V", "𝗩", zhrf)
        zhrf = re.sub("w", "𝘄", zhrf)
        zhrf = re.sub("W", "𝗪", zhrf)
        zhrf = re.sub("x", "𝘅", zhrf)
        zhrf = re.sub("X", "𝗫", zhrf)
        zhrf = re.sub("y", "𝘆", zhrf)
        zhrf = re.sub("Y", "𝗬", zhrf)
        zhrf = re.sub("z", "𝘇", zhrf)
        zhrf = re.sub("Z", "𝗭", zhrf)

        zhrf2 = re.sub('ض', 'ضَٰـُـٰٓ', m.text)
        zhrf2 = re.sub('ص', 'صَٰـُـٰٓ', zhrf2)
        zhrf2 = re.sub('ث', 'ثَٰـُـٰٓ', zhrf2)
        zhrf2 = re.sub('ق', 'قَٰـُـٰٓ', zhrf2)
        zhrf2 = re.sub('ف', 'فَٰ͒ـُـٰٓ', zhrf2)
        zhrf2 = re.sub('غ', 'غَٰـُـٰٓ', zhrf2)
        zhrf2 = re.sub('ع', 'عَٰـُـٰٓ', zhrf2)
        zhrf2 = re.sub('خ', 'خَٰ̐ـُـٰٓ', zhrf2)
        zhrf2 = re.sub('ح', 'حَٰـُـٰٓ', zhrf2)
        zhrf2 = re.sub('ج', 'جَٰـُـٰٓ', zhrf2)
        zhrf2 = re.sub('ش', 'شَٰـُـٰٓ', zhrf2)
        zhrf2 = re.sub('س', 'سَٰـُـٰٓ', zhrf2)
        zhrf2 = re.sub('ي', 'يَٰـُـٰٓ', zhrf2)
        zhrf2 = re.sub('ب', 'بَٰـُـٰٓ', zhrf2)
        zhrf2 = re.sub('ل', 'لَٰـُـٰٓ', zhrf2)
        zhrf2 = re.sub('ا', 'آ', zhrf2)
        zhrf2 = re.sub('ت', 'تَٰـُـٰٓ', zhrf2)
        zhrf2 = re.sub('ن', 'نَٰـُـٰٓ', zhrf2)
        zhrf2 = re.sub('م', 'مَٰـُـٰٓ', zhrf2)
        zhrf2 = re.sub('ك', 'ڪَٰـُـٰٓ', zhrf2)
        zhrf2 = re.sub('ط', 'طَٰـُـٰٓ', zhrf2)
        zhrf2 = re.sub('ظ', 'ظَٰـُـٰٓ', zhrf2)
        zhrf2 = re.sub('ء', 'ء', zhrf2)
        zhrf2 = re.sub('ؤ', 'ؤ', zhrf2)
        zhrf2 = re.sub('ر', 'ر', zhrf2)
        zhrf2 = re.sub('ى', 'ى', zhrf2)
        zhrf2 = re.sub('ز', 'ز', zhrf2)
        zhrf2 = re.sub('و', 'ﯛ̲୭', zhrf2)
        zhrf2 = re.sub("ه", "ۿۿہ", zhrf2)
        zhrf2 = re.sub('a', "𝖆", zhrf2)
        zhrf2 = re.sub('A', "𝖆", zhrf2)
        zhrf2 = re.sub("b", "𝖇", zhrf2)
        zhrf2 = re.sub("B", "𝖇", zhrf2)
        zhrf2 = re.sub("c", "𝖈", zhrf2)
        zhrf2 = re.sub("C", "𝖈", zhrf2)
        zhrf2 = re.sub("d", "𝖉", zhrf2)
        zhrf2 = re.sub("D", "𝖉", zhrf2)
        zhrf2 = re.sub("e", "𝖊", zhrf2)
        zhrf2 = re.sub("E", "𝖊", zhrf2)
        zhrf2 = re.sub("f", "𝖋", zhrf2)
        zhrf2 = re.sub("F", "𝖋", zhrf2)
        zhrf2 = re.sub("g", "𝖌", zhrf2)
        zhrf2 = re.sub("G", "𝖌", zhrf2)
        zhrf2 = re.sub("h", "𝖍", zhrf2)
        zhrf2 = re.sub("H", "𝖍", zhrf2)
        zhrf2 = re.sub("i", "𝖎", zhrf2)
        zhrf2 = re.sub("I", "𝖎", zhrf2)
        zhrf2 = re.sub("j", "𝖏", zhrf2)
        zhrf2 = re.sub("J", "𝖏", zhrf2)
        zhrf2 = re.sub("k", "𝖐", zhrf2)
        zhrf2 = re.sub("K", "𝖐", zhrf2)
        zhrf2 = re.sub("l", "𝖑", zhrf2)
        zhrf2 = re.sub("L", "𝖑", zhrf2)
        zhrf2 = re.sub("m", "𝖒", zhrf2)
        zhrf2 = re.sub("M", "𝖒", zhrf2)
        zhrf2 = re.sub("n", "𝖓", zhrf2)
        zhrf2 = re.sub("N", "𝖓", zhrf2)
        zhrf2 = re.sub("o", "𝖔", zhrf2)
        zhrf2 = re.sub("O", "𝖔", zhrf2)
        zhrf2 = re.sub("p", "𝖕", zhrf2)
        zhrf2 = re.sub("P", "𝖕", zhrf2)
        zhrf2 = re.sub("q", "𝖖", zhrf2)
        zhrf2 = re.sub("Q", "𝖖", zhrf2)
        zhrf2 = re.sub("r", "𝖗", zhrf2)
        zhrf2 = re.sub("R", "𝖗", zhrf2)
        zhrf2 = re.sub("s", "𝖘", zhrf2)
        zhrf2 = re.sub("S", "𝖘", zhrf2)
        zhrf2 = re.sub("t", "𝖙", zhrf2)
        zhrf2 = re.sub("T", "𝖙", zhrf2)
        zhrf2 = re.sub("u", "𝖚", zhrf2)
        zhrf2 = re.sub("U", "𝖚", zhrf2)
        zhrf2 = re.sub("v", "𝖛", zhrf2)
        zhrf2 = re.sub("V", "𝖛", zhrf2)
        zhrf2 = re.sub("w", "𝖜", zhrf2)
        zhrf2 = re.sub("W", "𝖜", zhrf2)
        zhrf2 = re.sub("x", "𝖝", zhrf2)
        zhrf2 = re.sub("X", "𝖝", zhrf2)
        zhrf2 = re.sub("y", "𝖞", zhrf2)
        zhrf2 = re.sub("Y", "𝖞", zhrf2)
        zhrf2 = re.sub("z", "𝖟", zhrf2)
        zhrf2 = re.sub("Z", "𝖟", zhrf2)

        zhrf3 = re.sub('ض', 'ض', m.text)
        zhrf3 = re.sub('ص', 'ص', zhrf3)
        zhrf3 = re.sub('ث', 'ثہ', zhrf3)
        zhrf3 = re.sub('ق', 'ق', zhrf3)
        zhrf3 = re.sub('ف', 'فُہ', zhrf3)
        zhrf3 = re.sub('غ', 'غہ', zhrf3)
        zhrf3 = re.sub('ع', 'عہ', zhrf3)
        zhrf3 = re.sub('ه', 'هٰہٰٖ', zhrf3)
        zhrf3 = re.sub('خ', 'خہ', zhrf3)
        zhrf3 = re.sub('ح', 'حہ', zhrf3)
        zhrf3 = re.sub('ج', 'جہ', zhrf3)
        zhrf3 = re.sub('د', 'د', zhrf3)
        zhrf3 = re.sub('ذ', 'ذ', zhrf3)
        zhrf3 = re.sub('ش', 'شہ', zhrf3)
        zhrf3 = re.sub('س', 'سہ', zhrf3)
        zhrf3 = re.sub('ي', 'يہ', zhrf3)
        zhrf3 = re.sub('ب', 'بّ', zhrf3)
        zhrf3 = re.sub('ل', 'لہ', zhrf3)
        zhrf3 = re.sub('ا', 'ا', zhrf3)
        zhrf3 = re.sub('ت', 'تہ', zhrf3)
        zhrf3 = re.sub('ن', 'نٰہٰٖ', zhrf3)
        zhrf3 = re.sub('م', 'مٰہٰٖ', zhrf3)
        zhrf3 = re.sub('ك', 'كُہ', zhrf3)
        zhrf3 = re.sub('ط', 'طہ', zhrf3)
        zhrf3 = re.sub('ئ', 'ئ ْٰ', zhrf3)
        zhrf3 = re.sub('ء', 'ء', zhrf3)
        zhrf3 = re.sub('ؤ', 'ؤ', zhrf3)
        zhrf3 = re.sub('ر', 'رَ', zhrf3)
        zhrf3 = re.sub('لا', 'لہا', zhrf3)
        zhrf3 = re.sub('ى', 'ىْ', zhrf3)
        zhrf3 = re.sub('ة', 'ة', zhrf3)
        zhrf3 = re.sub('و', 'و', zhrf3)
        zhrf3 = re.sub('ز', 'ز', zhrf3)
        zhrf3 = re.sub('ظ', 'ظۗہٰٰ', zhrf3)
        zhrf3 = re.sub('q', '𝐪', zhrf3)
        zhrf3 = re.sub('Q', '𝐪', zhrf3)
        zhrf3 = re.sub('w', '𝐰', zhrf3)
        zhrf3 = re.sub('W', '𝐰', zhrf3)
        zhrf3 = re.sub('e', '𝐞', zhrf3)
        zhrf3 = re.sub('E', '𝐞', zhrf3)
        zhrf3 = re.sub('r', '𝐫', zhrf3)
        zhrf3 = re.sub('R', '𝐫', zhrf3)
        zhrf3 = re.sub('t', '𝐭', zhrf3)
        zhrf3 = re.sub('T', '𝐭', zhrf3)
        zhrf3 = re.sub('y', '𝐲', zhrf3)
        zhrf3 = re.sub('Y', '𝐲', zhrf3)
        zhrf3 = re.sub('u', '𝐮', zhrf3)
        zhrf3 = re.sub('i', '𝐢', zhrf3)
        zhrf3 = re.sub('o', '𝐨', zhrf3)
        zhrf3 = re.sub('p', '𝐩', zhrf3)
        zhrf3 = re.sub('a', '𝐚', zhrf3)
        zhrf3 = re.sub('s', '𝐬', zhrf3)
        zhrf3 = re.sub('d', '𝐝', zhrf3)
        zhrf3 = re.sub('f', '𝐟', zhrf3)
        zhrf3 = re.sub('g', '𝐠', zhrf3)
        zhrf3 = re.sub('h', '𝐡', zhrf3)
        zhrf3 = re.sub('j', '𝐣', zhrf3)
        zhrf3 = re.sub('k', '𝐤', zhrf3)
        zhrf3 = re.sub('U', '𝐮', zhrf3)
        zhrf3 = re.sub('I', '𝐢', zhrf3)
        zhrf3 = re.sub('O', '𝐨', zhrf3)
        zhrf3 = re.sub('P', '𝐩', zhrf3)
        zhrf3 = re.sub('A', '𝐚', zhrf3)
        zhrf3 = re.sub('S', '𝐬', zhrf3)
        zhrf3 = re.sub('D', '𝐝', zhrf3)
        zhrf3 = re.sub('F', '𝐟', zhrf3)
        zhrf3 = re.sub('G', '𝐠', zhrf3)
        zhrf3 = re.sub('H', '𝐡', zhrf3)
        zhrf3 = re.sub('J', '𝐣', zhrf3)
        zhrf3 = re.sub('K', '𝐤', zhrf3)
        zhrf3 = re.sub('L', '𝐥', zhrf3)
        zhrf3 = re.sub('l', '𝐥', zhrf3)
        zhrf3 = re.sub('z', '𝐳', zhrf3)
        zhrf3 = re.sub('Z', '𝐳', zhrf3)
        zhrf3 = re.sub('x', '𝐱', zhrf3)
        zhrf3 = re.sub('X', 'ẋ', zhrf3)
        zhrf3 = re.sub('c', '𝐜', zhrf3)
        zhrf3 = re.sub('C', '𝐜', zhrf3)
        zhrf3 = re.sub('v', '𝐯', zhrf3)
        zhrf3 = re.sub('V', '𝐯', zhrf3)
        zhrf3 = re.sub('b', '𝐛', zhrf3)
        zhrf3 = re.sub('B', '𝐛', zhrf3)
        zhrf3 = re.sub('n', '𝐧', zhrf3)
        zhrf3 = re.sub('N', '𝐧', zhrf3)
        zhrf3 = re.sub('m', '𝐦', zhrf3)
        zhrf3 = re.sub('M', '𝐦', zhrf3)

        zhrf4 = re.sub('ض', 'ضۜہٰٰ', m.text)
        zhrf4 = re.sub('ص', 'ضۜہٰٰ', zhrf4)
        zhrf4 = re.sub('ث', 'ثہٰٰ', zhrf4)
        zhrf4 = re.sub('ق', 'قྀ̲ہٰٰ', zhrf4)
        zhrf4 = re.sub('ف', 'ف͒ہٰٰ', zhrf4)
        zhrf4 = re.sub('غ', 'غہٰٰ', zhrf4)
        zhrf4 = re.sub('ع', 'عہٰٰ', zhrf4)
        zhrf4 = re.sub('ه', 'هٰہٰٖ', zhrf4)
        zhrf4 = re.sub('خ', 'خٰ̐ہ ', zhrf4)
        zhrf4 = re.sub('ح', 'حہٰٰ', zhrf4)
        zhrf4 = re.sub('ج', 'جـٰ̲ـہْۧ', zhrf4)
        zhrf4 = re.sub('د', 'دٰ', zhrf4)
        zhrf4 = re.sub('ذ', 'ذِٰ', zhrf4)
        zhrf4 = re.sub('ش', 'شِٰہٰٰ', zhrf4)
        zhrf4 = re.sub('س', 'سٰٓ', zhrf4)
        zhrf4 = re.sub('ي', 'يِٰہ', zhrf4)
        zhrf4 = re.sub('ب', 'بّہ', zhrf4)
        zhrf4 = re.sub('ل', 'لـٰ̲ـہ', zhrf4)
        zhrf4 = re.sub('ا', 'آ', zhrf4)
        zhrf4 = re.sub('ت', 'تَہَٰ', zhrf4)
        zhrf4 = re.sub('ن', 'نَِہ', zhrf4)
        zhrf4 = re.sub('م', 'مٰ̲ہ', zhrf4)
        zhrf4 = re.sub('ك', 'ڪٰྀہٰٰ', zhrf4)
        zhrf4 = re.sub('ط', 'طۨہٰٰ', zhrf4)
        zhrf4 = re.sub('ئ', 'ئ ْٰ', zhrf4)
        zhrf4 = re.sub('ء', 'ء', zhrf4)
        zhrf4 = re.sub('ؤ', 'ؤ', zhrf4)
        zhrf4 = re.sub('ر', 'رَ', zhrf4)
        zhrf4 = re.sub('لا', 'لہا', zhrf4)
        zhrf4 = re.sub('ى', 'ىْ', zhrf4)
        zhrf4 = re.sub('ة', 'ة', zhrf4)
        zhrf4 = re.sub('و', 'وِٰ', zhrf4)
        zhrf4 = re.sub('ز', 'زَٰ', zhrf4)
        zhrf4 = re.sub('ظ', 'ظۗہٰٰ', zhrf4)
        zhrf4 = re.sub('q', '𝑸', zhrf4)
        zhrf4 = re.sub('Q', '𝑸', zhrf4)
        zhrf4 = re.sub('w', '𝑾', zhrf4)
        zhrf4 = re.sub('W', '𝑾', zhrf4)
        zhrf4 = re.sub('e', '𝑬', zhrf4)
        zhrf4 = re.sub('E', '𝑬', zhrf4)
        zhrf4 = re.sub('r', '𝑹', zhrf4)
        zhrf4 = re.sub('R', '𝑹', zhrf4)
        zhrf4 = re.sub('t', '𝑻', zhrf4)
        zhrf4 = re.sub('T', '𝑻', zhrf4)
        zhrf4 = re.sub('y', '𝒀', zhrf4)
        zhrf4 = re.sub('Y', '𝒀', zhrf4)
        zhrf4 = re.sub('u', '𝑼', zhrf4)
        zhrf4 = re.sub('U', '𝑼', zhrf4)
        zhrf4 = re.sub('i', '𝑰', zhrf4)
        zhrf4 = re.sub('I', '𝑰', zhrf4)
        zhrf4 = re.sub('o', '𝑶', zhrf4)
        zhrf4 = re.sub('O', '𝑶', zhrf4)
        zhrf4 = re.sub('p', '𝑷', zhrf4)
        zhrf4 = re.sub('P', '𝑷', zhrf4)
        zhrf4 = re.sub('a', '𝑨', zhrf4)
        zhrf4 = re.sub('A', '𝑨', zhrf4)
        zhrf4 = re.sub('s', '𝑺', zhrf4)
        zhrf4 = re.sub('S', '𝑺', zhrf4)
        zhrf4 = re.sub('d', '𝑫', zhrf4)
        zhrf4 = re.sub('D', '𝑫', zhrf4)
        zhrf4 = re.sub('f', '𝑭', zhrf4)
        zhrf4 = re.sub('F', '𝑭', zhrf4)
        zhrf4 = re.sub('g', '𝑮', zhrf4)
        zhrf4 = re.sub('G', '𝑮', zhrf4)
        zhrf4 = re.sub('h', '𝑯', zhrf4)
        zhrf4 = re.sub('H', '𝑯', zhrf4)
        zhrf4 = re.sub('j', '𝑱', zhrf4)
        zhrf4 = re.sub('J', '𝑱', zhrf4)
        zhrf4 = re.sub('k', '𝑲', zhrf4)
        zhrf4 = re.sub('K', '𝑲', zhrf4)
        zhrf4 = re.sub('l', '𝑳', zhrf4)
        zhrf4 = re.sub('L', '𝑳', zhrf4)
        zhrf4 = re.sub('z', '𝒁', zhrf4)
        zhrf4 = re.sub('Z', '𝒁', zhrf4)
        zhrf4 = re.sub('x', '𝑿', zhrf4)
        zhrf4 = re.sub('X', '𝑿', zhrf4)
        zhrf4 = re.sub('c', '𝑪', zhrf4)
        zhrf4 = re.sub('C', '𝑪', zhrf4)
        zhrf4 = re.sub('v', '𝑽', zhrf4)
        zhrf4 = re.sub('V', '𝑽', zhrf4)
        zhrf4 = re.sub('b', '𝑩', zhrf4)
        zhrf4 = re.sub('B', '𝑩', zhrf4)
        zhrf4 = re.sub('n', '𝑵', zhrf4)
        zhrf4 = re.sub('N', '𝑵', zhrf4)
        zhrf4 = re.sub('m', '𝑴', zhrf4)
        zhrf4 = re.sub('M', '𝑴', zhrf4)

        zhrf5 = re.sub('ض', 'ضَ', m.text)
        zhrf5 = re.sub('ص', 'صً', zhrf5)
        zhrf5 = re.sub('ث', 'ثَ', zhrf5)
        zhrf5 = re.sub('ق', 'قُ', zhrf5)
        zhrf5 = re.sub('ف', 'فّ', zhrf5)
        zhrf5 = re.sub('غ', 'غِ', zhrf5)
        zhrf5 = re.sub('ع', 'عُ', zhrf5)
        zhrf5 = re.sub('ه', 'ﮭ', zhrf5)
        zhrf5 = re.sub('خ', 'خِ', zhrf5)
        zhrf5 = re.sub('ح', 'حٌ', zhrf5)
        zhrf5 = re.sub('ج', 'جُ', zhrf5)
        zhrf5 = re.sub('د', 'دِ', zhrf5)
        zhrf5 = re.sub('ذ', 'ذَ', zhrf5)
        zhrf5 = re.sub('ش', 'شِ', zhrf5)
        zhrf5 = re.sub('س', 'سً', zhrf5)
        zhrf5 = re.sub('ي', 'يْ', zhrf5)
        zhrf5 = re.sub('ب', 'بّ', zhrf5)
        zhrf5 = re.sub('ل', 'لَ', zhrf5)
        zhrf5 = re.sub('ا', 'أُ', zhrf5)
        zhrf5 = re.sub('ت', 'تٌ', zhrf5)
        zhrf5 = re.sub('ن', 'نً', zhrf5)
        zhrf5 = re.sub('م', 'مِ', zhrf5)
        zhrf5 = re.sub('ك', 'ڳّ', zhrf5)
        zhrf5 = re.sub('ط', 'طٌ', zhrf5)
        zhrf5 = re.sub('ئ', 'ئ', zhrf5)
        zhrf5 = re.sub('ء', 'ء', zhrf5)
        zhrf5 = re.sub('ؤ', 'ؤ', zhrf5)
        zhrf5 = re.sub('ر', 'رٌ', zhrf5)
        zhrf5 = re.sub('لا', 'لٌأً', zhrf5)
        zhrf5 = re.sub('ى', 'ى', zhrf5)
        zhrf5 = re.sub('ة', 'ةَ', zhrf5)
        zhrf5 = re.sub('و', 'وِ', zhrf5)
        zhrf5 = re.sub('ز', 'زُ', zhrf5)
        zhrf5 = re.sub('ظ', 'ظ', zhrf5)
        zhrf5 = re.sub('q', '𝒒', zhrf5)
        zhrf5 = re.sub('Q', '𝒒', zhrf5)
        zhrf5 = re.sub('w', '𝒘', zhrf5)
        zhrf5 = re.sub('W', '𝒘', zhrf5)
        zhrf5 = re.sub('e', '𝒆', zhrf5)
        zhrf5 = re.sub('E', '𝒆', zhrf5)
        zhrf5 = re.sub('r', '𝒓', zhrf5)
        zhrf5 = re.sub('R', '𝒓', zhrf5)
        zhrf5 = re.sub('t', '𝒕', zhrf5)
        zhrf5 = re.sub('T', '𝒕', zhrf5)
        zhrf5 = re.sub('y', '𝒚', zhrf5)
        zhrf5 = re.sub('Y', '𝒚', zhrf5)
        zhrf5 = re.sub('u', '𝒖', zhrf5)
        zhrf5 = re.sub('U', '𝒖', zhrf5)
        zhrf5 = re.sub('i', '𝒊', zhrf5)
        zhrf5 = re.sub('I', '𝒊', zhrf5)
        zhrf5 = re.sub('o', '𝒐', zhrf5)
        zhrf5 = re.sub('O', '𝒐', zhrf5)
        zhrf5 = re.sub('p', '𝒑', zhrf5)
        zhrf5 = re.sub('P', '𝒑', zhrf5)
        zhrf5 = re.sub('a', '𝒂', zhrf5)
        zhrf5 = re.sub('A', '𝒂', zhrf5)
        zhrf5 = re.sub('s', '𝒔', zhrf5)
        zhrf5 = re.sub('S', '𝒔', zhrf5)
        zhrf5 = re.sub('d', '𝒅', zhrf5)
        zhrf5 = re.sub('D', '𝒅', zhrf5)
        zhrf5 = re.sub('f', '𝒇', zhrf5)
        zhrf5 = re.sub('F', '𝒇', zhrf5)
        zhrf5 = re.sub('g', '𝒈', zhrf5)
        zhrf5 = re.sub('G', '𝒈', zhrf5)
        zhrf5 = re.sub('h', '𝒉', zhrf5)
        zhrf5 = re.sub('H', '𝒉', zhrf5)
        zhrf5 = re.sub('j', '𝒋', zhrf5)
        zhrf5 = re.sub('J', '𝒋', zhrf5)
        zhrf5 = re.sub('K', '𝒌', zhrf5)
        zhrf5 = re.sub('k', '𝒌', zhrf5)
        zhrf5 = re.sub('L', '𝒍', zhrf5)
        zhrf5 = re.sub('l', '𝒍', zhrf5)
        zhrf5 = re.sub('z', '𝒛', zhrf5)
        zhrf5 = re.sub('Z', '𝒛', zhrf5)
        zhrf5 = re.sub('x', '𝒙', zhrf5)
        zhrf5 = re.sub('X', '𝒙', zhrf5)
        zhrf5 = re.sub('c', '𝒄', zhrf5)
        zhrf5 = re.sub('C', '𝒄', zhrf5)
        zhrf5 = re.sub('v', '𝒗', zhrf5)
        zhrf5 = re.sub('V', '𝒗', zhrf5)
        zhrf5 = re.sub('b', '𝒃', zhrf5)
        zhrf5 = re.sub('B', '𝒃', zhrf5)
        zhrf5 = re.sub('n', '𝒏', zhrf5)
        zhrf5 = re.sub('N', '𝒏', zhrf5)
        zhrf5 = re.sub('m', '𝒎', zhrf5)
        zhrf5 = re.sub('M', '𝒎', zhrf5)

        zhrf6 = re.sub('ض', 'ﺿ̭͠', m.text)
        zhrf6 = re.sub('ص', 'ﺻ͡', zhrf6)
        zhrf6 = re.sub('ث', 'ﺜ̲', zhrf6)
        zhrf6 = re.sub('ق', 'ﭰ', zhrf6)
        zhrf6 = re.sub('ف', 'ﻓ̲', zhrf6)
        zhrf6 = re.sub('غ', 'ﻏ̲', zhrf6)
        zhrf6 = re.sub('ع', 'ﻌ̲', zhrf6)
        zhrf6 = re.sub('ه', 'ﮬ̲̌', zhrf6)
        zhrf6 = re.sub('خ', 'خٌ', zhrf6)
        zhrf6 = re.sub('ح', 'ﺣ̅', zhrf6)
        zhrf6 = re.sub('ج', 'جُ', zhrf6)
        zhrf6 = re.sub('د', 'ډ̝', zhrf6)
        zhrf6 = re.sub('ذ', 'ذً', zhrf6)
        zhrf6 = re.sub('ش', 'ﺷ̲', zhrf6)
        zhrf6 = re.sub('س', 'ﺳ̉', zhrf6)
        zhrf6 = re.sub('ي', 'ﯾ̃̐', zhrf6)
        zhrf6 = re.sub('ب', 'ﺑ̲', zhrf6)
        zhrf6 = re.sub('ل', 'ا̄ﻟ', zhrf6)
        zhrf6 = re.sub('ا', 'ﺈ̃', zhrf6)
        zhrf6 = re.sub('ت', 'ټُ', zhrf6)
        zhrf6 = re.sub('ن', 'ﻧ̲', zhrf6)
        zhrf6 = re.sub('م', 'ﻣ̲̉', zhrf6)
        zhrf6 = re.sub('ك', 'گ', zhrf6)
        zhrf6 = re.sub('ط', 'ﻁ̲', zhrf6)
        zhrf6 = re.sub('ئ', ' ْٰئ', zhrf6)
        zhrf6 = re.sub('ء', 'ء', zhrf6)
        zhrf6 = re.sub('ؤ', 'ؤ', zhrf6)
        zhrf6 = re.sub('ر', 'ہڕ', zhrf6)
        zhrf6 = re.sub('لا', 'ﻟ̲ﺂ̲', zhrf6)
        zhrf6 = re.sub('ى', 'ى', zhrf6)
        zhrf6 = re.sub('ة', 'ة', zhrf6)
        zhrf6 = re.sub('و', 'ۇۈۉ', zhrf6)
        zhrf6 = re.sub('ز', 'زُ', zhrf6)
        zhrf6 = re.sub('ظ', 'ﻇ̲', zhrf6)
        zhrf6 = re.sub('q', 'ǫ', zhrf6)
        zhrf6 = re.sub('Q', 'ǫ', zhrf6)
        zhrf6 = re.sub('w', 'ᴡ', zhrf6)
        zhrf6 = re.sub('W', 'ᴡ', zhrf6)
        zhrf6 = re.sub('e', 'ᴇ', zhrf6)
        zhrf6 = re.sub('E', 'ᴇ', zhrf6)
        zhrf6 = re.sub('r', 'ʀ', zhrf6)
        zhrf6 = re.sub('R', 'ʀ', zhrf6)
        zhrf6 = re.sub('t', 'ᴛ', zhrf6)
        zhrf6 = re.sub('T', 'ᴛ', zhrf6)
        zhrf6 = re.sub('y', 'ʏ', zhrf6)
        zhrf6 = re.sub('Y', 'ʏ', zhrf6)
        zhrf6 = re.sub('u', 'ụ', zhrf6)
        zhrf6 = re.sub('U', 'ụ', zhrf6)
        zhrf6 = re.sub('i', 'ɪ', zhrf6)
        zhrf6 = re.sub('I', 'ɪ', zhrf6)
        zhrf6 = re.sub('o', 'ᴏ', zhrf6)
        zhrf6 = re.sub('O', 'ᴏ', zhrf6)
        zhrf6 = re.sub('p', 'ᴘ', zhrf6)
        zhrf6 = re.sub('P', 'ᴘ', zhrf6)
        zhrf6 = re.sub('a', 'ᴀ', zhrf6)
        zhrf6 = re.sub('A', 'ᴀ', zhrf6)
        zhrf6 = re.sub('s', 'ѕ', zhrf6)
        zhrf6 = re.sub('S', 'ѕ', zhrf6)
        zhrf6 = re.sub('d', 'ᴅ', zhrf6)
        zhrf6 = re.sub('D', 'ᴅ', zhrf6)
        zhrf6 = re.sub('f', 'ғ', zhrf6)
        zhrf6 = re.sub('F', 'ғ', zhrf6)
        zhrf6 = re.sub('g', 'ɢ', zhrf6)
        zhrf6 = re.sub('G', 'ɢ', zhrf6)
        zhrf6 = re.sub('h', 'ʜ', zhrf6)
        zhrf6 = re.sub('H', 'ʜ', zhrf6)
        zhrf6 = re.sub('j', 'ᴊ', zhrf6)
        zhrf6 = re.sub('J', 'ᴊ', zhrf6)
        zhrf6 = re.sub('K', 'ᴋ', zhrf6)
        zhrf6 = re.sub('k', 'ᴋ', zhrf6)
        zhrf6 = re.sub('L', 'ʟ', zhrf6)
        zhrf6 = re.sub('l', 'ʟ', zhrf6)
        zhrf6 = re.sub('z', 'ᴢ', zhrf6)
        zhrf6 = re.sub('Z', 'ᴢ', zhrf6)
        zhrf6 = re.sub('x', 'х', zhrf6)
        zhrf6 = re.sub('X', 'х', zhrf6)
        zhrf6 = re.sub('c', 'ᴄ', zhrf6)
        zhrf6 = re.sub('C', 'ᴄ', zhrf6)
        zhrf6 = re.sub('v', 'ᴠ', zhrf6)
        zhrf6 = re.sub('V', 'ᴠ', zhrf6)
        zhrf6 = re.sub('b', 'ʙ', zhrf6)
        zhrf6 = re.sub('B', 'ʙ', zhrf6)
        zhrf6 = re.sub('n', 'ɴ', zhrf6)
        zhrf6 = re.sub('N', 'ɴ', zhrf6)
        zhrf6 = re.sub('m', 'ᴍ', zhrf6)
        zhrf6 = re.sub('M', 'ᴍ', zhrf6)

        zhrf7 = re.sub('ض', 'ﺿ', m.text)
        zhrf7 = re.sub('ص', 'ﺻ', zhrf7)
        zhrf7 = re.sub('ث', 'ﭥ', zhrf7)
        zhrf7 = re.sub('ق', 'ﻗ̮ـ̃', zhrf7)
        zhrf7 = re.sub('ف', 'ﭬ', zhrf7)
        zhrf7 = re.sub('غ', 'ﻏ̣̐', zhrf7)
        zhrf7 = re.sub('ع', 'ﻋ', zhrf7)
        zhrf7 = re.sub('ه', 'ھَہّ', zhrf7)
        zhrf7 = re.sub('خ', 'ﺧ', zhrf7)
        zhrf7 = re.sub('ح', 'פ', zhrf7)
        zhrf7 = re.sub('ج', 'ﭴ', zhrf7)
        zhrf7 = re.sub('د', 'ﮃ', zhrf7)
        zhrf7 = re.sub('ذ', 'ذ', zhrf7)
        zhrf7 = re.sub('ش', 'ﺷ', zhrf7)
        zhrf7 = re.sub('س', 'ﺳ', zhrf7)
        zhrf7 = re.sub('ي', 'ﯾ', zhrf7)
        zhrf7 = re.sub('ب', 'ﺑ', zhrf7)
        zhrf7 = re.sub('ل', 'ﻟ', zhrf7)
        zhrf7 = re.sub('ا', 'ﺂ', zhrf7)
        zhrf7 = re.sub('ت', 'ﭠ', zhrf7)
        zhrf7 = re.sub('ن', 'ﻧ', zhrf7)
        zhrf7 = re.sub('م', 'ﻣ̝̚', zhrf7)
        zhrf7 = re.sub('ك', 'گـ', zhrf7)
        zhrf7 = re.sub('ط', 'ﻁْ', zhrf7)
        zhrf7 = re.sub('ئ', 'ٰئـ', zhrf7)
        zhrf7 = re.sub('ء', 'ء', zhrf7)
        zhrf7 = re.sub('ؤ', 'ﯗ', zhrf7)
        zhrf7 = re.sub('ر', 'ړُ', zhrf7)
        zhrf7 = re.sub('لا', 'ﻟآ', zhrf7)
        zhrf7 = re.sub('ى', 'ـﮯ', zhrf7)
        zhrf7 = re.sub('ة', 'ة', zhrf7)
        zhrf7 = re.sub('و', 'ۆ', zhrf7)
        zhrf7 = re.sub('ز', 'ژ', zhrf7)
        zhrf7 = re.sub('ظ', 'ﻅ', zhrf7)
        zhrf7 = re.sub('q', '𝘘', zhrf7)
        zhrf7 = re.sub('Q', '𝘘', zhrf7)
        zhrf7 = re.sub('w', '𝘞', zhrf7)
        zhrf7 = re.sub('W', '𝘞', zhrf7)
        zhrf7 = re.sub('e', '𝘌', zhrf7)
        zhrf7 = re.sub('E', '𝘌', zhrf7)
        zhrf7 = re.sub('r', '𝘙', zhrf7)
        zhrf7 = re.sub('R', '𝘙', zhrf7)
        zhrf7 = re.sub('t', '𝘛', zhrf7)
        zhrf7 = re.sub('T', '𝘛', zhrf7)
        zhrf7 = re.sub('y', '𝘠', zhrf7)
        zhrf7 = re.sub('Y', '𝘠', zhrf7)
        zhrf7 = re.sub('u', '𝘜', zhrf7)
        zhrf7 = re.sub('U', '𝘜', zhrf7)
        zhrf7 = re.sub('i', '𝘐', zhrf7)
        zhrf7 = re.sub('I', '𝘐', zhrf7)
        zhrf7 = re.sub('o', '𝘖', zhrf7)
        zhrf7 = re.sub('O', '𝘖', zhrf7)
        zhrf7 = re.sub('p', '𝘗', zhrf7)
        zhrf7 = re.sub('P', '𝘗', zhrf7)
        zhrf7 = re.sub('a', '𝘈', zhrf7)
        zhrf7 = re.sub('A', '𝘈', zhrf7)
        zhrf7 = re.sub('s', '𝘚', zhrf7)
        zhrf7 = re.sub('S', '𝘚', zhrf7)
        zhrf7 = re.sub('d', '𝘋', zhrf7)
        zhrf7 = re.sub('D', '𝘋', zhrf7)
        zhrf7 = re.sub('f', '𝘍', zhrf7)
        zhrf7 = re.sub('F', '𝘍', zhrf7)
        zhrf7 = re.sub('g', '𝘎', zhrf7)
        zhrf7 = re.sub('G', '𝘎', zhrf7)
        zhrf7 = re.sub('h', '𝘏', zhrf7)
        zhrf7 = re.sub('H', '𝘏', zhrf7)
        zhrf7 = re.sub('j', '𝘑', zhrf7)
        zhrf7 = re.sub('J', '𝘑', zhrf7)
        zhrf7 = re.sub('k', '𝘒', zhrf7)
        zhrf7 = re.sub('K', '𝘒', zhrf7)
        zhrf7 = re.sub('L', '𝘓', zhrf7)
        zhrf7 = re.sub('l', '𝘓', zhrf7)
        zhrf7 = re.sub('z', '𝘡', zhrf7)
        zhrf7 = re.sub('Z', '𝘡', zhrf7)
        zhrf7 = re.sub('x', '𝘟', zhrf7)
        zhrf7 = re.sub('X', '𝘟', zhrf7)
        zhrf7 = re.sub('c', '𝘊', zhrf7)
        zhrf7 = re.sub('C', '𝘊', zhrf7)
        zhrf7 = re.sub('v', '𝘝', zhrf7)
        zhrf7 = re.sub('V', '𝘝', zhrf7)
        zhrf7 = re.sub('b', '𝘉', zhrf7)
        zhrf7 = re.sub('B', '𝘉', zhrf7)
        zhrf7 = re.sub('n', '𝘕', zhrf7)
        zhrf7 = re.sub('N', '𝘕', zhrf7)
        zhrf7 = re.sub('m', '𝘔', zhrf7)
        zhrf7 = re.sub('M', '𝘔', zhrf7)

        zhrf8 = re.sub('ض', 'ض', m.text)
        zhrf8 = re.sub('ص', 'صہٰ', zhrf8)
        zhrf8 = re.sub('ث', 'ثہٰـ', zhrf8)
        zhrf8 = re.sub('ق', 'قہٰ', zhrf8)
        zhrf8 = re.sub('ف', 'فہٰ', zhrf8)
        zhrf8 = re.sub('غ', 'غـْ', zhrf8)
        zhrf8 = re.sub('ع', 'ع', zhrf8)
        zhrf8 = re.sub('ه', 'هٰہٰٖ', zhrf8)
        zhrf8 = re.sub('خ', 'خخَـ', zhrf8)
        zhrf8 = re.sub('ح', 'حہٰ', zhrf8)
        zhrf8 = re.sub('ج', 'ججہٰ', zhrf8)
        zhrf8 = re.sub('د', 'دَ', zhrf8)
        zhrf8 = re.sub('ذ', 'ذّ', zhrf8)
        zhrf8 = re.sub('ش', 'ششہٰ', zhrf8)
        zhrf8 = re.sub('س', 'سہٰ', zhrf8)
        zhrf8 = re.sub('ي', 'يٰ', zhrf8)
        zhrf8 = re.sub('ب', 'بٰٰ', zhrf8)
        zhrf8 = re.sub('ل', 'لہٰ', zhrf8)
        zhrf8 = re.sub('ا', 'آ', zhrf8)
        zhrf8 = re.sub('ت', 'تہٰ', zhrf8)
        zhrf8 = re.sub('ن', 'نہٰ', zhrf8)
        zhrf8 = re.sub('م', 'مہٰ', zhrf8)
        zhrf8 = re.sub('ك', 'ككہٰ', zhrf8)
        zhrf8 = re.sub('ط', 'طہٰ', zhrf8)
        zhrf8 = re.sub('ئ', ' ْئٰ', zhrf8)
        zhrf8 = re.sub('ء', 'ء', zhrf8)
        zhrf8 = re.sub('ؤ', 'ؤؤَ', zhrf8)
        zhrf8 = re.sub('ر', 'رَ', zhrf8)
        zhrf8 = re.sub('لا', 'لہٰا', zhrf8)
        zhrf8 = re.sub('ى', 'ىہٰ', zhrf8)
        zhrf8 = re.sub('ة', 'ة', zhrf8)
        zhrf8 = re.sub('و', 'ہٰو', zhrf8)
        zhrf8 = re.sub('ز', 'ز', zhrf8)
        zhrf8 = re.sub('ظ', 'ظہٰ', zhrf8)
        zhrf8 = re.sub('q', '𝚀', zhrf8)
        zhrf8 = re.sub('Q', '𝚀', zhrf8)
        zhrf8 = re.sub('w', '𝚆', zhrf8)
        zhrf8 = re.sub('W', '𝚆', zhrf8)
        zhrf8 = re.sub('e', '𝙴', zhrf8)
        zhrf8 = re.sub('E', '𝙴', zhrf8)
        zhrf8 = re.sub('r', '𝚁', zhrf8)
        zhrf8 = re.sub('R', '𝚁', zhrf8)
        zhrf8 = re.sub('t', '𝚃', zhrf8)
        zhrf8 = re.sub('T', '𝚃', zhrf8)
        zhrf8 = re.sub('y', '𝚈', zhrf8)
        zhrf8 = re.sub('Y', '𝚈', zhrf8)
        zhrf8 = re.sub('u', '𝚄', zhrf8)
        zhrf8 = re.sub('U', '𝚄', zhrf8)
        zhrf8 = re.sub('i', '𝙸', zhrf8)
        zhrf8 = re.sub('I', '𝙸', zhrf8)
        zhrf8 = re.sub('o', '𝙾', zhrf8)
        zhrf8 = re.sub('O', '𝙾', zhrf8)
        zhrf8 = re.sub('p', '𝙿', zhrf8)
        zhrf8 = re.sub('P', '𝙿', zhrf8)
        zhrf8 = re.sub('a', '𝙰', zhrf8)
        zhrf8 = re.sub('A', '𝙰', zhrf8)
        zhrf8 = re.sub('s', '𝚂', zhrf8)
        zhrf8 = re.sub('S', '𝚂', zhrf8)
        zhrf8 = re.sub('d', '𝙳', zhrf8)
        zhrf8 = re.sub('D', '𝙳', zhrf8)
        zhrf8 = re.sub('f', '𝙵', zhrf8)
        zhrf8 = re.sub('F', '𝙵', zhrf8)
        zhrf8 = re.sub('g', '𝙶', zhrf8)
        zhrf8 = re.sub('G', '𝙶', zhrf8)
        zhrf8 = re.sub('h', '𝙷', zhrf8)
        zhrf8 = re.sub('H', '𝙷', zhrf8)
        zhrf8 = re.sub('j', '𝙹', zhrf8)
        zhrf8 = re.sub('J', '𝙹', zhrf8)
        zhrf8 = re.sub('k', '𝙺', zhrf8)
        zhrf8 = re.sub('K', '𝙺', zhrf8)
        zhrf8 = re.sub('L', '𝙻', zhrf8)
        zhrf8 = re.sub('l', '𝙻', zhrf8)
        zhrf8 = re.sub('z', '𝚉', zhrf8)
        zhrf8 = re.sub('Z', '𝚉', zhrf8)
        zhrf8 = re.sub('x', '𝚇', zhrf8)
        zhrf8 = re.sub('X', '𝚇', zhrf8)
        zhrf8 = re.sub('c', '𝙲', zhrf8)
        zhrf8 = re.sub('C', '𝙲', zhrf8)
        zhrf8 = re.sub('v', '𝚅', zhrf8)
        zhrf8 = re.sub('V', '𝚅', zhrf8)
        zhrf8 = re.sub('b', '𝙱', zhrf8)
        zhrf8 = re.sub('B', '𝙱', zhrf8)
        zhrf8 = re.sub('n', '𝙽', zhrf8)
        zhrf8 = re.sub('N', '𝙽', zhrf8)
        zhrf8 = re.sub('m', '𝙼', zhrf8)
        zhrf8 = re.sub('M', '𝙼', zhrf8)

        zhrf9 = re.sub('ض', 'ض', m.text)
        zhrf9 = re.sub('ص', 'ص', zhrf9)
        zhrf9 = re.sub('ث', 'ث', zhrf9)
        zhrf9 = re.sub('ق', 'قٌ', zhrf9)
        zhrf9 = re.sub('ف', 'فُ', zhrf9)
        zhrf9 = re.sub('غ', 'غ', zhrf9)
        zhrf9 = re.sub('ع', 'عٍ', zhrf9)
        zhrf9 = re.sub('ه', 'هـ', zhrf9)
        zhrf9 = re.sub('خ', 'خـ', zhrf9)
        zhrf9 = re.sub('ح', 'حٍ', zhrf9)
        zhrf9 = re.sub('ج', 'جٍ', zhrf9)
        zhrf9 = re.sub('د', 'دِ', zhrf9)
        zhrf9 = re.sub('ذ', 'ذَ', zhrf9)
        zhrf9 = re.sub('ش', 'شُ', zhrf9)
        zhrf9 = re.sub('س', 'س', zhrf9)
        zhrf9 = re.sub('ي', 'ي', zhrf9)
        zhrf9 = re.sub('ب', 'بَ', zhrf9)
        zhrf9 = re.sub('ل', 'لُِ', zhrf9)
        zhrf9 = re.sub('ا', 'آ', zhrf9)
        zhrf9 = re.sub('ت', 'ت', zhrf9)
        zhrf9 = re.sub('ن', 'ن', zhrf9)
        zhrf9 = re.sub('م', 'م', zhrf9)
        zhrf9 = re.sub('ك', 'ڪ', zhrf9)
        zhrf9 = re.sub('ط', 'طُ', zhrf9)
        zhrf9 = re.sub('ئ', 'ئ ْٰ', zhrf9)
        zhrf9 = re.sub('ء', 'ء', zhrf9)
        zhrf9 = re.sub('ؤ', 'ؤ', zhrf9)
        zhrf9 = re.sub('ر', 'ر', zhrf9)
        zhrf9 = re.sub('لا', 'لُِآ', zhrf9)
        zhrf9 = re.sub('ى', 'ىْ', zhrf9)
        zhrf9 = re.sub('ة', 'ة', zhrf9)
        zhrf9 = re.sub('و', 'وو', zhrf9)
        zhrf9 = re.sub('ز', 'ز', zhrf9)
        zhrf9 = re.sub('ظ', 'ظهُ', zhrf9)
        zhrf9 = re.sub('q', 'ℚ', zhrf9)
        zhrf9 = re.sub('Q', 'ℚ', zhrf9)
        zhrf9 = re.sub('w', '𝕎', zhrf9)
        zhrf9 = re.sub('W', '𝕎', zhrf9)
        zhrf9 = re.sub('e', '𝔼', zhrf9)
        zhrf9 = re.sub('E', '𝔼', zhrf9)
        zhrf9 = re.sub('r', 'ℝ', zhrf9)
        zhrf9 = re.sub('R', 'ℝ', zhrf9)
        zhrf9 = re.sub('t', '𝕋', zhrf9)
        zhrf9 = re.sub('T', '𝕋', zhrf9)
        zhrf9 = re.sub('y', '𝕐', zhrf9)
        zhrf9 = re.sub('Y', '𝕐', zhrf9)
        zhrf9 = re.sub('u', '𝕌', zhrf9)
        zhrf9 = re.sub('U', '𝕌', zhrf9)
        zhrf9 = re.sub('i', '𝕀', zhrf9)
        zhrf9 = re.sub('I', '𝕀', zhrf9)
        zhrf9 = re.sub('o', '𝕆', zhrf9)
        zhrf9 = re.sub('O', '𝕆', zhrf9)
        zhrf9 = re.sub('p', 'ℙ', zhrf9)
        zhrf9 = re.sub('P', 'ℙ', zhrf9)
        zhrf9 = re.sub('a', '𝔸', zhrf9)
        zhrf9 = re.sub('A', '𝔸', zhrf9)
        zhrf9 = re.sub('s', '𝕊', zhrf9)
        zhrf9 = re.sub('S', '𝕊', zhrf9)
        zhrf9 = re.sub('d', '𝔻', zhrf9)
        zhrf9 = re.sub('D', '𝔻', zhrf9)
        zhrf9 = re.sub('f', '𝔽', zhrf9)
        zhrf9 = re.sub('F', '𝔽', zhrf9)
        zhrf9 = re.sub('g', '𝔾', zhrf9)
        zhrf9 = re.sub('G', '𝔾', zhrf9)
        zhrf9 = re.sub('h', 'ℍ', zhrf9)
        zhrf9 = re.sub('H', 'ℍ', zhrf9)
        zhrf9 = re.sub('j', '𝕁', zhrf9)
        zhrf9 = re.sub('J', '𝕁', zhrf9)
        zhrf9 = re.sub('k', '𝕂', zhrf9)
        zhrf9 = re.sub('K', '𝕂', zhrf9)
        zhrf9 = re.sub('L', '𝕃', zhrf9)
        zhrf9 = re.sub('l', '𝕃', zhrf9)
        zhrf9 = re.sub('z', 'ℤ', zhrf9)
        zhrf9 = re.sub('Z', 'ℤ', zhrf9)
        zhrf9 = re.sub('x', '𝕏', zhrf9)
        zhrf9 = re.sub('X', '𝕏', zhrf9)
        zhrf9 = re.sub('c', 'ℂ', zhrf9)
        zhrf9 = re.sub('C', 'ℂ', zhrf9)
        zhrf9 = re.sub('v', '𝕍', zhrf9)
        zhrf9 = re.sub('V', '𝕍', zhrf9)
        zhrf9 = re.sub('b', '𝔹', zhrf9)
        zhrf9 = re.sub('B', '𝔹', zhrf9)
        zhrf9 = re.sub('n', 'ℕ', zhrf9)
        zhrf9 = re.sub('N', 'ℕ', zhrf9)
        zhrf9 = re.sub('m', '𝕄', zhrf9)
        zhrf9 = re.sub('M', '𝕄', zhrf9)

        Text_Zhrfa = "♕ `" + zhrf + random.choice(EmojeS) \
                     + "`\n\n` " + zhrf2 + random.choice(EmojeS) \
                     + "`\n\n` " + zhrf3 + random.choice(EmojeS) \
                     + "•\n\n` " + zhrf4 + random.choice(EmojeS) \
                     + "`\n\n` " + zhrf5 + random.choice(EmojeS) \
                     + "`\n\n` " + zhrf6 + random.choice(EmojeS) \
                     + "`\n\n` " + zhrf7 + random.choice(EmojeS) \
                     + "`\n\n` " + zhrf8 + random.choice(Emoje) \
                     + "`\n\n` " + zhrf9 + random.choice(Emoje) \
                     + "`\n\n` " + zhrf5 + random.choice(Emoje)
        Text_Zhrfa = Text_Zhrfa + "<b>\n\n دەست بدە لەناوەکە کۆپی دەبێت \n│ \n👾</b>"
        await m.reply_text(Text_Zhrfa, reply_to_message_id=m.id)

print("Wait........")
app.run()
print("Bot is run")