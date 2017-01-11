#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# main.py

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Control import Control
from View import View
from Model import Model


import sqlite3
import sys
import os


def main(args) :
	"""Fonction principal qui va nous lancer notre annuaire"""	
	#bdd = sqlite3.connect('Bdd/patron.db')
	
	app=QApplication(args)
	control = Control()
	model = Model(control)
	fenetre = View(control);
	fenetre.show();
	
	#bdd.close()
	return app.exec_()

if __name__ == "__main__" :
	os.system('clear')
	main(sys.argv)
