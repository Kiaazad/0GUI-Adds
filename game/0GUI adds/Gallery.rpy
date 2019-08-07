# init -98 python:
#     menuz.insert(find_in_nested_list(menuz, "Settings")[0]+1, [0,0,0,1,_("Gallery"),ShowMenu("gallery")])

# # [0 for locked 1 for unlocked, "images name", "images address"]
# default persistent.gall = [
#     [1,"add your images to gallery.rpy","gui/window_icon.png"],
#     [1,"a very very long name for an image","gallery/1234.jpg"],
#     [0,"what is this?","gallery/5420.jpg"],
#     [1,"No 1","gallery/12342.jpg"],
#     [1,"Something...","gallery/000.PNG"],
#     [1,"name","gallery/00.PNGg"],
#     ]

# screen gallery(gall):
#     tag menu
#     style_prefix "gal"
#     modal True
    
#     default gallno = 0

#     #################################### the key navigation
#     key 'K_LEFT' action If(gallno > 0, SetScreenVariable("gallno", gallno-1), SetScreenVariable("gallno", (len(gall)-1)))
#     key 'K_RIGHT' action If(gallno < (len(gall)-1), SetScreenVariable("gallno", gallno+1), SetScreenVariable("gallno", 0))

#     #################################### the image
#     add "#666"
#     if gall[gallno][0] == 0:
#         text "Locked"
#     else:
#         add gall[gallno][2] align(.5,1.0)
#         frame:
#             align(.5,0.0)
#             text str(gall[gallno][1])
    
#     #################################### the side buttons
#     button:
#         xalign 0.0 yfill True xsize 400
#         text "back"
#         action If(gallno > 0, SetScreenVariable("gallno", gallno-1), SetScreenVariable("gallno", (len(gall)-1)))
#     button:
#         xalign 1.0 yfill True xsize 400
#         text "next"
#         action If(gallno < (len(gall)-1), SetScreenVariable("gallno", gallno+1), SetScreenVariable("gallno", 0))

#     #################################### the floating navigation
#     drag:
#         frame:
#             has hbox
#             textbutton _("X") action Return() at btn align(.5,1.0)
#             button:
#                 text "<"
#                 action If(gallno > 0, SetScreenVariable("gallno", gallno-1), SetScreenVariable("gallno", (len(gall)-1)))
#             button:
#                 text ">"
#                 action If(gallno < (len(gall)-1), SetScreenVariable("gallno", gallno+1), SetScreenVariable("gallno", 0))
#             text str(gallno+1)+ " - " + str(gall[gallno][1])

#     #################################### the return button
#     textbutton _("Return") action Return() at btn align(.5,1.0)
        

# style gal_text:
#     hover_color "#fff"
# style gal_button:
#     idle_background None
#     hover_background "#fff3"
    