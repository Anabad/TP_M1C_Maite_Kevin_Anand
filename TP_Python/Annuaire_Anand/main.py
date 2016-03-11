#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# main.py

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from View import View

import sqlite3
import sys


def main(args) :
	"""Fonction principal qui va nous lancer notre annuaire"""
	#bdd = sqlite3.connect('Bdd/patron.db')
	
	app=QApplication(args)
	fenetre = View();
	fenetre.showMaximized();
	
	#bdd.close()
	return app.exec_()

if __name__ == "__main__" :
   main(sys.argv)
