# Copyright (C) 2020 Dihan Official

# This file is part of Emma (Telegram Bot)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import random
from contextlib import suppress

from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import MessageNotModified
from Emma.decorator import register

from Emma.modules.utils.disable import disableable_dec

from . import MOD_HELP
from .language import select_lang_keyboard
from .utils.disable import disableable_dec
from .utils.language import get_strings_dec

helpmenu_cb = CallbackData("helpmenu", "mod")


def help_markup(modules):
    markup = InlineKeyboardMarkup()
    for module in modules:
        markup.insert(
            InlineKeyboardButton(module, callback_data=helpmenu_cb.new(mod=module))
        )
    return markup


STICKERS = (
    "CAACAgUAAxkBAAIT0WDT_9vlxT8UT7zd4KS0B00Swx4yAALaBQACOI6ZVtQmJ58BrF6EHgQ",
    "CAACAgUAAxkBAAIT2GDUAAElxf0VRP-Y78hzdZgBF6jHvQACBgQAAk66kFb6aCcpkNLKWh4E",
    "CAACAgUAAxkBAAIT3WDUAAGJhWoWV2ENCzNxKXE6-QiEVAACWAMAAqNJmFY0_-aWGYvGeh4E",
    "CAACAgUAAxkBAAIUIGDUBB_wnSovmtJTM6L33r07JFVGAALoAQACt_jwV84L7yV925FmHgQ",
    "CAACAgUAAxkBAAIT72DUAiOTejKJM6tje3Q65iaIXcxRAAJLAgACl22YVkMjdJmouwoWHgQ",
    "CAACAgUAAxkBAAIT7GDUAgTCmx7omAcfF26o_f40yObDAAJ2AgAC_bSYVq2xoCnR3xmuHgQ",
    "CAACAgUAAxkBAAIUBmDUA_alWCDgu25988NnQVX9RDkEAAIXAQACfgLoV0lrI6UxLXrrHgQ",
    "CAACAgUAAxkBAAIT-2DUAoc_zGoLhCEYYOnfL6q0ry9qAAIxBAACzt6ZVkDdPzVYe5l5HgQ",
    "CAACAgUAAxkBAAIT5mDUAdAd8RXUtfKiQ2ifPBhF-9BYAALKBAACbgWYViaIi0cWmR3LHgQ",
    "CAACAgUAAxkBAAIT-GDUAmuQO6F3jEkkoE-CFacTmPDXAAKyAgACm7eYVj0rrWgw43nOHgQ",
    "CAACAgUAAxkBAAIUA2DUA-kLc_rnSRsD1B23_9X26BZdAAK6AQACaVm5V6QygeVH028PHgQ",
    "CAACAgUAAxkBAAIT6WDUAekCr3-bbTXVyncaQFPNlpb-AALxAgACe0yYVtJEv2a_gQ6XHgQ",
    "CAACAgUAAxkBAAIT8mDUAjzuVp-Ted1W8Np_q2MF8-qvAAL1AgACYAiYVkDrGiuqVGyiHgQ",
    "CAACAgUAAxkBAAIULWDUBdanEzas6ZBDnMZsLylVDh4LAAJ7AgACWIGgVoGQShu8lYnvHgQ",
    "CAACAgUAAxkBAAIT4GDUAZjubr3Mh2oRP13UEevhBd_iAALFAgACJLqZVu8aC6J0swzFHgQ",
    "CAACAgUAAxkBAAIUMWDUBfWjFLmmpETV8o8jaB6SEdNEAAIjAgACAtqhVtm2xvyDbh_0HgQ",
    "CAACAgUAAxkBAAIT9WDUAlRiKqBG8DULvdRKrpQXP_vsAAJgAwACT9OZViBzgyvtdeWpHgQ",
    "CAACAgUAAxkBAAIUNWDUBharieXsQzphnPMPU6Nxl7QMAALUAgACHRWhVoKUglpqY4-zHgQ",
    "CAACAgUAAxkBAAIT42DUAbUUEwjCYsRQulbLSpWS7u45AAJuAgACv5GYVnc_8mNJs29MHgQ",
    "CAACAgUAAxkBAAIUNGDUBiZkuAjSJWEE-U3mlbQyImtqAAKuAgACi_egVvKCCvvYXVDtHgQ",
    "CAACAgUAAxkBAAIUO2DUBk53OYgGciNEKCg_Jkq0C8R4AALXAgACstugVq5fYqbzOYwcHgQ",
)


@register(cmds="start", no_args=True, only_groups=True)
@disableable_dec("start")
@get_strings_dec("pm_menu")
async def start_group_cmd(message, strings):
    await message.reply(strings["start_hi_group"])


@register(cmds="start", no_args=True, only_pm=True)
async def start_cmd(message):
    await message.reply_sticker(random.choice(STICKERS))
    await get_start_func(message)


@get_strings_dec("pm_menu")
async def get_start_func(message, strings, edit=False):
    msg = message.message if hasattr(message, "message") else message

    task = msg.edit_text if edit else msg.reply
    buttons = InlineKeyboardMarkup()
    buttons.add(InlineKeyboardButton(strings["btn_help"], callback_data="get_help"))
    buttons.add(
        InlineKeyboardButton(strings["btn_lang"], callback_data="lang_btn"),
        InlineKeyboardButton(
            strings["btn_source"],
            url="https://github.com/dihanofficial/Emma",
        ),
    )
    buttons.add(
        InlineKeyboardButton(
            strings["btn_channel"], url="https://t.me/EmmaBot_updates"
        ),
        InlineKeyboardButton(strings["btn_group"], url="https://t.me/EmmaBot_support"),
    )
    buttons.add(
        InlineKeyboardButton("🥰𝙔𝙤𝙪𝙩𝙪𝙗𝙚 𝘾𝙝𝙖𝙣𝙣𝙚𝙡", url="https://youtube.com/channel/"),
        InlineKeyboardButton(
            "😋𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥",
            url="https://t.me/dihanrandila",
        ),
    )
    buttons.add(
        InlineKeyboardButton(
            "🤖𝘽𝙊𝙏𝙎 𝙐𝙋𝘿𝘼𝙏𝙀𝙎",
            url=f"https://telegram.me/DihanOfficial",
        ),
    )
    buttons.add(
        InlineKeyboardButton(
            "➕Add Emma to your group➕",
            url=f"https://telegram.me/TheEmmaBot?startgroup=true",
        ),
    )
    buttons.add(
        InlineKeyboardButton(
            "➕Add Music Assistant➕",
            url=f"https://telegram.me/dihanofficial_helper?startgroup=true",
        )
    )
    # Handle error when user click the button 2 or more times simultaneously
    with suppress(MessageNotModified):
        await task(strings["start_hi"], reply_markup=buttons)


@register(regexp="get_help", f="cb")
@get_strings_dec("pm_menu")
async def help_cb(event, strings):
    button = help_markup(MOD_HELP)
    button.add(InlineKeyboardButton(strings["back"], callback_data="go_to_start"))
    with suppress(MessageNotModified):
        await event.message.edit_text(strings["help_header"], reply_markup=button)


@register(regexp="lang_btn", f="cb")
async def set_lang_cb(event):
    await select_lang_keyboard(event.message, edit=True)


@register(regexp="go_to_start", f="cb")
async def back_btn(event):
    await get_start_func(event, edit=True)


@register(cmds="help", only_pm=True)
@disableable_dec("help")
@get_strings_dec("pm_menu")
async def help_cmd(message, strings):
    button = help_markup(MOD_HELP)
    button.add(InlineKeyboardButton(strings["back"], callback_data="go_to_start"))
    await message.reply(strings["help_header"], reply_markup=button)


@register(cmds="help", only_groups=True)
@disableable_dec("help")
@get_strings_dec("pm_menu")
async def help_cmd_g(message, strings):
    text = strings["btn_group_help"]
    button = InlineKeyboardMarkup().add(
        InlineKeyboardButton(text=text, url="https://t.me/TheEmmaBot?start")
    )
    await message.reply(strings["help_header"], reply_markup=button)


@register(helpmenu_cb.filter(), f="cb", allow_kwargs=True)
async def helpmenu_callback(query, callback_data=None, **kwargs):
    mod = callback_data["mod"]
    if not mod in MOD_HELP:
        await query.answer()
        return
    msg = f"Help for <b>{mod}</b> module:\n"
    msg += f"{MOD_HELP[mod]}"
    button = InlineKeyboardMarkup().add(
        InlineKeyboardButton(text="🏃‍♂️ Back", callback_data="get_help")
    )
    with suppress(MessageNotModified):
        await query.message.edit_text(
            msg, disable_web_page_preview=True, reply_markup=button
        )
        await query.answer("Help for " + mod)
