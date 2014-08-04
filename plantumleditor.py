# -*- coding: utf-8 -*-
#
# plantumleditor.py
# (based on ditaaeditor.py)
#
# This is a plugin for Zim, to include PlantUML diagrams
#
# Author: Rolf Kleef <rolf@drostan.org>
# Original Author: Yao-Po Wang <blue119@gmail.com>
# Date: 2014-08-04
# Copyright (c) 2012, 2014, released under the GNU GPL v2 or higher
#
#

from zim.plugins.base.imagegenerator import ImageGeneratorPlugin, ImageGeneratorClass
from zim.fs import File, TmpFile
from zim.config import data_file
from zim.applications import Application, ApplicationError


# TODO put these commands in preferences
dotcmd = ('plantuml')


class InsertPlantumlPlugin(ImageGeneratorPlugin):

	plugin_info = {
		'name': _('Insert PlantUML'), # T: plugin name
		'description': _('''\
This plugin provides a diagram editor for zim based on PlantUML.
'''), # T: plugin description
        'help': 'Plugins:PlantUML Editor',
		'author': 'Adaptation by Rolf Kleef of Ditaa plugin by Yao-Po Wang',
	}

	object_type = 'plantuml'
	short_label = _('PlantUML') # T: menu item
	insert_label = _('Insert PlantUML') # T: menu item
	edit_label = _('_Edit PlantUML') # T: menu item
	syntax = None

	@classmethod
	def check_dependencies(klass):
		has_dotcmd = Application(dotcmd).tryexec()
		return has_dotcmd, [("Plantuml", has_dotcmd, True)]


class PlantumlGenerator(ImageGeneratorClass):

	uses_log_file = False

	object_type = 'plantuml'
	scriptname = 'plantuml.pu'
	imagename = 'plantuml.png'

	def __init__(self, plugin):
		ImageGeneratorClass.__init__(self, plugin)
		self.dotfile = TmpFile(self.scriptname)
		self.dotfile.touch()
		self.pngfile = File(self.dotfile.path[:-3] + '.png') # len('.pu') == 3

	def generate_image(self, text):
		if isinstance(text, basestring):
			text = text.splitlines(True)

		# Write to tmp file
		self.dotfile.writelines(text)

		# Call PlantUML
		try:
			dot = Application(dotcmd)
			dot.run(('', self.dotfile))
		except ApplicationError:
			return None, None # Sorry, no log
		else:
			return self.pngfile, None

	def cleanup(self):
		self.dotfile.remove()
		self.pngfile.remove()
