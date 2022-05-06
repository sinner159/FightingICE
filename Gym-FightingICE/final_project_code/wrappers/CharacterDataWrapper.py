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
        # self.Action = cd.setAction(Action action)
        # self.Attack = cd.setAttack(AttackData attack)
        # self.Bottom = cd.setBottom(int bottom)
        # self.Control = cd.setControl(boolean control)
        # self.Energy = cd.setEnergy(int energy)
        # self.Front = cd.setFront(boolean front)
        # self.HitConfirm = cd.setHitConfirm(boolean hitConfirm)
        # self.HitCount = cd.setHitCount(int hitCount)
        # self.Hp = cd.setHp(int hp)
        # self.LastHitFrame = cd.setLastHitFrame(int lastHitFrame)
        # self.Left = cd.setLeft(int left)
        # self.RemainingFrame = cd.setRemainingFrame(int remainingFrame)
        # self.Right = cd.setRight(int right)
        # self.SpeedX = cd.setSpeedX(int speedX)
        # self.SpeedY = cd.setSpeedY(int speedY)
        # self.State = cd.setState(State state)
        # self.Top = cd.setTop(int top)
        # self.X = cd.setX(int x)
        # self.Y = cd.setY(int y)

    def onGround(self):
        return self.centerY == 537

    def inAir(self):
        return self.centerY > 537
    
    def isCrouching(self):
        return self.centerY < 537