import pyautogui




a = "Autoclicker"
b = "Credits"
c = "Exit"

print ("                                     //////////  CREATED BY TKODE  //////////")


choices = {a: 'Autoclicker', b: 'Credits', c: 'Exit'}

answer = pyautogui.confirm('Choose one.' , buttons=list(choices))

if answer == a:
	  
	  num = pyautogui.prompt("How many clicks you want to do?  ")

	  print ("You selected Autoclicker")
	  
	  pyautogui.alert(text=choices[answer], button='OK')
	  
	  for num in range (int(num)):
	  
	  	pyautogui.click(clicks=4,interval=0.0001)


	  	

	
		


		
	
	
 

if answer == b:
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("")
	print("                                 You can follow me on instagram @eyskode.exe")
	
	pyautogui.alert(text=choices[answer], button='OK')




if answer == c:
	
	print("Exit")








 



