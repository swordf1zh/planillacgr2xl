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


class TxtTitleBox:

    def __init__(self, titulo):
        self.width = len(titulo)
        self.boxContents = []
        self.addTitulo(titulo)


    def vborder(self):
        border = '-' * (self.width + 2)
        return '*%s*' % border


    def padText(self, text, pos='c'):
        if pos == 'c': padded = text.center(self.width)
        elif pos == 'l': padded = text.ljust(self.width)
        elif pos == 'r': padded = text.rjust(self.width)
        return ' %s ' % padded


    def addTitulo(self, titulo):
        self.boxContents.append('|%s|' % self.padText(titulo.upper()))
        self.boxContents.append('|%s|' % self.padText('-' * len(titulo)))


    def addEspacio(self):
        return '|%s|' % self.padText('')


    def addLinea(self, linea='', pos='c'):
        if isinstance(linea, list):
            for l in linea:
                self.boxContents.append('|%s|' % self.padText(l, pos))
        else:
            self.boxContents.append('|%s|' % self.padText(linea, pos))


    def makeBox(self):
        box = []
        box.append(self.vborder())
        box.append(self.addEspacio())
        for linea in self.boxContents:
            box.append(linea)
        box.append(self.addEspacio())
        box.append(self.vborder())
        return box


    def getBox(self):
        box = self.makeBox()
        return '\n'.join(box)