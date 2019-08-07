init -98 python:
    menuz.insert(find_in_nested_list(menuz, "Settings")[0]+1, [0,0,0,1,_("Extras"),ShowMenu("extras")])
init offset = -1

## Help screen #################################################################

default help_hover = 0

screen help():
    tag menu
    default device = "keyboard"
    use game_menu(_("Help")):
        style_prefix "hlp"
        text "no help"

## About screen ################################################################

screen about():
    tag menu
    use game_menu(_("About")):
        style_prefix "abt"
        frame:
            xsize 1000
            has vbox
            label "[config.name!t]"
            text _("Version [config.version!t]\n")
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")

define gui.about = ""