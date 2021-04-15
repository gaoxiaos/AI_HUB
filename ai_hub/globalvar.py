#!/usr/bin/python
# -*- coding: utf-8 -*-

def _init():
    global _global_dict
    _global_dict = {}
    _global_dict["show_exception"] = True

def set_value(name, value):
    _global_dict[name] = value

def get_value(name, defValue=None):
    try:
        return _global_dict[name]
    except KeyError:
        return defValue
