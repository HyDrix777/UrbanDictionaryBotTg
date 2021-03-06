from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = "π―ππ {}. \n\nπΎππππππ ππ {} \n\nπ° πππ ππππππ πππππ ππππ πΌππππ π«πππππππππ πππ ππππ ππππ ππ πππ. π° ππππ πππππππ ππ'π ππππππππππ ππ ππππ ππ πππππππ \n\nπππ πππ ππππ πππ ππππ ππππ ππ π»ππ πππππ ππ ππππππ ππππ."

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("π Search Inline π", switch_inline_query_current_chat="")],
        [
            InlineKeyboardButton(
                "β Add to your Group β", url="https://t.me/DictionaryXrobot?startgroup=True"
            )
        ],
        [InlineKeyboardButton(text="π  Return Home", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("Search Inline π", switch_inline_query_current_chat=""),
            InlineKeyboardButton("πHow to Useπ", callback_data="help")
        ],
        [
            InlineKeyboardButton("π« About The Bot", callback_data="about")
        ],
        [
            InlineKeyboardButton(
                "β Add to your Group β", url="https://t.me/DictionaryXrobot?startgroup=True"
            )
        ],
        [InlineKeyboardButton("π₯ Group", url="https://t.me/Tg_Galaxy")],
        
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

Thanks for using me π
    """
