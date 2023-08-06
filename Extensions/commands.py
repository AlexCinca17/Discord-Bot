import hikari
import lightbulb

plugin = lightbulb.Plugin('Commands')

@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_messages(event):
    print(event.content)



def load(bot):
    bot.add_plugin(plugin)