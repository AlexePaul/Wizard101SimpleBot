import PySimpleGUI as sg
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import datetime

def click() :
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def buy() :
	win32api.SetCursorPos(Empower)
	time.sleep(0.5)
	click()

	time.sleep(0.5)

	BuyMore = pyautogui.locateCenterOnScreen('Buying-Assets/BuyMore.png', confidence=0.9)
	win32api.SetCursorPos(BuyMore)
	time.sleep(0.5)
	click()

	time.sleep(0.5)

	More = pyautogui.locateCenterOnScreen('Buying-Assets/More.png', confidence=0.9)
	win32api.SetCursorPos(More)
	time.sleep(0.5)
	for x in range(100):
		time.sleep(0.03)
		click()

	time.sleep(0.5)

	BuyNow = pyautogui.locateCenterOnScreen('Buying-Assets/BuyNow.png', confidence=0.9)
	win32api.SetCursorPos(BuyNow)
	time.sleep(0.5)
	click()

	time.sleep(0.5)

	Okay = pyautogui.locateCenterOnScreen('Buying-Assets/Okay.png', confidence=0.9)
	win32api.SetCursorPos(Okay)
	time.sleep(0.5)
	click()

def goForward() :
	win32api.keybd_event(0x57, 0,0,0)
	time.sleep(0.5)
	win32api.keybd_event(0x57,0 ,win32con.KEYEVENTF_KEYUP ,0)

def goBackwards() :
	win32api.keybd_event(0x53, 0,0,0)
	time.sleep(0.5)
	win32api.keybd_event(0x53,0 ,win32con.KEYEVENTF_KEYUP ,0)

def clickFights(location) :
	win32api.SetCursorPos(location)
	time.sleep(0.5)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(.05)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	win32api.SetCursorPos((0,0))

sg.theme('Dark Blue 3')

#Window used for selecting whether the bot is gonna farm fights or snipe bazaar for Empowers
farmSelectionLayout = [	[sg.Text('What do you want the bot to farm?',font='helvetica 20')],
						[sg.Button('Empowers',font='helvetica 20'), sg.Button('Fights',font='helvetica 20')]
					]
farmSelection = sg.Window("Wizard101 Farm-Bot", farmSelectionLayout, size = (500, 100), element_justification='c')

while 1:
	event, values = farmSelection.read()
	if event == sg.WIN_CLOSED :
		break;
	if event == 'Empowers' :
		farmType = 'Empowers'
		break
	elif event == 'Fights' :
		farmType = 'Fights'		
		break
farmSelection.close()

ok = 0

if farmType == 'Empowers' :
	empowersSnipeLayout = [ [sg.Text('Make sure to have the bazaar open, as shown in the picture below',font='helvetica 20')],
							[sg.Image(r'./Buying-Assets/Example.png')],
							[sg.Button('Start',font='helvetica 20')],
							[sg.Text('To stop the bot, close this window or hold K while refreshing and a bit after', font='helvetica 18')]
						]
	empowersSnipe = sg.Window('wizard101 Bazaar-Snipe-Bot', empowersSnipeLayout, size = (850, 800), element_justification='c')
	event, values = empowersSnipe.read()
	
	while 1:
		if event == sg.WIN_CLOSED :
			break;
		if event == 'Start' :
			ok = 1
		
		if ok == 1 :
			empowersSnipe.Minimize()
			time.sleep(1)
			DeathSchool = pyautogui.locateCenterOnScreen('Buying-Assets/Death.png', confidence=0.9)
			print("Refreshing...")
			win32api.SetCursorPos(DeathSchool)
			time.sleep(0.5)
			click()
			if keyboard.is_pressed('k'):
				break
			time.sleep(2)
			if keyboard.is_pressed('k'):
				break

			NextPage = pyautogui.locateCenterOnScreen('Buying-Assets/Next.png', confidence=0.9)
			while NextPage != None:
			
				Empower = pyautogui.locateCenterOnScreen('Buying-Assets/Empower.png', confidence=0.9)
				if Empower != None:
					print("Buying Empower!")
					buy()
					break

				if Empower == None:
					NextPage = pyautogui.locateCenterOnScreen('Buying-Assets/Next.png', confidence=0.9)
					if NextPage == None:
						NextPage = pyautogui.locateCenterOnScreen('Buying-Assets/NextLit.png', confidence=0.9)
					if NextPage == None:
						break
					win32api.SetCursorPos(NextPage)
					click()

				Empower = pyautogui.locateCenterOnScreen('Buying-Assets/Empower.png', confidence=0.9)
				if Empower != None:
					print("Buying Empower!")
					buy()
					break
			event, values = empowersSnipe.read(timeout=100)

if farmType == 'Fights' :
	fightingLayout = [	[sg.Text('Make sure you have max mana before starting the bot!',font='helvetica 20')],
						[sg.Text('before the first time use, refer to the "read me" file',font='helvetica 20')],
						[sg.Text('To stop the bot, close this window or hold K when the \ncharacter switches from going forward to going backwards', font='helvetica 18')],
						[sg.Text('Mana:',font='helvetica 20'), sg.InputText(size=(73,0))],
						[sg.Text('Mana cost of the spell:',font='helvetica 20'), sg.InputText()],
						[sg.Submit('Start', font='helvetica 20')]
					]
	fighting = sg.Window('wizard101 Fight-Farming Bot', fightingLayout, size = (700, 350))
	event, values = fighting.read()
	maxSpellCount = int(int(values[0])/int(values[1]))
	counter=0

	while 1:
		
		if event == sg.WIN_CLOSED :
			break;
		if event == 'Start' :
			ok = 1
		
		if ok == 1:
			fighting.Minimize()
			goForward()
			if keyboard.is_pressed('k'):
				break
			goBackwards()

			spell = pyautogui.locateCenterOnScreen('Farming-Assets/Spell.png', confidence=0.9)
			passButton = pyautogui.locateCenterOnScreen('Farming-Assets/Pass.png', confidence=0.9)

			if spell != None :
				clickFights(spell)
				counter += 1
				print('Casted Spell!')
			elif passButton != None :
				clickFights(passButton)
				print('Passed...')
			if counter ==  maxSpellCount:
				potionBottle = pyautogui.locateCenterOnScreen('Farming-Assets/Bottle.png', confidence=0.9)
				while potionBottle == None:
					potionBottle = pyautogui.locateCenterOnScreen('Farming-Assets/Bottle.png', confidence=0.9)
				clickFights(potionBottle)
				print('Used a mana bottle...')
				counter = 0;
		event, values = fighting.read(timeout=100)
