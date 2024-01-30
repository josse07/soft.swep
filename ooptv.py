class Tv():
    def __init__(self, brand, location) -> None:
        self.brand = brand
        self.location = location
        self.isOn = False
        self.isMuted = False
        self.channelList = [2,4,5,7,9,11,20,36,44,54,65]
        self.Nchannel = len(self.channelList)
        self.channelIndex = 0
        self.volume_minimum = 0
        self.volume_maximum = 10
        self.volume = self.volume_maximum
    
    def power(self):
        self.isOn = not self.isOn
    
    def volumeUp(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False
        if self.volume < self.volume_maximum:
            self.volume = self.volume + 1
    
    def volumeDown(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False
        if self.volume > self.volume_minimum:
            self.volume = self.volume - 1
    
    def channelUp(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex + 1
        if self.channelIndex > self.Nchannel:
            self.channelIndex = 0
    
    def channelDown(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex - 1
        if self.channelIndex < 0:
            self.channelIndex = self.Nchannel - 1
    
    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted
        
    def setchannel(self, NewChannel):
        if NewChannel in self.channelList:
            self.channelIndex = self.channelList.index(NewChannel)
    
    def showInfo(self):
        print()
        print('status of Tv:', self.brand)
        print(' location:', self.location)
        print('Tv status:')
        if self.isOn:
            print('Tv is: On')
            print('channel is: ', self.channelList[self.channelIndex])
            if self.isMuted:
                print('volume is:', self.volume,'(sound is muted)')
                
            else:
                print('volume is; ', self.volume)
                
        else:
            print('Tv is: Off' )

oTv = Tv('samsung', 'living room')
oTv1 = Tv('LG', 'Bed room')
#Turn both Tvs on
oTv.power()
oTv1.power()
#Raise the volume of oTv
oTv.volumeUp()
oTv.volumeUp()
#Raise the volume of oTv1
oTv1.volumeUp()
oTv1.volumeUp()
oTv1.volumeUp()
oTv1.volumeUp()
oTv1.volumeUp()
oTv1.volumeUp()
#change Tv1 channel, then mute it
oTv1.setchannel(20)
oTv1.mute()
#Now display both Tvs
oTv.showInfo()
oTv1.showInfo()

