#!/usr/bin/env python
__author__ = 'justinarmstrong'

"""
This is an attempt to recreate the first level of
Super Mario Bros for the NES.
"""

import sys
import pygame as pg
from data.main import main
import cProfile


if __name__=='__main__':
    programIcon = pg.image.load('ikon.png')
    pg.display.set_icon(programIcon)
    main()
    pg.quit()
    sys.exit()