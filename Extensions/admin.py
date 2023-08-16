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

#Kick
@plugin.command
@lightbulb.option('target', 'Member', hikari.Member)
@lightbulb.command('kick','kick a member')
@lightbulb.implements(lightbulb.SlashCommand)
async def kick_command(ctx: lightbulb.context.Context) -> None:
    target_ = ctx.options.target
    target = (
        target_
        if isinstance(target_, hikari.Member)
        else ctx.get_guild().get_member(target_)
     )
    if not target:
        await ctx.respond("That user is not in the server.")
        return
    await target.kick(reason='None')

#Ban
@plugin.command
@lightbulb.option('target', 'Member', hikari.Member)
@lightbulb.command('ban','ban a member')
@lightbulb.implements(lightbulb.SlashCommand)
async def kick_command(ctx: lightbulb.context.Context) -> None:
    target_ = ctx.options.target
    target = (
        target_
        if isinstance(target_, hikari.Member)
        else ctx.get_guild().get_member(target_)
     )
    if not target:
        await ctx.respond("That user is not in the server.")
        return
    await target.ban(reason='None')

def load(bot):
    bot.add_plugin(plugin)