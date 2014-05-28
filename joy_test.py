#!/usr/bin/env python
 
import pygame
import time
#!/usr/bin/env python
 
import pygame
import time
import math
 
# init controller
pygame.init()
controller = pygame.joystick.Joystick(0)
controller.init()
print 'Xbox Controller Connected'

print '/*********************************/'
print '  Joystick Drive Program           '
print "Updated by MRO for XBox Pad        "
print '/*********************************/'
 
key = 0
y = 0
x = 0

while key != 'q':
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:
	     #Print out the Axis pressed and the Value turned out (usually between -1 and 1)
     	    print "Axis: ",event.axis," Value: ",event.value
            if event.axis == 1:
                y = event.value
		  # to make these less sensetive turn them to 0.5s (for bigger deadzone?)
                if math.fabs(y) < 0.2:
                    y = 0
            if event.axis == 0: #I had to check this value using the above event.axis!!!
                x = event.value
                if math.fabs(x) < 0.2:
                    x = 0
         
    # Display the correct output hopefully!
    command = ' '
    if y < 0:
        command = 'up'
    elif y > 0:
        command = 'down'
    elif x < 0:
        command = 'left'
    elif x > 0:
        command = 'right'
    
    if command != ' ':     
    	print command

