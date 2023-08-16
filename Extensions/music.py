import hikari
import lightbulb

plugin = lightbulb.Plugin('Music')


def load(bot):
    bot.add_plugin(plugin)