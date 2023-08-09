import hikari
import lightbulb
import discord
import random

plugin = lightbulb.Plugin('Admin')

#Add role
@plugin.command
@lightbulb.command('addrole','add role')
@lightbulb.implements(lightbulb.SlashCommand)
async def addrole_command(ctx):
    await ctx.member.add_role('1137755946974715964')
    await ctx.respond('Role added')

#Remove role
@plugin.command
@lightbulb.command('rmvrole', 'remove role')
@lightbulb.implements(lightbulb.SlashCommand)
async def rmvrole_command(ctx):
    await ctx.member.remove_role('1137755946974715964')
    await ctx.respond('Role removed')

#Kick Not Working
@plugin.command
@lightbulb.command('kick','kick a member')
@lightbulb.implements(lightbulb.SlashCommand)
async def kick_command(ctx, member : hikari.User, reason=None):
    member_id=member.id
    await ctx.bot.rest.create_guild_ban(ctx.get_guild(), member_id, reason=reason)
    await ctx.respond(f'{member.display_name} has been kicked. Reason: {reason}')

def load(bot):
    bot.add_plugin(plugin)