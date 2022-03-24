#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import environ

def settings():

    """
    Setup domain and api environemnt
    """

    return {
            "DEBUG": True,
            "RENDERERS": ['eve.renderer.JSONRender'],
            "MONGO_URI": environ.get("DB_URI", "mongodb://db:27017/test"),
            "X_DOMAINS": ['*', 'http://editor.swagger.io' ],
            "X_HEADERS": ['Content-Type', 'If-Match'],
            "DOMAIN": {
                "test": {},
                "username": {
                    "type": str(),
                    "minlength": 5,
                    "maxlength": 25,
                }
            }
    }
