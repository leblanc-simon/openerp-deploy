#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os
import logging

class Logger:
    def __init__(self, filename = None):
        self.root_logger = logging.getLogger('deploy')

        if filename is not None:
            self._initWithFile(filename)

        self._initConsole()


    def _initWithFile(self, filename):
        """
        Défini le logging dans un fichier

        :param filename: le chemin du fichier pour les logs
        """
        # The handler of the file
        if filename[:1] != '/':
            filename = os.path.normpath(os.path.join(os.getcwd(), filename))

        logfile = logging.FileHandler(filename)
        self._initLogger(logfile)


    def _initConsole(self):
        """
        Défini le logging dans la console
        """
        # The handler of the console
        console = logging.StreamHandler()
        self._initLogger(console)


    def _initLogger(self, handler):
        self.root_logger.setLevel(logging.DEBUG)

        # Formate the message
        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)

        # Add the handle to the logging
        self.root_logger.addHandler(handler)


    def getLogger(self):
        """
        Retourne l'objet permettant de générer des logs

        :returns: Logger
        """
        return self.root_logger