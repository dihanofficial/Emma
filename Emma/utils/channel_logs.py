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

import html

from Emma import bot
from Emma.config import get_int_key
from Emma.utils.logger import log


async def channel_log(msg, info_log=True):
    chat_id = get_int_key("LOGS_CHANNEL_ID")
    if info_log:
        log.info(msg)

    await bot.send_message(chat_id, html.escape(msg, quote=False))
