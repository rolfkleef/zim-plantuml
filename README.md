zim-plantuml
============

Plugin for Zim to work with PlantUML diagrams

PlantUML
========

PlantUML lets you quickly write UML diagrams in plain text:

* sequence diagram,
* use case diagram,
* class diagram,
* activity diagram,
* component diagram,
* state diagram
* object diagram
* wireframe graphical interface

http://plantuml.sourceforge.net

Zim
===

Zim is a graphical text editor used to maintain a collection of 
wiki pages on your local machine.

http://zim-wiki.org

Zim can be extended with plugins. The Ditaa plugin lets you work with
GraphViz diagrams.

Install
=======

A bit of a hack:

* Download `plantuml.jar` from http://sourceforge.net/projects/plantuml/files/plantuml.jar/download
* Put it somewhere in your path and make it executable

* Fork or download this repo.
* Put `plantuml` somewhere in your path.
* Put `my-style.plantuml` in the same directory, and adapt as you like.
* Copy or symlink the Zim plugin

On Ubuntu:
  
  sudo cp zim-plugin/plantumleditor.py /usr/lib/python2.7/dist-packages/zim/plugins
  
* Close all Zim instances, and restart it. Under menu Edit > Preferences, you should be able to enable the plugin now.

