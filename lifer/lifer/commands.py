import os
import subprocess

import shutil

from snake import config
from snake import error
from snake import scale


class Commands(scale.Commands):
    def check(self):
        self.lifer_path = None
        if config.scale_configs['lifer']['lifer_path']:
            if os.path.exists(config.scale_configs['lifer']['lifer_path']):
                self.lifer_path = config.scale_configs['lifer']['lifer_path']
        else:
            self.lifer = shutil.which("lifer")
        if not self.lifer_path:
            raise error.CommandError("binary 'lifer' not found")

    @scale.command({
        'info': 'This function will return all strings found within the file passed'
    })
    def all_strings(self, args, file, opts):
        try:
            proc = subprocess.run([self.lifer_path, file.file_path],
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)
        except TimeoutError:
            raise error.CommandWarning("timeout when running lifer")

        if proc.stderr:
            raise error.CommandWarning("an error occurred with the lifer module:\n%s" % proc.stderr.decode('utf-8'))

        if proc.stdout == '':
            raise error.CommandWarning("lifer all strings returned no output")

        return {'all_strings': proc.stdout.decode('utf-8')}

    def all_strings_plaintext(self, json):
        return json['all_strings']

    @scale.command({
        'info': 'This function will return lifer decoded strings found within the file passed'
    })
    def decoded_strings(self, args, file, opts):
        try:
            proc = subprocess.run([self.lifer_path, file.file_path, '--no-static-strings', '--no-stack-strings'],
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)
        except TimeoutError:
            raise error.CommandWarning("timeout when running lifer")

        if proc.stderr:
            raise error.CommandWarning("an error occurred with the lifer module:\n%s" % proc.stderr.decode('utf-8'))

        if proc.stdout == '':
            raise error.CommandWarning("lifer decoded strings returned no output")

        return {'decoded_strings': proc.stdout.decode('utf-8')}

    def decoded_strings_plaintext(self, json):
        return json['decoded_strings']

    @scale.command({
        'info': 'This function will return lifer stack strings found within the file passed'
    })
    def stack_strings(self, args, file, opts):
        try:
            proc = subprocess.run([self.lifer_path, file.file_path, '--no-static-strings', '--no-decoded-strings'],
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)
        except TimeoutError:
            raise error.CommandWarning("timeout when running lifer")

        if proc.stderr:
            raise error.CommandWarning("an error occurred with the lifer module:\n%s" % proc.stderr.decode('utf-8'))

        if proc.stdout == '':
            raise error.CommandWarning("lifer stack strings returned no output")

        return {'stack_strings': proc.stdout.decode('utf-8')}

    def stack_strings_plaintext(self, json):
        return json['stack_strings']
