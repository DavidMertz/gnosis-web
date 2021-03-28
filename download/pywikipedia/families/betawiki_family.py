# -*- coding: utf-8  -*-

import family

# The official Beta Wiki.

class Family(family.Family):
    name = 'betawiki' #Set the family name; this should be the same as in the filename.

    def __init__(self):
        family.Family.__init__(self)
        self.langs = {
            'en': 'www.ucip.org', #Put the hostname here.
        }
        self.namespaces[4] = {
            '_default': u'BetaWiki', #Specify the project namespace here. Other
        }                               #namespaces will be set to MediaWiki default.

        self.namespaces[5] = {
            '_default': u'BetaWiki talk',
        }

    def version(self, code):
        return "1.5.4"  #The MediaWiki version used. Not very important in most cases.

    def path(self, code):
        return '/beta/index.php' #The path of index.php
