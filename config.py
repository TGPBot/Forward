from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "fe9a6ba19c179384e55d0ee0be216a5e")
      API_ID = int(getenv("API_ID", 20726759))
      AS_COPY = True if getenv("AS_COPY", False) == "True" else False
      BOT_TOKEN = getenv("BOT_TOKEN", "6058302908:AAGpTMECwmd_f-U7sPNhaMi5U0e9-3tSztc")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001918503297").replace("\n", " ").split(' '))
