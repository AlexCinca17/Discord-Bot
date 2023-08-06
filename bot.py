import hikari
import lightbulb

bot = lightbulb.BotApp(token='TOKEN',
                        default_enabled_guilds=('Testing server id'))

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('Bot started!')
#command
@bot.command
@lightbulb.command('ping','Says pong!')
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

@bot.command
@lightbulb.option('num2', 'The second number', type=int)
@lightbulb.option('num1', 'The first number', type=int)
@lightbulb.command('add', 'Add two numbers together')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)

bot.load_extensions_from('./Extensions')
bot.run()