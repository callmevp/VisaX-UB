# credit goes to @D3_krish and @official_sameer

from telethon import events
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *


#-------------------------------------------------------------------------------
DEFAULTER = Config.YOUR_NAME

@bot.on(visa_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def up(visa):
    if visa.fwd_from:
        return
    await visa.get_chat()
    await visa.delete()
    await bot.send_file(visa.chat_id, VISA_PIC, caption=VISA_CAPTION)
    await visa.delete()

VISA_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/37ac22fe95355d62c2d76.mp4"
VISA_CAPTION = "đĽ ĘÉÉ˘ÉŐźÉÇĘĘ ÇĘ ĘÉ¨ÖÇ-Óź ÉŽÖČś đĽ\n\n"
VISA_CAPTION += (
    f"                __âźđźđ°đđđ´đâ__\n  **ă {visa_mention} ă**\n\n"
)
VISA_CAPTION += f"âââââââââââââââââ\n"
VISA_CAPTION += f"â â˘âłâ  `đđ´đťđ´đđˇđžđ˝:` `{tel_ver}` \n"
VISA_CAPTION += f"â â˘âłâ  `đđ´đđđ¸đžđ˝:` `{visa_ver}`\n"
VISA_CAPTION += f"â â˘âłâ  `đśđđžđđż:`  [đšđžđ¸đ˝](t.me/Visa_SUPPORT)\n"
VISA_CAPTION += f"â â˘âłâ  `đ˛đˇđ°đ˝đ˝đ´đť:` [đšđžđ¸đ˝](t.me/Visa_Update)\n"
VISA_CAPTION += f"â â˘âłâ  `đ˛đđ´đ°đđžđ:` [âĄđżđđžâĄ](https://t.me/CALL_ME_VP)\n"
VISA_CAPTION += f"âââââââââââââââââ\n\n"
VISA_CAPTION += " [â¨đđ´đżđžâ¨](https://github.com/callmevp/VisaXBot) đš [đđťđ¸đ˛đ´đ˝đđ´đ](https://github.com/callmevp/VisaXBot/blob/main/LICENSE)"
                            
#_______



@bot.on(visa_cmd(outgoing=True, pattern="awake$"))
@bot.on(sudo_cmd(pattern="awake$", allow_sudo=True))
async def up(visa):
    if visa.fwd_from:
        return
    await visa.get_chat()
    await visa.delete()
    await bot.send_file(visa.chat_id, VISA_PIC, caption=visa_caption)
    await visa.delete()

visa_caption = f"đĽ ĘÉÉ˘ÉŐźÉÇĘĘ ÇĘ ĘÉ¨ÖÇ-Óź ÉŽÖČś đĽ\n\n"
visa_caption += f"ââââââââââââââââââââââââââââ\n\n"
visa_caption += f"**{Config.ALIVE_MSG}**\n\n"
visa_caption += f"ââââââââââââââââââââââââââââ\n\n"                
visa_caption += f"đŁ đ°đąđžđđ đźđ đđđđđ´đź đŁ\n\n"
visa_caption += f"âž `đđ´đťđ´đđˇđžđ˝` âŁ `{tel_ver}` \n"
visa_caption += f"âž `đđđłđž đźđžđłđ´:` âŁ `{is_sudo}`\n"
visa_caption += f"âž đźđ đ˛đˇđ°đ˝đ˝đ´đť: âŁ [đšđžđ¸đ˝](t.me/Config.YOUR_CHANNEL)\n"
visa_caption += f"âž đźđ đśđđžđđż: âŁ [đšđžđ¸đ˝](t.me/Config.YOUR_GROUP)\n\n"
visa_caption += f"[â¨ đđđđđđ đđđđ đđđđ-đ đđđ â¨](https://github.com/callmevp/VisaXBot)\n" 
                                     
                                 
                
CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "Awake", None, "Shows Inline Alive Menu with more details."
).add_warning(
  "â Harmless Module"
).add()
