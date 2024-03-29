#!/usr/bin/ python
# -*- coding: utf-8 -*-

import os
from Config import *

def get_config():
    #default environment is Development
    env = os.environ.get('ENV', 'Dev')
    if env == 'Dev':
        return DevelopmentConfig
    elif env == 'Prod':
        return ProductionConfig

app_config = get_config()