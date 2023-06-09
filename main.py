# main.py

import importlib
import os
import glob
from pyrogram import Client
from config import API_TOKEN, API_ID, API_HASH

class Userbot(Client):
    def __init__(self):
        super().__init__(
            session_name="userbot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=API_TOKEN,
        )

    def load_modules(self):
        path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "modules")
        modules = glob.glob(f"{path}/*.py")

        for module in modules:
            module_name = os.path.basename(module)[:-3]
            module_path = f"modules.{module_name}"

            try:
                importlib.import_module(module_path)
                print(f"[INFO] Loaded module: {module_name}")
            except Exception as e:
                print(f"[ERROR] Failed to load module: {module_name} - {e}")

    def start(self):
        self.load_modules()
        super().start()

    def stop(self):
        super().stop()

if __name__ == "__main__":
    userbot = Userbot()
    userbot.start()
