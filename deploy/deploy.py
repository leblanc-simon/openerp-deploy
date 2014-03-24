#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os
import json

import logger
import bzr, execute, download, library, openerp

class Deploy:
    def __init__(self, filename, log = None):
        o_logger = logger.Logger(log)
        self.logger = o_logger.getLogger()

        self.base_path = None
        self.filename = None
        self.without_openerp = False
        self.addons = []

        self._initFilename(filename)


    def process(self):
        """
        """
        # Parse JSON
        app_file = open(self.filename, 'r')
        app_json = json.loads(app_file.read())

        self.logger.info('Processing of {0} {1}'.format(app_json['name'], app_json['version']))

        obzr = bzr.Bzr(self.base_path)
        obzr.setLogger(self.logger)

        oexecute = execute.Execute(self.base_path)
        oexecute.setLogger(self.logger)

        odownload = download.Download(self.base_path)
        odownload.setLogger(self.logger)

        olibrary = library.Library(self.base_path)
        olibrary.setLogger(self.logger)

        # Execute pre-execute
        if 'pre-execute' in app_json:
            self.logger.info('Process pre-execute...')
            oexecute.process(app_json['pre-execute'])

        # get Openerp
        if not self.without_openerp and "openerp" in app_json:
            self.logger.info('Process OpenERP framework...')
            obzr.process(app_json['openerp'], 'framework')

        # get Addons
        if 'addons' in app_json:
            if 'enova' in app_json['addons']:
                self.logger.info('Process Enova\'s addons...')
                obzr.process(app_json['addons']['enova'], 'enova')
            if 'extras' in app_json['addons']:
                self.logger.info('Process Extras\' addons...')
                obzr.process(app_json['addons']['extras'], 'extras')
            
        # get libraries
        if 'libraries' in app_json:
            self.logger.info('Process libraries...')
            olibrary.process(app_json['libraries'])

        # download somes files
        if 'download' in app_json:
            self.logger.info('Process download...')
            odownload.process(app_json['download'])

        # Execute post-execute
        if 'post-execute' in app_json:
            self.logger.info('Process post-execute...')
            oexecute.process(app_json['post-execute'])

        self.addons = obzr.getAddons()


    def showOpenerpConfig(self):
        oopenerp = openerp.Openerp(self.base_path)
        oopenerp.setLogger(self.logger)
        oopenerp.setAddons(self.addons)
        oopenerp.showConfig()


    def setBasePath(self, path):
        """
        """
        if path[:1] == '/':
            self.base_path = path
        else:
            self.base_path = os.path.normpath(os.path.join(os.getcwd(), path))

        self.logger.debug('The base path is : %s' % self.base_path)



    def setWithoutOpenerp(self, value):
        self.without_openerp = value


    def _initFilename(self, filename):
        """
        """
        if filename[:1] != '/':
            filename = os.path.normpath(os.path.join(os.getcwd(), filename))

        if os.path.exists(filename) == False:
            self.logger.error('%s doesn\'t exist' % filename)
            raise Exception('%s doesn\'t exist' % filename)

        self.filename = filename

        self.logger.debug('The app filename is : %s' % filename)