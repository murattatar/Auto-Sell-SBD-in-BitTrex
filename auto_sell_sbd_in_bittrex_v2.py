''' #####################################################
''' # Auto Sell SBD in BitTrex v1
''' # by Murat Tatar
''' # January 2018
''' #####################################################

''' #####################################################
''' # --!-- WARNING! --!--
''' # YOU MUST, FIRST TRY WITH yesreal ==0
''' # WHILE SETUP OR CONFIGURATION
''' # YOU MAY LOSE SBD/STEEM
''' # !! ALL RESPONSIBILITIES YOUR OWN !!
''' ##################################################### '''


''' import needed moduls '''
from selenium import webdriver as web
from selenium.webdriver.common.keys import Keys
import win32api, win32con
from controls import *



''' #####################################################
''' # --!-- WARNING! --!--
''' # YOU MUST, FIRST TRY WITH yesreal ==0
''' # WHILE SETUP OR CONFIGURATION
''' # YOU MAY LOSE SBD/STEEM
''' # !! ALL RESPONSIBILITIES YOUR OWN !!
''' ##################################################### '''

yesreal = 0

''' ##################################################### ''' 


def e():
  exit()


'''  ## Auto Sell SBD @ BitTrex  ######################### ''' 


bitTrexUser = 'root@yahoo.com'
bitTrexPass = 'imnotroot123'



'''  # Call the chromedriver ''' 
driver = web.Chrome("chromedriver.exe")

'''  # set chromedriver window size and position ''' 
'''  # if you get an error about the click location, ''' 
'''  # you should set the pixel location ''' 
driver.set_window_size(1360, 768)
driver.set_window_position(0,0)



'''  # You have already logged in ''' 
logurl = 'https://bittrex.com/Account/Login'
driver.get(logurl)
driver.implicitly_wait(30)
time.sleep(1)



''' # bitTrex user is your login e-mail '''
userbox = driver.find_element_by_name('UserName')
userbox.send_keys(bitTrexUser)  
time.sleep(.2)
keybox = driver.find_element_by_name('Password')
keybox.send_keys(bitTrexPass)
time.sleep(.2)
butonSL = driver.find_element_by_xpath(".//button[@class='g-recaptcha btn btn-primary login']")
time.sleep(.2)
keybox.send_keys(Keys.RETURN)
time.sleep(2)


'''  # Wait for manuel loggin or recaptcha ''' 
time.sleep(48)


''' # Bring an address specific to SBD  '''
sbdurl = 'https://bittrex.com/Market/Index?MarketName=BTC-SBD'
driver.get(sbdurl)
driver.implicitly_wait(30)

''' # Wait for driver done  '''
time.sleep(7)




'''  # find element created via javasctipt that there is NOT in Ctrl + U ''' 
'''  ## like as <span data-bind="text: summary.lastUsd()">6.20</span> ''' 
js_code = '''
b = document.getElementsByTagName('span');
return b
'''

spns = driver.execute_script(js_code)


x=0
for element in spns:
	element_text = element.text
	if x==38: price_text= element_text
	x= x+1


''' # may be you want, calculate %10+ and sell after that '''
sbd_price = float(price_text)

print 'SBD price: ', sbd_price


''' # scroll down at page '''
Cliq(1346,427)
time.sleep(1)


''' # unit box '''
Cliq(950,245)
time.sleep(1)


''' # select all '''
PressHoldRelease('ctrl', 'a')
time.sleep(1)


''' # clear box '''
PressHoldRelease('del')
time.sleep(1)


''' # write amount '''
''' # you can adjust the units as you want amount. ''' 
''' # Or you can click on "Max button" using Clicq. '''
Write('1.25')
time.sleep(1)




''' # Price box '''
Cliq(800,285)
time.sleep(1)


''' # select bid '''
Cliq(877,344)
time.sleep(1)


''' # clik to Sell button '''
Cliq(988,423)
time.sleep(1) 


''' # First, Read Warning! '''
if yesreal == 1:
	''' # clik to Confirm '''
	Cliq(912,692)



e()