import hikari
import lightbulb
import string
import os
import sys

plugin = lightbulb.Plugin('control_panel')


def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)
@plugin.command()
@lightbulb.command('restart','Restart')
@lightbulb.implements(lightbulb.SlashCommand)
async def restart(ctx):
  await ctx.respond("Restarting bot...")
  restart_bot()


#Ping Test
@plugin.command()
@lightbulb.command("ping", "Get the average DWSP latency for the bot.")
@lightbulb.implements(lightbulb.SlashCommand)
async def cmd_ping(ctx: lightbulb.SlashContext) -> None:
    await ctx.respond(
        f"Pong! DWSP latency: {ctx.bot.heartbeat_latency * 1_000:,.0f} ms."
    )

def load(bot):
    bot.add_plugin(plugin)