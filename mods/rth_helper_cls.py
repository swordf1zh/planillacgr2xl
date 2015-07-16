#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

class Filename:
    def __init__(self, name):
        self.filename = os.path.abspath(name)
        if self.filename:
            self.head, self.filext = os.path.split(self.filename)
            self.name, self.extension = os.path.splitext(self.filext)