"""
VideoPlayerBot, Telegram Video Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

admins = {}
OLD_PMS = {}
AUDIO_CALL = {}
VIDEO_CALL = {}
API_ID = int(getenv("14284911", ""))
API_HASH = getenv("8a3d2e03520271bf1ab61f76f9c4279c", "")
BOT_TOKEN = getenv("5124052732:AAFhkJBdqEKKkMvR3varpH_t8v28rcqQcyw", "")
SESSION_STRING = getenv("AQA5l3nveV19zeNKBNI5DNfbcvwMfVcNXJiXYDdj8_1X_NRDhcl4CuNFSadiC_OIHVwcZIkOtUiUPhtlJ7yMC7Xpuzy9YriiT2iQDclRUki-X78DTdrQQ0hlEoq7fzUUT4HU3xrI24nHxOkfs01FhZLD83hNE78djqzcmwKHGp32-4euRQlwwjthHz69I8d537zTf6nMKhQEsx87rw9Oh_qzF0nCg58WntFuukbZ8k_g-ErC1ULVCdUuMkoUzNzNTKkqek2ZVN6rJR8UFeq2e4ZhNyT7gk955gd6rNpI2KFwUn9wlFpuE_erniwWYMEjsoMxIBpm63EycnOHniElXlkMAAAAATXsoYQA", "")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "AsmSupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "AsmSafone")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "MyVideoPlayer")
SUDO_USERS = list(map(int, getenv("1321702696").split()))
REPLY_MESSAGE = getenv("REPLY_MESSAGE", "")
if not REPLY_MESSAGE:
    REPLY_MESSAGE = None
else:
    REPLY_MESSAGE = REPLY_MESSAGE
