#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os, shutil, sys, subprocess

class Execute:
    def __init__(self, base_path):
        self.logger = None
        self.base_path = base_path


    def setLogger(self, logger):
        self.logger = logger


    def process(self, processes):
        return_value = True
        for process in processes:
            if not self._execute(process):
                return_value = False

        return return_value


    def _execute(self, process):
        try:
            self.logger.info('Execute "' + ' '.join(process) + '"')

            os.chdir(self.base_path)

            process = subprocess.Popen(process, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
            (stdout, stderr) = process.communicate()
            if process.returncode != 0:
                raise Exception(stderr)

            return True
            
        except Exception as e:
            self.logger.error(str(e))
            return False