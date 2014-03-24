#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os, urllib

class Download:
    def __init__(self, base_path):
        self.logger = None
        self.base_path = base_path


    def setLogger(self, logger):
        self.logger = logger


    def process(self, downloads):
        return_value = True
        for folder in downloads:
            real_folder = os.path.normpath(os.path.join(self.base_path, folder))
            self._initFolder(real_folder)

            for filename in downloads[folder]:
                real_filename = os.path.normpath(os.path.join(real_folder, filename))
                if not self._download(downloads[folder][filename], real_filename):
                    return_value = False

        return return_value


    def _initFolder(self, folder):
        if not os.path.exists(folder):
            self.logger.debug('Create "{0}" directory'.format(folder))
            os.makedirs(folder)


    def _download(self, url, filename):
        try:
            self.logger.info('Download "{0}" in "{1}"'.format(url, filename))
            urllib.urlretrieve(url, filename)
            return True

        except Exception as e:
            self.logger.error('Fail to download "{0}" : {1}'.format(url, str(e)))
            return False