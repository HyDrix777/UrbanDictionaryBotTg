from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = "𝑯𝒆𝒚 {}. \n\n𝑾𝒆𝒍𝒄𝒐𝒎𝒆 𝒕𝒐 {} \n\n𝑰 𝒄𝒂𝒏 𝒔𝒆𝒂𝒓𝒄𝒉 𝒘𝒐𝒓𝒅𝒔 𝒇𝒓𝒐𝒎 𝑼𝒓𝒃𝒂𝒏 𝑫𝒊𝒄𝒕𝒊𝒐𝒏𝒂𝒓𝒚 𝒂𝒏𝒅 𝒈𝒊𝒗𝒆 𝒕𝒉𝒆𝒎 𝒕𝒐 𝒚𝒐𝒖. 𝑰 𝒘𝒊𝒍𝒍 𝒑𝒓𝒐𝒗𝒊𝒅𝒆 𝒊𝒕'𝒔 𝒅𝒆𝒇𝒊𝒏𝒊𝒕𝒊𝒐𝒏 𝒂𝒔 𝒘𝒆𝒍𝒍 𝒂𝒔 𝒆𝒙𝒂𝒎𝒑𝒍𝒆 \n\n𝒀𝒐𝒖 𝒄𝒂𝒏 𝒔𝒆𝒏𝒅 𝒂𝒏𝒚 𝒘𝒐𝒓𝒅 𝒉𝒆𝒓𝒆 𝒐𝒓 𝑻𝒓𝒚 𝒖𝒔𝒊𝒏𝒈 𝒎𝒚 𝒊𝒏𝒍𝒊𝒏𝒆 𝒎𝒐𝒅𝒆."

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔍 Search Inline 🔍", switch_inline_query_current_chat="")],
        [
            InlineKeyboardButton(
                "➕ Add to your Group ➕", url="https://t.me/DictionaryXrobot?startgroup=True"
            )
        ],
        [InlineKeyboardButton(text="🏠 Return Home", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("Search Inline 🔍", switch_inline_query_current_chat=""),
            InlineKeyboardButton("🆘How to Use🆘", callback_data="help")
        ],
        [
            InlineKeyboardButton("🚫 About The Bot", callback_data="about")
        ],
        [
            InlineKeyboardButton(
                "➕ Add to your Group ➕", url="https://t.me/DictionaryXrobot?startgroup=True"
            )
        
    ]

    # Help Message
    HELP = """
1) **Inline Mode** (recommended)
 ~ Search any word or word sequence in inline mode, any time.
 ~ Use "`-r`" to get random word

2) **Private Chat**
 ~ Send any word or word sequence privately, any time.
 ~ Send "/random" to get random word.

3) **Group Chats**
 ~ Add in group and reply to any message with /ud or /search".
 ~ You can also use: "/ud text here" or "/search text here" in groups.
 ~ Send "/random" to get random word.
(If doesn't responds in group then make it admin. Telegram is weird)
    """

    # About Message
    ABOUT = """
**About This Bot** 

Thanks for the sopport

Source Code : [Click Here](https://github.com/StatsIndustries/UrbanallDictionaryBotTgpg)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Thanks for using me 🙂
    """
