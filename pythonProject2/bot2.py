from discord.ext.commands import bot

BOT_PREFIX = ("!")
TOKEN = "NzUyNzk0ODYxOTcwNzg0MjU4.X1c02Q.lBXuGu7l4WHxk7A96y47Qt6ONAA"
client = bot(command_prefix=BOT_PREFIX)

client.run(TOKEN)