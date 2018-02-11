"""Main app."""

import logging
import traceback

from discord.ext import commands


class DiscordBot(commands.Bot):
    """Bot class."""

    def __init__(self, config):
        """Init method for DiscordBot."""
        self.config = config
        self._parse_config(config)

        super().__init__(command_prefix=self.config_command_prefix,
                         description=self.config_description, pm_help=True,
                         help_attrs=dict(hidden=True))

        for extension in self.config_extensions:
            try:
                self.load_extension(extension)
            except Exception as e:
                logging.error('Failed to load extension {}.'.format(extension))
                traceback.print_exc()

    def run(self):
        """Run method for DiscordBot."""
        super().run(self.config_token, reconnect=True)

    def _parse_config(self, config):
        """Method for parsing config options."""
        self.config_token = config["general"]["token"]
        self.config_description = config["general"]["description"]
        self.config_command_prefix = config["general"]["command_prefix"]
        self.config_extensions = list(config["extensions"].keys())


def run_bot(config):
    """Method for running DiscordBot."""
    bot = DiscordBot(config)
    bot.run()
