import random
class Warrior:
    def __init__(self,ap,dph,ats,chc):
        self.ap = ap
        self.dph = dph
        self.ats = ats
        self.chc = chc
        self.world_time = 0
        self.rage = 0
        self.damage = 0
        self.mt_cd = [-60]
        self.wh_cd = [-100]
        self.ntimes = 0
        self.mtimes = 0
        self.wtimes = 0


    def normal_attack(self):
        c = 230
        f = 3.5
        ap = self.ap
        ats = self.ats
        chc = self.chc
        low,high = self.dph
        dw = random.randint(low,high)
        dap = ap/14*ats
        damage = dw + dap
        r = random.random()
        if r < chc:
            damage = 2.4*damage
            f = f*2
        rage = 15*damage/(4*c) + f*ats/2
        self.rage += rage
        if self.rage > 100:
            self.range = 100
        self.damage += damage
        self.ntimes += 1

    def mortal_attack(self):
        self.mt_cd.append(self.world_time)
        self.rage -= 30
        ap = self.ap
        chc = self.chc
        low,high = self.dph
        dw = random.randint(low,high)
        dap = ap/14*3.3
        damage = dw + dap + 160
        r = random.random()
        if r < chc:
            damage = 2.4*damage
        self.damage += damage
        self.mtimes += 1

    def whirlwind(self):
        self.wh_cd.append(self.world_time)
        self.rage -= 25
        ap = self.ap
        chc = self.chc
        low,high = self.dph
        dw = random.randint(low,high)
        dap = ap/14*3.3
        damage = dw + dap
        r = random.random()
        if r < chc:
            damage = 2.4*damage
        self.damage += damage
        self.wtimes += 1

    def attack(self,t):
        t = int(10*t)
        ats = self.ats*10
        self.rage += 10
        for i in range(t):
            self.world_time = i
            if i % ats == 0:
                self.normal_attack()
            mt_cd = i - self.mt_cd[-1]
            if self.rage >= 30 and mt_cd >= 60:
                self.mortal_attack()
            mt_cd = i - self.mt_cd[-1]
            wh_cd = i - self.wh_cd[-1]
            if self.rage >=25 and wh_cd >=100 and mt_cd < 45:
                self.whirlwind()


ap = 1400
dph = (229,344)
ats = 3.4
chc = 0.3
w = Warrior(ap,dph,ats,chc)
w.attack(10)
        
