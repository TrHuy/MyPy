from distutils.core import setup

import py2exe

setup (windows = [{"script":'FirstPro.py', "icon_resources":[(1,"FirstProicon.png")]}])