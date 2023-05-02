from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
API_ID = "20809128"
API_HASH = "69c8efc67e1e5b4e696b7f98ee4d7d51"
BOT_USERNAME = "Ksgkye_bot"
session = "1AZWarzMBu7Jdm_edGUUZ8vfUq1BQV0sqA2ZRuMFVYrRe9noPCJU0qVktzip4JOsAus1QeVEHVxpg3mKpy0ekSLrDbfkFSbyiqthrwuazY_wGAmhlopZDlWKYsZVfN1eRRuyDuI4hYXZXQZsigQlrZ5_YVWIOs5yfV4i5i2YOF8-fwCY_8vKP69yikmj671wPBWiO-x23cVrZAxYNQo9TZZkL8sWtbtBzYnr6OQv7fVXz3QFAj4gjNS1VMZv7ua9C6rJCiIARv4sWT6zaRz5Rfb9Edr_MH-3WSOvdcnoi-Nbf2vo5j2zKo57ecpEM7i0vvgRSEDvmdMcN1v_pXgdQ-t7t6zGuDak="
SESSION = "1AZWarzMBu7Jdm_edGUUZ8vfUq1BQV0sqA2ZRuMFVYrRe9noPCJU0qVktzip4JOsAus1QeVEHVxpg3mKpy0ekSLrDbfkFSbyiqthrwuazY_wGAmhlopZDlWKYsZVfN1eRRuyDuI4hYXZXQZsigQlrZ5_YVWIOs5yfV4i5i2YOF8-fwCY_8vKP69yikmj671wPBWiO-x23cVrZAxYNQo9TZZkL8sWtbtBzYnr6OQv7fVXz3QFAj4gjNS1VMZv7ua9C6rJCiIARv4sWT6zaRz5Rfb9Edr_MH-3WSOvdcnoi-Nbf2vo5j2zKo57ecpEM7i0vvgRSEDvmdMcN1v_pXgdQ-t7t6zGuDak="
token = "6022228026:AAH4MwFk3sNno832jZ9SorCsVbHBheK2c-0"
eighthon = TelegramClient(StringSession(session), API_ID, API_HASH)
bot = TelegramClient("bot", API_ID, API_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()
