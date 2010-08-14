from pyjamas.Canvas2D import Canvas, CanvasImage, ImageLoadListener
from pyjamas.ui.RootPanel import RootPanel

class OurCanvas(Canvas):
    def __init__(self):
        Canvas.__init__(self, 300, 250)
        self.img = CanvasImage('media/splash%20screen.png', self)
    
    def onLoad(self, sender=None):
        if sender==self.img:
            self.draw()

    def onError(self):
        pass

    def draw(self):
        ptrn = self.context.createPattern(self.img.getElement(), 'repeat')
        self.context.fillStyle = ptrn
        self.context.fillRect(0,0,300,250)
    


class RotatedCanvas(Canvas):
    def __init__(self):
        Canvas.__init__(self, 150, 150)
        self.context.translate(75,75)
        self.draw()

    def draw(self):
        pi = 3.14159265358979323
        # Loop through rings (from inside to out)
        for i in range(1,6):
            self.context.save()
            self.context.fillStyle = 'rgb(%d,%d,255)'%((51*i), (255-51*i))

            # draw individual dots
            for j in range(0,i*6): 
                self.context.rotate(pi*2/(i*6))
                self.context.beginPath()
                self.context.arc(0,i*12.5,5,0,pi*2,True)
                self.context.fill()

            self.context.restore()

if __name__ == '__main__':
    c = OurCanvas()
    #h = HTML("<b>Space Game</b>", StyleName='teststyle')
    RootPanel().add(c)
