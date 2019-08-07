init -97 python:
    menuz.insert(find_in_nested_list(menuz, "Settings")[0]+1, [0,0,1,1,_("Help"),ShowMenu("help")])
init offset = -1

   


screen extras:
    style_prefix "nav"
    modal True
    add bgs[2]
    hbox:
        textbutton _("About") action [Hide("extras"), ShowMenu("about")] at btn
        textbutton _("Gallery") action [Hide("extras"), ShowMenu("gallery")] at btn
        textbutton _("Hide") action Hide("extras") at btn
