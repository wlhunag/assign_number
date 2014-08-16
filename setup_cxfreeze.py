#-*- coding: utf-8-*-
__author__ = 'Aaron'
import sys

from cx_Freeze import setup, Executable


if sys.platform == "win32":
    base = "Win32GUI"

#因為已經包含下列檔案了，所以就comment掉了
includefiles = [ 'playtext.pyc',"exam.ico",'imageformats/qico4.dll','resources']
#記得要加上C:\Python27\Lib\site-packages\PyQt4\plugins\imageformats 這個資料夾
includes = ['sip', 'PyQt4.QtCore','PyQt4.QtGui','atexit']


setup(
        name = "Assign-number",
        version = "0.5",
        description = u"加上答案標號",
        options = {'build_exe': {'include_files':includefiles,"includes": includes}},
        executables = [Executable("Assign_number_to_question.pyw" ,base = base, icon = "exam.ico")])