init -97 python:
    try:
        mmm.add(
            gui0_menu(
                _("Gallery"),
                ShowMenu("gallery"),
                True, False, True
                ),
            )
    except:
        pass


# --------------------------------------------- Classes
init python:
    class gallpic:
        def __init__(self, name, img, icon = None, info = "", align = (0.5, 1.0)):
            self.name = name
            self.img = img
            self.icon = icon
            self.info = info
            self.align = align
            

    class gallery_class:
        def __init__(self, lst, thumbs = 6, type = "thumbs", iconsize = (480,270)):
            self.lst = lst
            self.current = 0
            self.slc = False
            self.thumbs = thumbs
            self.currentPage = 0
            self.type = type
            self.iconsize = iconsize

        def add(self, x, l = 0):
            r = [x, l]
            if r not in self.lst:
                self.lst.append(r)
        def unlock(self, x):
            for i in self.lst:
                if i[0] == x:
                    i[1] = 0
                    break
        def next(self):
            if self.current < len(self.lst)-1:
                self.current += 1
        def back(self):
            if self.current > 0:
                self.current -= 1
        def set(self, x):
            self.current = x
            self.slc = True
        def unset(self):
            self.slc = False
        def nextPage(self):
            if self.currentPage + self.thumbs < len(self.lst):
                self.currentPage += self.thumbs
                self.current = self.currentPage
        def pervPage(self):
            if self.currentPage - self.thumbs > -1:
                self.currentPage -= self.thumbs
                self.current = self.currentPage
        def toggle(self):
            if self.type == "thumbs":
                self.type = "simple"
            else:
                self.type = "thumbs"
        def thumbsless(self):
            if self.thumbs - 1 > 0:
                self.thumbs -= 1
        def thumbsmore(self):
            if self.thumbs + 1 <  len(self.lst)+1:
                self.thumbs += 1
        def ret(self):
            return eval(self.lst[self.current][0]), self.lst[self.current][1]
        def retthumb(self, x):
            return eval(self.lst[x][0]), self.lst[x][1]

screen gallery(g=gallery_1):
    tag menu
    modal True
    default hovbar = 0
    default settings = 0

    # ----- BackGround
    add "#666"

    # ----- the key navigation
    key 'd' action Function(g.next)
    key 'a' action Function(g.back)

    # ----- Selector
    if g.type == "thumbs":
        use gallery_thumbnail
    elif g.type == "simple":
        use gallery_simple

    # ----- the floating navigation
    if hovbar:
        drag:
            frame:
                has hbox
                textbutton _("✖") action SetScreenVariable("hovbar", 0) at btn align(.5,1.0)
                button:
                    text "<"
                    action Function(g.back)
                button:
                    text ">"
                    action Function(g.next)
                text "{} - {}".format(g.ret()[0].name, g.ret()[0].info) hover_color "#fff"

    # ----- the return button
    hbox:
        align 0.5,1.0
        textbutton _("⚙") action ToggleScreenVariable("settings", 1, 0) at btn

        textbutton _("✖") action Return() at btn

    # ----- settings
    if settings:
        drag:
            yalign .8
            frame:
                has vbox
                hbox:
                    textbutton _("✖") action SetScreenVariable("settings", 0) at btn align(.5,1.0)
                    textbutton _("▬") action ToggleScreenVariable("hovbar", 1, 0) at btn
                    textbutton _("⚏") action Function(g.toggle) at btn
                text "Number of thumbnails per page"
                hbox:
                    button:
                        text "<"
                        action Function(g.thumbsless)
                    text "{}".format(g.thumbs)
                    button:
                        text ">"
                        action Function(g.thumbsmore)
                
                
# -------------------------------- Simple Gallery
screen gallery_simple:
    # ----- the image
    if g.ret()[1]:
        vbox:
            text "⚷" size 200 color "#d00"
            text "Locked"
    else:
        add g.ret()[0].img align g.ret()[0].align
    frame:
        align(.5,0.0)
        text "{} - {}".format(g.ret()[0].name, g.ret()[0].info)

    # ----- the side buttons
    button:
        style "gal"
        xalign 0.0
        action Function(g.back)
    button:
        style "gal"
        xalign 1.0
        action Function(g.next)



# -------------------------------- Thumbnail Gallery
screen gallery_thumbnail:

    # ----- the thumbnails
    hbox:
        box_wrap True spacing 20 box_wrap_spacing 20
        for i in range(g.thumbs):
            if i+(int(g.current/g.thumbs)*g.thumbs) < len(g.lst):
                if g.retthumb(i+(int(g.current/g.thumbs)*g.thumbs))[1]:
                    button:
                        fixed:
                            fit_first True
                            if g.retthumb(i+(int(g.current/g.thumbs)*g.thumbs))[0].icon:
                                add g.retthumb(i+(int(g.current/g.thumbs)*g.thumbs))[0].icon
                            else:
                                frame:
                                    xysize g.iconsize
                                    text "No Thumbnail"
                            vbox:
                                text "⚷" size 200 color "#d00"
                                text "Locked"
                else:
                    button:
                        at btn
                        if g.retthumb(i+(int(g.current/g.thumbs)*g.thumbs))[0].icon:
                            add g.retthumb(i+(int(g.current/g.thumbs)*g.thumbs))[0].icon
                        else:
                            frame:
                                xysize g.iconsize
                                text "No Thumbnail"
                        action Function(g.set, i+(int(g.current/g.thumbs)*g.thumbs)), SelectedIf(i+(int(g.current/g.thumbs)*g.thumbs) == g.current)

    # ----- the side buttons
    button:
        style "gal"
        xalign 0.0
        action Function(g.pervPage)
    button:
        style "gal"
        xalign 1.0
        action Function(g.nextPage)

    # ----- the image
    if g.slc:
        button:
            align(.5,1.0) background "#000d" padding 0,0 xfill True yfill True
            add g.ret()[0].img align g.ret()[0].align
            action Function(g.unset)
        frame:
            align(.5,0.0)
            text "{} - {}".format(g.ret()[0].name, g.ret()[0].info)



style gal:
    idle_background None
    hover_background "#fff3"
    yfill True
    xsize 400
    