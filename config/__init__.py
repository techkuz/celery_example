# -*- coding: utf-8 -*-
import os
import sys

import anyconfig

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(os.path.abspath(os.path.join(BASE_DIR)))

config_dir = os.path.join(BASE_DIR, "config")
base_config = anyconfig.open(os.path.join(config_dir, "config.yml"))
config = anyconfig.load(
    [base_config, os.path.join(config_dir, "config.local.yml")],
    ignore_missing=True
)
