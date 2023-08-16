import hikari
import lightbulb
import discord
import random
import datetime as dt

plugin = lightbulb.Plugin('Commands')

@plugin.listener(hikari.GuildMessageCreateEvent)
async def print_messages(event):
    print(event.content)

#Say command
@plugin.command
@lightbulb.option('text_var', 'Something', type=str)
@lightbulb.command('say', 'Something')
@lightbulb.implements(lightbulb.SlashCommand)
async def say_command(ctx):
    await ctx.respond(ctx.options.text_var)

#Say Hello
@plugin.command
@lightbulb.command('hello','hello')
@lightbulb.implements(lightbulb.SlashCommand)
async def hello_command(ctx):
     greetings=[
          "Hi there!",
          "Hey!",
          "Hello!",
          "Howdy!",
          "Greetings!",
          "Salutations!",
          "What's up?",
          "Yo!",
          "Hiya!",
          "How's it going?",
          "Hey, what's cracking?",
          "Hola!",
          "Good day!",
          "Hi, friend!",
          "Aloha!",
          "Sup?",
          "Hi, there, lovely!",
          "Wassup?",
          "Bonjour!"
     ]
     msgs = random.choice(greetings)
     await ctx.respond(f"{msgs} {ctx.author.mention}")

#Clear command
@plugin.command
@lightbulb.option('lines', 'number of lines', type=int)
@lightbulb.command('clear', 'delete lines')
@lightbulb.implements(lightbulb.SlashCommand)
async def clear_command(ctx):
     lines = int(ctx.options.lines)
     channel = str(ctx.channel_id)
     msgs = await ctx.bot.rest.fetch_messages(channel).limit(lines)
     await ctx.bot.rest.delete_messages(channel, msgs)
     await ctx.respond(f"Done!")

#Calculator
@plugin.command
@lightbulb.command('calculator', 'Math calculator')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def calculator_command(ctx):
     pass

@calculator_command.child
@lightbulb.option('num2', 'Second number', type=int)
@lightbulb.option('num1', 'First number', type=int)
@lightbulb.command('add', 'aduna')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)

@calculator_command.child
@lightbulb.option('num2', 'The second number', type=int)
@lightbulb.option('num1', 'The first number', type=int)
@lightbulb.command('minus', 'Scade')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def minus_command(ctx):
     await ctx.respond(ctx.options.num1 - ctx.options.num2)

@calculator_command.child
@lightbulb.option('num2', 'The second number', type=int)
@lightbulb.option('num1', 'The first number', type=int)
@lightbulb.command('multiplication', 'inmulteste')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def multiplication_command(ctx):
     await ctx.respond(ctx.options.num1 * ctx.options.num2)

@calculator_command.child
@lightbulb.option('num2', 'The second number', type=int)
@lightbulb.option('num1', 'The first number', type=int)
@lightbulb.command('division', 'imparte')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def division_command(ctx):
     await ctx.respond(ctx.options.num1 / ctx.options.num2)

#UserInfo
@plugin.command
@lightbulb.option('target', 'Member', hikari.Member)
@lightbulb.command('userinfo', 'userinfo')
@lightbulb.implements(lightbulb.SlashCommand)
async def userinfo_command(ctx: lightbulb.context.Context) -> None:
     target_ = ctx.options.target
     target = (
        target_
        if isinstance(target_, hikari.Member)
        else ctx.get_guild().get_member(target_)
     )
     if not target:
        await ctx.respond("That user is not in the server.")
        return

     created_at = int(target.created_at.timestamp())
     joined_at = int(target.joined_at.timestamp())
     roles = (await target.fetch_roles())[1:]

     embed = (
        hikari.Embed(
            title="User information",
            description=f"ID: {target.id}",
            colour=hikari.Colour(0x563275),
        )
        .set_thumbnail(target.avatar_url)
        .set_footer("Random")
        .add_field(name='Name: ', value=target.display_name, inline=False)
        .add_field(name='Bot?',value=target.is_bot, inline=False)
        .add_field(name='Requested by: ', value=ctx.author.username, inline=False)
    )

     await ctx.respond(embed)

#Join New Server  NotWorking!  
@plugin.listener
@lightbulb.command(hikari.GuildJoinEvent, 'Something')
async def greet_new_member(ctx, event: hikari.GuildJoinEvent):
        greetings = [
            "Hello, everyone! I'm here to assist and have some fun with you!",
            "Greetings, fellow server members! Let's make this server even more awesome together!",
            "Welcome, new friends! Get ready for some exciting times ahead!",
            "Hey there! Excited to join your fantastic server. Let's make memories together!",
            "Ahoy, mates! Your friendly bot has arrived to lend a helping hand.",
            "Salutations! I'm here to answer your questions and share some laughs.",
            "Hi, everyone! I'm here to ensure your server experience is top-notch.",
            "Welcome aboard! Let's make this server a place of camaraderie and enjoyment.",
            "Hello, lovely people! Ready to explore and have a great time?",
            "Greetings, adventurers! Let's embark on a journey of fun and discovery.",
            "Hey, folks! Your AI friend is here to make your server experience even better!"
            "Hello, world! I'm here to bring a dash of excitement to your server.",
            "Welcome, wanderers! Prepare for a voyage filled with laughter and interaction.",
            "Hey, everyone! Let's create memorable moments and share some smiles!",
            "Greetings, companions! I'm here to assist and make your stay enjoyable.",
            "Hello, fellow enthusiasts! Let's collaborate and have a blast in this server.",
            "Welcome, dear members! Let's build a vibrant community together."
            "Hey, team! I'm here to enhance your server experience in every way I can.",
            "Hello, heroes! I'm your bot ally, ready to aid and amuse.",
            "Greetings, fellow beings of the internet! Let's make this server awesome!"
        ]
        
        msgs = random.choice(greetings)
        await ctx.member.get_guild().get_text_channels()[0].send(msgs)

#Coinflip command
@plugin.command
@lightbulb.command('coinflip','Flip a coin')
@lightbulb.implements(lightbulb.SlashCommand)
async def coinflip_command(ctx):
     number = random.randint(1,10)
     if number % 2 == 0:
          await ctx.respond(f"Tails")
     else:
          await ctx.respond(f"Head")

#Joke
@plugin.command
@lightbulb.command('joke','jokes')
@lightbulb.implements(lightbulb.SlashCommand)
async def joke_command(ctx):
     jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them.",
    "Parallel lines have so much in common. It's a shame they'll never meet.",
    "Why was the math book sad? It had too many problems.",
    "I told my wife she was drawing her eyebrows too high. She seemed surprised.",
    "How do you organize a space party? You 'planet'!",
    "Why don't skeletons fight each other? They don't have the guts.",
    "Why don't scientists trust stairs? Because they're always up to something.",
    "How do you make holy water? You boil the hell out of it.",
    "What's orange and sounds like a parrot? A carrot!",
    "What's brown and sticky? A stick!",
    "Why don't oysters donate to charity? Because they're shellfish.",
    "I used to play piano by ear, but now I use my hands.",
    "Did you hear about the cheese factory explosion? There was nothing left but de-brie.",
    "How do you catch a squirrel? Climb a tree and act like a nut!",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "Parallel lines have so much in common. It's a shame they'll never meet.",
    "Why don't scientists trust atoms? Because they make up everything!",
    "How do you organize a space party? You 'planet'!",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "Parallel lines have so much in common. It's a shame they'll never meet.",
    "Why don't scientists trust atoms? Because they make up everything!",
    "How do you organize a space party? You 'planet'!",
    "What's orange and sounds like a parrot? A carrot!",
    "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them.",
    "Why was the math book sad? It had too many problems.",
    "I told my wife she was drawing her eyebrows too high. She seemed surprised.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "Why don't scientists trust stairs? Because they're always up to something.",
    "How do you make holy water? You boil the hell out of it.",
    "What's brown and sticky? A stick!",
    "Why don't oysters donate to charity? Because they're shellfish.",
    "I used to play piano by ear, but now I use my hands.",
    "Did you hear about the cheese factory explosion? There was nothing left but de-brie.",
    "How do you catch a squirrel? Climb a tree and act like a nut!",
    "Why don't eggs tell jokes? Because they might crack up.",
    "How do you organize a space party? You 'planet'!",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "Parallel lines have so much in common. It's a shame they'll never meet.",
    "Why don't scientists trust atoms? Because they make up everything!",
    "What's orange and sounds like a parrot? A carrot!",
    "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them.",
    "Why was the math book sad? It had too many problems.",
    "I told my wife she was drawing her eyebrows too high. She seemed surprised.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "Why don't scientists trust stairs? Because they're always up to something.",
    "How do you make holy water? You boil the hell out of it.",
    "What's brown and sticky? A stick!",
    "Why don't oysters donate to charity? Because they're shellfish.",
    "I used to play piano by ear, but now I use my hands.",
    "Did you hear about the cheese factory explosion? There was nothing left but de-brie.",
    "How do you catch a squirrel? Climb a tree and act like a nut!",
    "Why don't eggs tell jokes? Because they might crack up.",
    "How do you organize a space party? You 'planet'!",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "Parallel lines have so much in common. It's a shame they'll never meet.",
    "Why don't scientists trust atoms? Because they make up everything!",
    "What's orange and sounds like a parrot? A carrot!",
    "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them.",
    "Why was the math book sad? It had too many problems.",
    "I told my wife she was drawing her eyebrows too high. She seemed surprised.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "Why don't scientists trust stairs? Because they're always up to something.",
    "How do you make holy water? You boil the hell out of it.",
    "What's brown and sticky? A stick!",
    "Why don't oysters donate to charity? Because they're shellfish.",
    "I used to play piano by ear, but now I use my hands.",
    "Did you hear about the cheese factory explosion? There was nothing left but de-brie.",
    "How do you catch a squirrel? Climb a tree and act like a nut!",
    "Why don't eggs tell jokes? Because they might crack up.",
    "Ur mom"
]
     random_joke = random.choice(jokes)
     await ctx.respond(random_joke)

#Roll
@plugin.command
@lightbulb.option('num2', 'Second number', type=int)
@lightbulb.option('num1','First number', type=int)
@lightbulb.command('roll','pick 2 numbers')
@lightbulb.implements(lightbulb.SlashCommand)
async def roll_command(ctx):
     number = random.randint(ctx.options.num1,ctx.options.num2)
     await ctx.respond(number)

def load(bot):
    bot.add_plugin(plugin)