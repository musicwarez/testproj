# -*- coding: utf-8 -*-
import ConfigParser


def read_conf(config, block):
    conf = ConfigParser.RawConfigParser()
    conf.read(config)
    a = {x: y for x,y in conf.items(block)}
    return a


