from pyjamas.Canvas2D import Canvas, CanvasImage, ImageLoadListener
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.HTML import HTML
from pyjamas.ui.Image import Image


class OurCanvas(Canvas):
    def __init__(self):
        Canvas.__init__(self, 300, 250)
        self.img = CanvasImage('media/splash%20screen.png', self)
        self.addMouseListener(self)
    
    def onMouseDown(self, sender, x, y):
        if instuctions is not 1:
             self.img = CanvasImage('media/instructions%20screen.png', self)
             instructions = 1
        else:
            pass

    def onMouseEnter(self, sender):
        #RootPanel().add(HTML("mouseenter: setting focus (keyboard input accepted)"))      
        self.setFocus(True)

    def onMouseLeave(self, sender):
        #RootPanel().add(HTML("mouseleave: clearing focus (keyboard input not accepted)"))      
        self.setFocus(False)

    def onMouseMove(self, sender, x, y):
        #RootPanel().add(HTML("move: x %d " % x + "y %d" % y))
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
