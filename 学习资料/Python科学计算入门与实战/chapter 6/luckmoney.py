import random
class LuckyMoney:

    def __init__(self,T,N):
        self.T = T
        self.N = N

    def generate(self):
        T = self.T*100
        N = self.N
        RN = [random.randint(1,T) for i in range(N)]
        RNT = sum(RN)
        RN = [round(el/RNT*T) for el in RN]
        err = T-sum(RN)
        index = random.randint(0,N-1)
        RN[index] += err
        RN = [el/100 for el in RN]
        random.shuffle(RN)
        return RN
    
##import matplotlib.pyplot as plt
##
##lm = LuckyMoney(30,6)
##bags = lm.generate()
##bags = [part/30*100 for part in bags]
##i_max,i_min = bags.index(max(bags)),bags.index(min(bags))
##names = ["Li Lei","Han Meimei","Jim","Bob","Herry","Rose"]
##explode = [0]*6
##explode[i_max] = 0.1
##explode[i_min] = 0.1
##plt.pie(x=bags,labels=names,explode = explode, autopct='%1.1f%%')
##plt.axis('equal')
##plt.show()
