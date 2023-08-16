import hikari
import lightbulb
import discord
import random

bot = lightbulb.BotApp(token='',
                        default_enabled_guilds=(), intents=hikari.Intents.ALL)

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('Bot started!')

#@bot.listen(hikari.GuildMessageCreateEvent)  //get message content command
#async def message(event):
    #print(event.content)

#command
@bot.command
@lightbulb.command('piinng','Says pong!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('Pong!')
#command_group
@bot.command
@lightbulb.command('group','This is a group')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def m_group(ctx):
    pass

@m_group.child
@lightbulb.command('subcommand', 'This is a subcommand')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond('I am a subcommand!')

@m_group.child
@lightbulb.command('subcommand2', 'Anothe subcommand')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond('Another one')

#Error Handler 
@bot.listen(lightbulb.CommandErrorEvent)
async def errorhandler(event: lightbulb.CommandErrorEvent) -> None:
    if isinstance(event.exception, lightbulb.CommandInvocationError):
        await event.context.respond(f"Something went wrong during the invocation of command `{event.context.command.name}`")
        raise event.exception
    
    exception = event.exception.__cause__ or event.exception

    if isinstance(exception, lightbulb.NotOwner):
        await event.context.respond("You are not the owner")
    elif isinstance(exception, lightbulb.CommandIsOnCooldown):
        m, s=divmod(exception.retry_after, 60)
        h ,m=divmod(m,60)
        await event.context.respond(f"Come back in `{s:.2f}` seconds.")
    else:
        raise exception

bot.load_extensions_from('./Extensions')
bot.run()