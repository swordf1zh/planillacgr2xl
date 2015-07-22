#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, datetime
from rth_helper_cls import *

def get_metodos(object,showValor=False):
    metodos = [metodo for metodo in dir(object) if hasattr(getattr(object, metodo), '__call__')]
    for metodo in metodos:
        if showValor: print '%s: %s' % (metodo, str(object[metodo]))
        else: print metodo

def get_propiedades(object,showValor=False):
    propiedades = [propiedad for propiedad in dir(object) if not hasattr(getattr(object, propiedad), '__call__')]
    for propiedad in propiedades:
        if showValor: print '%s: %s' % (propiedad, str(object[propiedad]))
        else: print propiedad

def ver_objeto(object,showValor=False):
    print_titulo('Métodos:')
    get_metodos(object,showValor)
    
    print_titulo('Propiedades:')
    get_propiedades(object,showValor)

def print_titulo(titulo):
    print u'\n\n%s\n%s' % (titulo, '-' * len(titulo))

def getExtension(name):
    filename = os.path.abspath(name)
    if filename:
        head, filext = os.path.split(filename)
        name, extension = os.path.splitext(filext)
        return extension

def printToFile(msg, title = False, rep = False):
    lineASCII = str(msg)
    lineUnicode = unicode( lineASCII, "utf-8" )
    if title:
        print_titulo(lineUnicode)
    else:
        print lineUnicode + '\n',

    '''
    fileName = 'outputREP.txt' if (rep) else 'output.txt'
    file = open(fileName, 'a')
    file.write(line)
    file.close()
    '''

def getMyDate(dateLike):
    date = ''
    if isinstance(dateLike, datetime.date):
        return str(dateLike.year)[-2:] + \
               str(dateLike.month).rjust(2,'0') + \
               str(dateLike.day).rjust(2,'0')

    else:
        splitBy = '/' if (dateLike.find('/') > -1) else '-'
        for d in dateLike.split(splitBy):
            date += d[-2:]
        return date

def printTxtHeader(titl, ver):
    dev = ['Desarrollado por:',\
           'Ricardo Tribaldos H.',\
           '<ricardo@tribaldos.org>']

    txtHeader = TxtTitleBox(titl)
    txtHeader.addLinea(ver)
    txtHeader.addLinea()
    txtHeader.addLinea(dev, 'r')

    print txtHeader.getBox()