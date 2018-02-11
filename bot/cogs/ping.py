"""Ping module."""

from discord.ext import commands


class Ping:
    """Ping class."""

    def __init__(self, bot):
        """Init method for Ping."""
        self.bot = bot

    @commands.command()
    async def ping(self):
        """Simple command to test the bot.

        :return: Pong!
        """
        await self.bot.say(":ping_pong: Pong!")


def setup(bot):
    """Cog setup method."""
    bot.add_cog(Ping(bot))
