#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
baseapi JSON-LD meta data
"""

__all__ = [
     '__author__',
     '__copyright__',
     '__credits__',
     '__email__', 
     '__license__',
     '__maintainer__',
     '__status__',
     '__version__', 
]

__author__ = "Rob Knight, Gavin Huttley, and Peter Maxwell"
__copyright__ = 'Copyright (c) 2011-2018 Digital Bazaar, Inc.'
__credits__ = ["Rob Knight", "Peter Maxwell", "Gavin Huttley","Matthew Wakefield"]
__email__ = "rob@spot.colorado.edu"
__license__ = 'New BSD license'
__maintainer__ = "Rob Knight"
__status__ = "Production"
__version__ = "1.0.1"

from os import environ
from eve import Eve
from eve_swagger import swagger

def settings():
    return {
        "DEBUG": True,
        "API_VERSION": 'v1',
        "RENDERERS": ['eve.render.JSONRenderer'],
        "MONGO_URI": environ("DB_URI", "mongodb://db:27017/test"),
        "X_DOMAINS": ['*', 'http://editor.swagger.io' ],
        "X_HEADERS": ['Content-Type', 'If-Match'],
        "CACHE_CONTROL": 'max-ege=20',
        "CACHE_EXPIRES": 20,
        "RESOURCE_METHODS": ["GET", "DELETE", "POST"],
        "ITEM_METHODS": ["GET", "PUT", "DELETE"],
        "SWAGGER_INFO": {
            'title': 'My Supercool API',
            'version': __version__,
            'description': 'an API description',
            'termsOfService': 'my terms of service',
            'contact': {
                'name': 'nicola',
                'url': 'http://nicolaiarocci.com'
            },
            'license': {
                'name': 'BSD',
                'url': 'https://github.com/pyeve/eve-swagger/blob/master/LICENSE',
            },
            'schemes': ['http', 'https']},
        
        "DOMAIN": {
            "test": {},
            "users": {
                'item_title': 'member',
                'schema': {
                    'username': {
                        "type": str(),
                        "minlength": 5,
                        "maxlength": 25,
                    },
                }
            }
        }
    }


def main():

    port = int(environ.get("PORT", 5000))
    app = Eve(auth=None, settings=settings())
    app.register_blueprint(swagger)

    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
