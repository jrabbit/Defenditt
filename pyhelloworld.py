from pyjamas.ui.Button import Button
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.HTML import HTML
from pyjamas.ui.Image import Image
# from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.KeyboardListener import KeyboardHandler
#from pyjamas.ui.ClickListener import ClickHandler
from pyjamas.Timer import Timer
from pyjamas import Window
from pyjamas.Canvas2D import Canvas, CanvasImage, ImageLoadListener

import pyjslib
from __pyjamas__ import JS
import random

def start(sender):
    Window.alert("Hello, GAMERS!")
    hw = HTML("<img src='http://github.com/jrabbit/Defenditt/raw/master/public/media/instructions%20screen.png' alt='instructions'/>")
    hw.setID('instructions')
    RootPanel().add(hw)
    JS(""" 
    parent.top.document.getElementById("splash").style.display = "none"; 
    parent.top.document.getElementById("startbutton").style.display = "none";
    parent.top.document.getElementById("startbutton").style.height = 0;
    """)

def defenditt():
    #Characters
    snoo = Image("./public/media/reddit alien.png")
    suit = Image("./public/media/suit.png")
    bullet = Image("./public/media/bullet.png")
    suit()
    pass

def suit():
    """spawn a zombie marketer at a random Y at the far right"""
    # 300, random.randrange(0,250)


class OurCanvas(Canvas):
    def __init__(self):
        Canvas.__init__(self, 300, 250)
        self.img = CanvasImage('media/splash screen.png', self)
        self.draw()
    


if __name__ == '__main__':
    #Canvas.__init__(0,0)
    b = Button("Start Game", start)
    b.setID('startbutton')
    RootPanel().add(b)
    hw = HTML("<img src='http://github.com/jrabbit/Defenditt/raw/master/public/media/splash%20screen.png' alt='start screen'/>")
    hw.setID("splash")
    RootPanel().add(hw)