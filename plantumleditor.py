# -*- coding: utf-8 -*-
#
# plantumleditor.py
# (based on ditaaeditor.py)
#
# This is a plugin for Zim, to include PlantUML diagrams
#
# Author: Rolf Kleef <rolf@drostan.org>
# Original Author: Yao-Po Wang <blue119@gmail.com>
# Date: 2014-03-25
# Copyright (c) 2012, 2014, released under the GNU GPL v2 or higher
#
#

import gtk

from zim.fs import File, TmpFile
from zim.plugins import PluginClass
from zim.config import data_file
from zim.applications import Application, ApplicationError
from zim.gui.imagegeneratordialog import ImageGeneratorClass, ImageGeneratorDialog
from zim.gui.widgets import populate_popup_add_separator

# TODO put these commands in preferences
dotcmd = ('plantuml')

ui_xml = '''
<ui>
	<menubar name='menubar'>
		<menu action='insert_menu'>
			<placeholder name='plugin_items'>
				<menuitem action='insert_plantuml'/>
			</placeholder>
		</menu>
	</menubar>
</ui>
'''

ui_actions = (
	# name, stock id, label, accelerator, tooltip, read only
	('insert_plantuml', None, _('PlantUML...'), '', _('Insert PlantUML'), False),
		# T: menu item for insert diagram plugin
)


class InsertPlantumlPlugin(PluginClass):

	plugin_info = {
		'name': _('Insert PlantUML'), # T: plugin name
		'description': _('''\
This plugin provides a diagram editor for zim based on PlantUML.
'''), # T: plugin description
        'help': 'Plugins:PlantUML Editor',
		'author': 'Adaptation by Rolf Kleef of Ditaa plugin by Yao-Po Wang',
	}

	@classmethod
	def check_dependencies(klass):
		has_dotcmd = Application(dotcmd).tryexec()
		return has_dotcmd, [("plantuml", has_dotcmd, True)]

	def __init__(self, ui):
		PluginClass.__init__(self, ui)
		if self.ui.ui_type == 'gtk':
			self.ui.add_actions(ui_actions, self)
			self.ui.add_ui(ui_xml, self)
			self.register_image_generator_plugin('plantuml')

	def insert_plantuml(self):
		dialog = InsertPlantumlDialog.unique(self, self.ui)
		dialog.run()

	def edit_object(self, buffer, iter, image):
		dialog = InsertPlantumlDialog(self.ui, image=image)
		dialog.run()

	def do_populate_popup(self, menu, buffer, iter, image):
		populate_popup_add_separator(menu, prepend=True)

		item = gtk.MenuItem(_('_Edit PlantUML')) # T: menu item in context menu
		item.connect('activate',
			lambda o: self.edit_object(buffer, iter, image))
		menu.prepend(item)



class InsertPlantumlDialog(ImageGeneratorDialog):

	def __init__(self, ui, image=None):
		generator = PlantumlGenerator()
		ImageGeneratorDialog.__init__(self, ui, _('Insert PlantUML'), # T: dialog title
            generator, image, help=':Plugins:PlantUML Editor' )


class PlantumlGenerator(ImageGeneratorClass):

	uses_log_file = False

	type = 'plantuml'
	scriptname = 'plantuml.pu'
	imagename = 'plantuml.png'

	def __init__(self):
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
