"""Module containing utils methods."""

import argparse
import configparser
import logging


def parse_args():
    """It creates an instance of ArgumentParser."""
    parser = argparse. ArgumentParser()
    parser.add_argument('-c', '--config', help='config file', required=True,
                        dest='config_file', default='config.ini', type=str)
    return parser.parse_args()


def load_config(config_file):
    """It loads and return the config file."""
    config = configparser.ConfigParser(allow_no_value=True)
    config.read(config_file)
    return config


def setup_logging(log_level=logging.DEBUG, log_file='discord.log'):
    """It sets up logging for the application."""
    logger = logging.getLogger('discord')
    logger.setLevel(log_level)
    handler = logging.FileHandler(filename=log_file, encoding='utf-8',
                                  mode='w')
    handler.setFormatter(logging.Formatter(
        '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
    logger.addHandler(handler)
