#!/usr/bin/env python
# -*- coding: utf-8 -*- 

class Openerp:
    def __init__(self, base_path):
        self.logger = None
        self.base_path = base_path
        self.addons = []


    def setLogger(self, logger):
        self.logger = logger


    def setAddons(self, addons):
        self.addons = addons


    def showConfig(self):
        print self._buildOpenerpConfig()


    def writeConfig(self):
        addons_path = self._buildOpenerpConfig()


    def _buildOpenerpConfig(self):
        return 'addons_path = ' + ','.join(self.addons)