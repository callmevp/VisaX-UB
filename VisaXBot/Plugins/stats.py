import time

from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User

from . import *


@bot.on(visa_cmd(pattern="stats$"))
@bot.on(sudo_cmd(pattern="stats$", allow_sudo=True))
async def stats(
    event: NewMessage.Event,
) -> None:  # pylint: disable = R0912, R0914, R0915
    if event.fwd_from:
        return
    visa = await edit_or_reply(event, "`Collecting stats...`")
    start_time = time.time()
    private_chats = 0
    bots = 0
    groups = 0
    broadcast_channels = 0
    admin_in_groups = 0
    creator_in_groups = 0
    admin_in_broadcast_channels = 0
    creator_in_channels = 0
    unread_mentions = 0
    unread = 0
    dialog: Dialog
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel):
            # participants_count = (await event.get_participants(dialog,
            # limit=0)).total
            if entity.broadcast:
                broadcast_channels += 1
                if entity.creator or entity.admin_rights:
                    admin_in_broadcast_channels += 1
                if entity.creator:
                    creator_in_channels += 1
            elif entity.megagroup:
                groups += 1
                # if participants_count > largest_group_member_count:
                #     largest_group_member_count = participants_count
                if entity.creator or entity.admin_rights:
                    # if participants_count > largest_group_with_admin:
                    #     largest_group_with_admin = participants_count
                    admin_in_groups += 1
                if entity.creator:
                    creator_in_groups += 1
        elif isinstance(entity, User):
            private_chats += 1
            if entity.bot:
                bots += 1
        elif isinstance(entity, Chat):
            groups += 1
            if entity.creator or entity.admin_rights:
                admin_in_groups += 1
            if entity.creator:
                creator_in_groups += 1
        unread_mentions += dialog.unread_mentions_count
        unread += dialog.unread_count
    stop_time = time.time() - start_time
    full_name = inline_mention(await event.client.get_me())
    response = f"???? ???????????????????? ????????  {full_name} ????\n\n"
    response += f"??????????????????????????????????????????????????????????????????\n" 
    response += f"??? ???? ???????????????????????????? ????????????????????: {private_chats} \n"
    response += f"??? ???? ????????????????????: {private_chats - bots}  \n"
    response += f"??? ???? ????????????????: {bots}  \n"
    response += f"??? ???? ????????????????????????: {groups} \n"
    response += f"??? ???? ????????????????????????????????: {broadcast_channels} \n"
    response += f"??? ???? ???????????????????? ???????? ????????????????????????: {admin_in_groups} \n"
    response += f"??? ???? ????????????????????????????: {creator_in_groups} \n"
    response += f"??? ???? ???????????????????? ????????????????????????: {admin_in_groups - creator_in_groups} \n"
    response += f"??? ???? ???????????????????? ???????? ????????????????????????????: {admin_in_broadcast_channels} \n"
    response += f"??? ???? ????????????????????????????: {creator_in_channels} \n"
    response += f"??? ???? ???????????????????? ????????????????????????: {admin_in_broadcast_channels - creator_in_channels} \n"
    response += f"??? ???? ????????????????????????: {unread} \n"
    response += f"??? ???? ???????????????????????? ????????????????????????????????: {unread_mentions} \n"
    response += f"??? ???? ???????? ????????????????: {stop_time:.02f}???? \n"
    response += f"??????????????????????????????????????????????????????????????????\n\n"

    response += (
        f"???? ???????????????? ???????????? ???????????????????????????????? ???????? :-\n[???? ?????g????????????? ???? ????????-?? ?????? ????](t.me/Visa_support)\n\n" 
    )
    await visa.edit(response)


def make_mention(user):
    if user.username:
        return f"@{user.username}"
    return inline_mention(user)


def inline_mention(user):
    full_name = user_full_name(user) or "H??ll"
    return f"[{full_name}](tg://user?id={user.id})"


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    return " ".join(names)


CmdHelp("stats").add_command(
  'stats', None, 'Shows you the count of your groups, channels, private chats, etc.'
).add_info(
  'Statistics Of Account'
).add_warning(
  '??? Harmless Module.'
).add()
