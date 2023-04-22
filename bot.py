from pyrogram import Client 
from config import API_ID, API_HASH, BOT_TOKEN, FORCE_SUB, PORT, WEBHOOK 
from aiohttp import web
from route import web_server

class Bot(Client):

    def __init__(self):
        super().__init__(
            name="renamer",
            api_id=28749782,
            api_hash=41ccb476f64d1348fab05079840a7ed3,
            bot_token=6029848697:AAFCU5z3rXtDtY77POMk118ySEkMNj5QDFU,
            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=15,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username 
        self.force_channel = https://t.me/alllivecricketmatches
        if https://t.me/alllivecricketmatches:
            try:
                link = await self.export_chat_invite_link(https://t.me/alllivecricketmatches)                  
                self.invitelink = link
            except Exception as e:
                print(e)
                print("Make Sure Bot admin in force sub channel")             
                self.force_channel = None
        if WEBHOOK:
            app = web.AppRunner(await web_server())
            await app.setup()       
            await web.TCPSite(app, "0.0.0.0", PORT).start()     
        print(f"{me.first_name} 𝚂𝚃𝙰𝚁𝚃𝙴𝙳 ⚡️⚡️⚡️")
      

    async def stop(self, *args):
        await super().stop()      
        print("Bot Stopped")
       

bot=Bot()
bot.run()
