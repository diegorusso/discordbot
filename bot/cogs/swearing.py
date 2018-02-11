"""Swearing module."""

import json

import requests
from discord.ext import commands


class Swearing(object):
    """Swearing class."""

    def __init__(self, bot):
        """Init method for Swearing."""
        self.bot = bot

    @commands.command(name='bestemmia')
    async def italian_random_swearing(self):
        """Fetch and say an italian random swearing."""
        r = requests.get('http://www.bestemmie.org/api/bestemmie/random')
        bestemmia = json.loads(r.text)[0]
        await self.bot.say(bestemmia.get('bestemmia_low'))


def setup(bot):
    """Cog setup method."""
    bot.add_cog(Swearing(bot))
