import os
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import tkinter as tk
import random
import time

#images = os.listdir('/home/v/ENGL114/board/')

#print(images)
#print(str(random.randint(1,6)))

# key for chutes & ladders
routes = {
	'4': 17,
	'8': 18,
	'12': 15,
	'34': 57,
	'39': 75,
	'16': 3,
	'25': 21,
	'28': 22,
	'32': 30,
	'50': 47,
	'55': 54,
	'59': 58,
	'64': 62,
	'71': 70,
	'84': 82,
	'88': 86,
	'91': 90,
	'93': 92,
	'96': 76
}

# initialization
counter = 0
fig, ax = plt.subplots(1,1)
fig.set_size_inches(10, 10, forward=True)
img = mpimg.imread('board/0.png')
plt.axis('off')
imgplot = ax.imshow(img)
plt.pause(1)

def update_board(ctr):
	global imgplot
	global fig
	img = mpimg.imread('board/' + str(ctr) + '.png')
	imgplot.set_data(img)
	fig.canvas.draw_idle()
	plt.pause(0.1)
	#time.sleep(1)

root = tk.Tk()
root.title('Snakes & Ladders')
label = tk.Label(root, fg='dark green')
label.pack()

def perform_turn():
	#initialize global variables
	global counter
	global imgplot
	global fig
	global label

	# roll die, update label
	die = random.randint(1,6)
	label.config(text=str(die))
	counter += die

	if counter >= 100:
		time.sleep(1)
		label.config(text='You win!')
		update_board(100)
	else:

		update_board(counter)
	
		# move counter if it lands on a snake or ladder
		for key in routes:
			if str(counter) == key:
				counter = routes[key]
				time.sleep(1)
				update_board(counter)

		if counter >= 100:
			label.config(text='You win!')


# button controls

button = tk.Button(root, text='Next Turn', width=25, command=lambda: perform_turn())
button.pack()
root.mainloop()
