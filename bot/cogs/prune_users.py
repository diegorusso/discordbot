"""PruneUsers module."""

import asyncio


class PruneUsers(object):
    """PruneUsers class."""

    def __init__(self, bot):
        """Init method for PruneUsers."""
        self.bot = bot
        server_id = self.bot.config['general']['server_id']
        inactive_days = int(self.bot.config['prune_users']['inactive_days'])
        bg_interval = int(self.bot.config['prune_users']['bg_interval'])
        self.bot.loop.create_task(
            self._setup_prune(server_id, inactive_days, bg_interval))

    async def _setup_prune(self, server_id, inactive_days, bg_interval):
        """Setup prune users."""
        await self.bot.wait_until_ready()
        server = self.bot.get_server(server_id)
        to_prune = False
        while not self.bot.is_closed:
            # OK, let's prune them all!
            if to_prune:
                pm = self.bot.prune_members(server=server, days=inactive_days)
                message = "I've pruned {} members because inactive for {} days"
                await self.bot.say(message.format(pm, inactive_days))
                to_prune = False
            # I try to give a warning before the actual pruning
            epm = await self.bot.estimate_pruned_members(server=server,
                                                         days=inactive_days)
            if epm:
                message = "{} members will be pruned in {} hours because " \
                          "inactive for {} days"
                await self.bot.say(message.format(epm, bg_interval/3600,
                                                  inactive_days))
                to_prune = True
            await asyncio.sleep(bg_interval)


def setup(bot):
    """Cog setup method."""
    bot.add_cog(PruneUsers(bot))
