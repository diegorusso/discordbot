"""Main application."""

import sys
from utils import parse_args, load_config, setup_logging

from bot.app import run_bot

if __name__ == '__main__':
    args = parse_args()
    config = load_config(args.config_file)
    setup_logging(config['logging']['level'], config['logging']['logfile'])
    run_bot(config)
