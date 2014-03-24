#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os, shutil, sys, subprocess

class Library:
    def __init__(self, base_path):
        self.logger = None
        self.base_path = base_path


    def setLogger(self, logger):
        self.logger = logger


    def process(self, libraries):
        return_value = True
        for library in libraries:
            if not self._pipInstall(library):
                return_value = False

        return return_value


    def _pipInstall(self, library):
        """
        Installe une bibliothèque Python via pip

        :param library: le nom de la bibliothèque à installer (avec si nécessaire sa version library==version)
        :type library: str
        :returns: bool -- Vrai en cas de succès, faux si une erreur survient
        """
        try:
            self.logger.info('Install library : "{0}"'.format(library))

            process = subprocess.Popen(['pip', 'install', library], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            (stdout, stderr) = process.communicate()
            if process.returncode != 0:
                raise Exception(stderr)

            return True
        except Exception as e:
            self.logger.error(str(e))
            return False