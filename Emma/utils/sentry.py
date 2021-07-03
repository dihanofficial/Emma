# This file is part of Emma (Telegram Bot)

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sentry_sdk
from sentry_sdk.integrations.redis import RedisIntegration

from Emma.config import get_str_key
from Emma.utils.logger import log

log.info("Starting sentry.io integraion...")

sentry_sdk.init(get_str_key("SENTRY_API_KEY"), integrations=[RedisIntegration()])
