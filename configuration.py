# -*- coding: utf-8 -*-
from pathlib import Path
from ruamel.yaml import load, dump, Loader

def read_config():
    defaultConfigPath = Path(Path(__file__).parent, 'default.yaml')
    with open(defaultConfigPath , 'r') as defaultConfigFile:
        defaultConf = load(defaultConfigFile, Loader=Loader)    
    return defaultConf

config = read_config()