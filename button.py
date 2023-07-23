import cv2


class Button:
    def __init__(self,pos,width,height,value):
        self.pos=pos
        self.width=width
        self.height=height
        self.value=value

    def draw(self, img ):
        cv2.rectangle(img,self.pos,(self.pos[0]+self.width,self.pos[1]+self.height),(0,0,0),2)
        # cv2.rectangle(img,self.pos,(self.pos[0]+self.width,self.pos[1]+self.height),(250,50,50),3)
        halfWidth=self.width/2
        halfHeight=self.height/2
        cv2.putText(img,self.value,(int(self.pos[0]+halfWidth-10),int(self.pos[1]+halfHeight+10)),cv2.FONT_HERSHEY_PLAIN,2,(0,0,0),2)

    def getValue(self,x,y,angle):
        if self.pos[0] <x<self.pos[0]+self.width and \
            self.pos[1] <y<self.pos[1]+self.height:
                print('value:',self.value)
                return self.value
        else:
            return 'x'