from final_project_code.action import Action


class CharacterDataWrapper():

    def __init__(self, cd):
        self.action = cd.getAction()
        self.attack = cd.getAttack()
        self.bottom = cd.getBottom()
        self.centerX = cd.getCenterX()
        self.centerY = cd.getCenterY()
        self.energy = cd.getEnergy()
        self.graphicAdjustX = cd.getGraphicAdjustX()
        self.graphicSizeX = cd.getGraphicSizeX()
        self.graphicSizeY = cd.getGraphicSizeY()
        self.hitCount = cd.getHitCount()
        self.hp = cd.getHp()
        self.lastHitFrame = cd.getLastHitFrame()
        self.left = cd.getLeft()
        self.remainingFrame = cd.getRemainingFrame()
        self.right = cd.getRight()
        self.speedX = cd.getSpeedX()
        self.speedY = cd.getSpeedY()
        self.state = cd.getState()
        self.top = cd.getTop()
        self.control = cd.isControl()
        self.front = cd.isFront()
        self.hitConfirm = cd.isHitConfirm()
        self.playerNumber = cd.isPlayerNumber()


    def onGround(self):
        return self.centerY == 537

    def inAir(self):
        return self.centerY > 537
    
    def isCrouching(self):
        return self.centerY < 537