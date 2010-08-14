from pyjamas.ui.Button import Button
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.HTML import HTML
from pyjamas.ui.Image import Image
# from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas import Window
import pyjslib
from __pyjamas__ import JS

def start(sender):
    Window.alert("Hello, GAMERS!")
    hw = HTML("<img src='http://github.com/jrabbit/Defenditt/raw/master/media/instructions%20screen.png' alt='instructions'/>", StyleName="instructions")
    RootPanel().add(hw)
    JS(""" 
    parent.top.document.getElementById("splash").style.display = "none"; 
    parent.top.document.getElementById("startbutton").style.display = "none";
    parent.top.document.getElementById("startbutton").style.height = 0;
    """)

def defenditt():
    #Characters
    snoo = Image("./public/media/alien.png")
    suit = Image("./public/media/suit.png")
    pass

if __name__ == '__main__':
    b = Button("Start Game", start)
    b.setID('startbutton')
    RootPanel().add(b)
    hw = HTML("<img src='http://github.com/jrabbit/Defenditt/raw/master/media/splash%20screen.png' alt='start screen'/>")
    hw.setID("splash")
    RootPanel().add(hw)