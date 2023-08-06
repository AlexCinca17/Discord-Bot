import hikari
import lightbulb

plugin = lightbulb.Plugin('Example')

@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_messages(event):
    print(event.content)

@plugin.command
@lightbulb.command('lol', 'Wtf LOL')
@lightbulb.implements(lightbulb.SlashCommand)
async def lol(ctx):
    await ctx.respond('LOL')

def load(bot):
    bot.add_plugin(plugin)