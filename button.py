import subprocess
from gpiozero import Button, LED
from signal import pause

bCliq = Button(17)
bGoa = Button(22)
bBoris = Button(26)

#bCliq_kill = Button(17, hold_time=2)
#bGoa_kill = Button(22, hold_time=2)
#bBoris_kill = Button(26, hold_time=2)

#killbuttons = [bCliq_kill, bGoa_kill, bBoris_kill]

lCliq = LED(27)
lGoa = LED(20)
lBoris = LED(21)

leds = [lCliq, lGoa, lBoris]

def cliq():
    print("cliq pressed")
    killvlc()
    subprocess.Popen(["cvlc", "http://somafm.com/cliqhop130.pls"])
    lCliq.on()

def goa():
    print("goa pressed")
    killvlc()
    subprocess.Popen(["cvlc", "http://somafm.com/suburbsofgoa130.pls"])
    lGoa.on()

def boris():
    print("boris pressed")
    killvlc()
    #subprocess.Popen(["cvlc", "file:///home/alarm/boris/"]) # TODO will it accept directory?
    subprocess.Popen(["cvlc", "file:///home/alarm/massenet/fixtures/c.opus"])
    lBoris.on()

def killvlc():
    print("killing vlc")
    subprocess.run(["killall", "vlc"])
    ledsoff()

def ledsoff():
    print("leds off")
    for l in leds:
        l.off()


bCliq.when_pressed = cliq
bGoa.when_pressed = goa
bBoris.when_pressed = boris

#for k in killbuttons:
#    k.when_held = killvlc

pause()
