class HitAreaWrapper():

    def __init__(self, hitArea):
        self.hitArea = hitArea
        self.bottom = hitArea.getBottom()
        self.left = hitArea.getLeft()
        self.right = hitArea.getRight()
        self.top = hitArea.getTop()
        
    def move(self, speedX, speedY):
        self.hitArea.move(speedX, speedY)