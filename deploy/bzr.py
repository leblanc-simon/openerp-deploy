#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os, shutil, sys, subprocess

class Bzr:
    def __init__(self, base_path):
        self.logger = None
        self.base_path = base_path
        self.addons_path = os.path.join(self.base_path, 'addons')
        self.addons_enova_path = os.path.join(self.addons_path, 'enova')
        self.addons_extras_path = os.path.join(self.addons_path, 'extras')
        self.framework_path = os.path.join(self.base_path, 'framework')

        self.branch_paths = {
            "enova": self.addons_enova_path,
            "extras": self.addons_extras_path,
            "framework": self.framework_path
        }

        self.addons = []

        self._createStructure()


    def setLogger(self, logger):
        self.logger = logger


    def process(self, branches, name):
        return_value = True
        for branch in branches:
            folder = os.path.join(self.branch_paths[name], branch)
            if self._importBranch(branches[branch], folder):
                self.addons.append(folder)
            else:
                return_value = False

        return return_value


    def getAddons(self):
        return self.addons


    def _createStructure(self):
        paths = [self.base_path, self.addons_path, self.addons_enova_path, self.addons_extras_path, self.framework_path]
        for path in paths:
            if not os.path.exists(path):
                os.mkdir(path, 0755)


    def _importBranch(self, branch, folder):
        """
        Importe une branche Bazaar dans un dossier

        :param folder: le dossier où mettre la branche
        :type folder: str
        :param branch: le chemin du repository pour récupérer la branche
        :type branch: str
        :returns: bool -- Vrai en cas de succès, faux si une erreur survient
        """
        try:
            self.logger.info('Set branch "' + branch + '" in "' + folder + '"')

            parent_folder = os.path.dirname(folder)
            if not os.path.exists(parent_folder):
                os.makedirs(parent_folder)
            if os.path.exists(folder):
                shutil.rmtree(folder)

            process = subprocess.Popen(['bzr', 'branch', branch, folder], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            (stdout, stderr) = process.communicate()
            if process.returncode != 0:
                raise Exception(stderr)

            return True
            
        except Exception as e:
            self.logger.error(str(e))
            return False
