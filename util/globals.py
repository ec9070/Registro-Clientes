def setSize(width, height):
    global w
    global h
    w = width
    h = height

def getSize():
    size=(w,h)
    return size

def c_window(window, width, height):
    height = height-48
    x = int((w/2) - (width/2))
    y = int((h/2) - (height/2))
    return window.geometry(f"{width}x{height}+{x}+{y}")
    