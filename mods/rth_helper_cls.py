#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

class Filename:
    def __init__(self, name):
        self.filename = os.path.abspath(name)
        if self.filename:
            self.head, self.filext = os.path.split(self.filename)
            self.name, self.extension = os.path.splitext(self.filext)
            self.isFile = os.path.isfile(name)
            self.isDir = os.path.isdir(name)


class MyException(Exception):
    def __init___(self,dErrorArguments):
        Exception.__init__(self,"my exception was raised with arguments {0}".format(dErrorArguments))
        self.dErrorArguments = dErrorArguments