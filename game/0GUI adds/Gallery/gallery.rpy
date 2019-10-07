# --------------------------------------------- Define your images here
# You need to define each image with a unique name.
# I prefix each instance with gall_ to avoid duplicate names, feel free to use your own system.
# The name and img are required, the rest are optional.

define gall_bg = gallpic(
    name = "Background",
    img = "demo/bg.jpg",
    icon = "gall/bg.jpg",
    info = "A simple background.",
    align = (0.5, 1.0)
    )
define gall_ayame = gallpic(
    "Ayame",
    "demo/Ayame Errkk.png",
    "gall/Ayame Errkk.jpg",
    "Ayume is the shy girl.",
    )
define gall_nana = gallpic(
    "Nana",
    "demo/Nana Confident.png",
    "gall/Nana Confident.jpg",
    "Nana is the wild girl.",
    )
define gall_icon = gallpic(
    "Background",
    "gui/window_icon.png",
    "gall/icon.png",
    "It's the games icon.",
    (.5,.5)
    )
define gall_abdul = gallpic(
    "Abdul",
    "gall/confused.png",
    "gall/confused - icon.png",
    "A guest appearance?.",
    )
define gall_test = gallpic(
    "I don't know",
    "gall/test.png",
    "gall/test icon.png",
    "eehh!.",
    (.5,.5)
    )
define gall_4 = gallpic(
    "Some render",
    "gall/4.png",
    )
define gall_nana_locked = gallpic(
    "Nana",
    "demo/Nana Confident.png",
    )
# --------------------------------------------- Define a gallery and add images/settings to it
# You need a persistent variable to keep track of images in your gallery.
default persistent.gallery_1_list = [
    ["gall_bg", 0],
    ["gall_ayame", 0],
    ["gall_nana", 1],
    ["gall_icon", 1],
    ["gall_abdul", 1],
    ["gall_test", 0],
    ["gall_4",0],
    ["gall_nana_locked", 0],
    ]

# Pass your image list to your gallery instance, (required)
# with the number of thumbnails per page, the gallery type ("simple", "thumbs", or your own design) and thumbnail size (all optional)
define gallery_1 = gallery_class(
    lst = persistent.gallery_1_list,
    thumbs = 6,
    type = "thumbs"
    )

