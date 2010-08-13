from pyjamas.ui.Button import Button
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.HTML import HTML
from pyjamas import Window

def start(sender):
    Window.alert("Hello, GAMERS!")
    hw = HTML("<img src='http://github.com/jrabbit/Defenditt/raw/master/media/instructions%20screen.png' alt='instructions'/>")
    RootPanel().add(hw)
if __name__ == '__main__':
    b = Button("Start Game", start)
    RootPanel().add(b)
    hw = HTML("<img src='http://github.com/jrabbit/Defenditt/raw/master/media/splash%20screen.png' alt='start screen'/>")
    RootPanel().add(hw)