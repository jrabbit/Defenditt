from pyjamas.Canvas2D import Canvas, CanvasImage, ImageLoadListener
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.HTML import HTML
from pyjamas.ui.Image import Image

Alien_ypos = 125
difficulty = 1

class defenddit(Canvas):
    def __init__(self):
        pass

def move_alien(y):
    """move the alien to the y coord: following the mouse"""
    pass

def bang():
    """fire a bullet at the alien's current y position"""
    pass

class OurCanvas(Canvas):
    def __init__(self):
        Canvas.__init__(self, 300, 250)
        self.img = CanvasImage('media/splash%20screen.png', self)
        self.screen = 1
        self.addMouseListener(self)
    
    def onMouseDown(self, sender, x, y):
        if self.screen == 1:
            self.img = CanvasImage('media/instructions%20screen.png', self)
            #RootPanel().add(HTML("mouse down instuctions"))
            #RootPanel().add(HTML(self.screen))
            
        if self.screen == 2:
            self.img = CanvasImage('media/bkg.png', self)
            self.alien = CanvasImage('media/reddit alien.png')
            self.loader = ImageLoadListener()
            self.loader.add(self.alien)
            self.context.drawImage(self.alien.getElement(), 0, Alien_ypos)
            self.context.globalCompositeOperation('source-atop')
            #self.screen = self.screen + 1
            #RootPanel().add(HTML("mouse down bkg"))
        self.screen = self.screen + 1
        
    

    def onMouseEnter(self, sender):
        #RootPanel().add(HTML("mouseenter: setting focus (keyboard input accepted)"))      
        self.setFocus(True)
    
    def onMouseLeave(self, sender):
        #RootPanel().add(HTML("mouseleave: clearing focus (keyboard input not accepted)"))      
        self.setFocus(False)
    
    def onMouseMove(self, sender, x, y):
        #RootPanel().add(HTML("move: x %d " % x + "y %d" % y))
        move_alien(y)
        pass
    
    def onMouseUp(self, sender, x, y):
        pass
    
    def onLoad(self, sender=None):
        if sender==self.img:
            self.draw()
    
    def onError(self):
        pass
    
    def draw(self):
        ptrn = self.context.createPattern(self.img.getElement(), 'repeat')
        self.context.fillStyle = ptrn
        self.context.fillRect(0,0,300,250)
    

if __name__ == '__main__':
    c = OurCanvas()
    RootPanel().add(c)
    c.getElement().focus()
