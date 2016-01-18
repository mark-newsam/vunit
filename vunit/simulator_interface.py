# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2015-2016, Lars Asplund lars.anders.asplund@gmail.com

"""
Generic simulator interface
"""

import sys
import os


class SimulatorInterface(object):
    """
    Generic simulator interface
    """

    @staticmethod
    def package_users_depend_on_bodies():
        """
        Returns True when package users also depend on package bodies with this simulator
        """
        return False

    @staticmethod
    def find_executable_paths(executable):
        """
        Return a list of all paths found in PATH that contain executable
        """
        path = os.environ['PATH']
        paths = path.split(os.pathsep)

        result = []
        for path in ["."] + paths:
            path = os.path.abspath(path)
            if contains_executable(path, executable):
                result.append(path)
        return result

    def post_process(self, output_path):
        """
        Hook for simulator interface to perform post processing such as creating coverage reports
        """
        pass


def isfile(file_name):
    """
    Case insensitive os.path.isfile
    """
    if not os.path.isfile(file_name):
        return False

    return os.path.basename(file_name) in os.listdir(os.path.dirname(file_name))


def os_executable_name(executable_name):
    """
    Add .exe on Windows
    """
    _, ext = os.path.splitext(executable_name)
    if (sys.platform == 'win32' or os.name == 'os2') and (ext != '.exe'):
        suffix = ".exe"
    else:
        suffix = ""
    return executable_name + suffix


def contains_executable(path, executable_name):
    """
    Returns True if path containts executable named executable_name
    """

    file_name = os.path.abspath(os.path.join(path, os_executable_name(executable_name)))
    return isfile(file_name)
