#!/usr/bin/env python

from __future__ import (absolute_import, division, print_function)
from subprocess import check_output
from ansible.plugins.lookup import LookupBase
__metaclass__ = type


class LookupModule(LookupBase):

    def run(self, terms, varibles=None, **kwargs):
        result = []

        for term in terms:
            var = term.split()[0]

            out = check_output("pass {}".format(var), shell=True).rstrip()
            if 'Error:' in out:
                # Not found, generate
                out = check_output("pass generate {} 20".format(var), shell=True).rstrip()
                out = out.replace("\x1b[1m\x1b[37mThe generated password for \x1b[4m{}\x1b[24m is:\x1b[0m\n\x1b[1m\x1b[93".format(var), "")  # Works better than regex...
                out = out.replace("\x1b[0m", "")
            result.append(out)

        return result
