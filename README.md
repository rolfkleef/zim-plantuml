zim-plantuml
============

Plugin for Zim to work with PlantUML diagrams. You can define a default style for your diagrams.

![](https://raw.githubusercontent.com/rolfkleef/zim-plantuml/master/plantuml-sample.png)

PlantUML
========

PlantUML lets you write UML diagrams in plain text. The source for the diagram above

```
@startuml

actor hacker
actor user

hacker -left- (Adapts Ditaa plugin)
note top: Simple adaptation

cloud GitHub {
    hacker -> (Uploads PlantUML plugin)
    user <- (Downloads PlantUML plugin)
}

hacker - (Uses UML diagrams in Zim)
user - (Uses UML diagrams in Zim)

@enduml
```

http://plantuml.sourceforge.net

Zim
===

Zim is a graphical text editor used to maintain a collection of 
wiki pages on your local machine.

http://zim-wiki.org

Zim can be extended with plugins. The Ditaa plugin lets you work with
GraphViz diagrams. This PlantUML plugin is a simple adaptation of the Ditaa plugin.

Install
=======

A bit of a hack:

* Download `plantuml.jar` from http://sourceforge.net/projects/plantuml/files/plantuml.jar/download
* Put it somewhere in your path and make it executable

* Fork or download this repo.
* Put `plantuml` somewhere in your path and make it executable.
* Put `my-style.plantuml` in the same directory, and adapt as you like for your default style settings.
* Copy or symlink the Zim plugin:

> Ubuntu 16.04:
> 
> * Make the local directory for plugins (if needed)
>   `mkdir $HOME/.local/share/zim/plugins/`
> * Copy the plugin to the directory you just created.
>   `cp zim-plugin/plantumleditor.py $HOME/.local/share/zim/plugins/`
>
> Ubuntu 13.10:
>
> * Check which Python version Zim uses (on Ubuntu 13.10 it uses version 2.7, with a system-wide directory for plugins `/usr/lib/python2.7/dist-packages/zim/plugins`)
> * Make the local directory for plugins (if needed)
>   `mkdir $HOME/.local/lib/python2.7/site-packages/zim/plugins`
> * Copy the plugin to the directory you just created.
>   `cp zim-plugin/plantumleditor.py $HOME/.local/lib/python2.7/site-packages/zim/plugins`

* Close all Zim instances, and restart Zim. Under menu Edit > Preferences, you should be able to enable the plugin now.
