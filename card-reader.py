from gpiozero import Button, LED, Buzzer
from time import sleep
from mcpi.minecraft import Minecraft
from mcpi import block
import pygame
import subprocess

peg1 = Button(17)
peg2 = Button(27)
peg3 = Button(22)
buzzer = Buzzer(23)
led = LED(24)

mc = Minecraft.create()

def test():
	mc.postToChat("Insert a card")
	sleep(5)

def flowers():
	pos = mc.player.getTilePos()
	mc.setBlock(pos.x, pos.y +3, pos.z, block.FLOWER_YELLOW)

def lightshow():
	led.blink(n=3)
	buzzer.beep(n=3)
	mc.postToChat("Lots of blinking lights, lets now open a browser window!")
	subprocess.call(["epiphany","http://linuxvoice.com"])
	sleep(5)


def audio(file):
    pygame.mixer.init()
    sound = pygame.mixer.music.load(file)
    pygame.mixer.music.play(1)
    mc.postToChat("You're now listening to "+(file))
try:
	while True:
		if peg1.is_pressed:
			flowers()
		elif peg2.is_pressed:
			lightshow()
		elif peg3.is_pressed:
			audio("LV.wav")
		else:
			test()
except KeyboardInterrupt:
	print("EXIT - Bye bye")
