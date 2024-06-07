from pololu_3pi_2040_robot import robot
import time

directions_list = ['down', 'down', 'down', 'down', 'left', 'up', 'left', 'up', 'up', 'up', 'right', 'up', 'right', 'up', 'up', 'up']

rgb_leds = robot.RGBLEDs()
motors = robot.Motors()
buzzer = robot.Buzzer()
display = robot.Display()
encoders = robot.Encoders()
#max_speed = 1000
turn_time = 250

def forward():
    global motors
    global encoders
    encoders.get_counts(reset=True)  # Reset encoder counts
    while True:
        c = encoders.get_counts()[0]  # Get current encoder counts
        if c >= 700:  # Check if encoder count reaches approximately 360
            motors.set_speeds(0, 0)  # Stop motors
            break  # Exit the loop
        else:
            rgb_leds.set(0, [255, 0, 0])
            rgb_leds.show()
            motors.set_speeds(1000, 1000)  # Set motors speed
            buzzer.play("a32")  # Play buzzer
            display.fill(0)  # Clear display
            display.text("Moving forward", 0, 0)  # Display text
            display.show()  # Update display
            rgb_leds.off()
    time.sleep_ms(1000)

def down():
    global motors
    global encoders
    encoders.get_counts(reset=True)  # Reset encoder counts
    while True:
        c = encoders.get_counts()[0]  # Get current encoder counts
        if c >= 420:  # Check if encoder count reaches approximately 36
            motors.set_speeds(0, 0)  # Stop motors
            break  # Exit the loop
        else:
            rgb_leds.set(1, [192, 64, 0])
            rgb_leds.show()
            motors.set_speeds(1000, -1000)  # Set motors speed
            buzzer.play("a32")  # Play buzzer
            display.fill(0)  # Clear display
            display.text("Turning Backward", 0, 0)  # Display text
            display.show()  # Update display
            rgb_leds.off()
    time.sleep_ms(1000)
    forward()

def right():
    global motors
    global encoders
    encoders.get_counts(reset=True)  # Reset encoder counts
    while True:
        c = encoders.get_counts()[0]  # Get the first element (encoder count) from the list
        if c >= 180:  # Check if encoder count reaches approximately 90
            motors.set_speeds(0, 0)  # Stop motors
            break  # Exit the loop
        else:
            rgb_leds.set(2, [128, 128, 0])
            rgb_leds.show()
            motors.set_speeds(1000, -1000)  # Set motors speed
            buzzer.play("a32")  # Play buzzer
            display.fill(0)  # Clear display
            display.text("Turning Right", 0, 0)  # Display text
            display.show()  # Update display
            rgb_leds.off()
    time.sleep_ms(1000)
    forward()


def left():
    global motors
    global encoders
    encoders.get_counts(reset=True)  # Reset encoder counts
    while True:
        c = encoders.get_counts()[0]  # Get current encoder counts
        if abs(c) >= 240:  # Check if encoder count reaches approximately 90
            motors.set_speeds(0, 0)  # Stop motors
            break  # Exit the loop
        else:
            rgb_leds.set(3, [0, 255, 0])
            rgb_leds.show()
            motors.set_speeds(-1000, 1000)  # Set motors speed
            buzzer.play("a32")  # Play buzzer
            display.fill(0)  # Clear display
            display.text("Turning Left", 0, 0)  # Display text
            display.show()  # Update display
            rgb_leds.off()
    time.sleep_ms(1000)
    forward()
def spin():
    display.fill(1)
    display.text("Spinning", 30, 20, 0)
    display.text("WATCH OUT", 27, 30, 0)
    display.show()

    buzzer.play("L16 o4 cfa>cra>c4r4")

    circus =\
        "! O6 L8 T180" +\
        "MS aa- L16 ML ga-gg- L8 MS fe ML e- MS e fe L16 ML e-ee-d L8 MS d-c ML <b MS c" +\
        "MS e L16 <b<b L8 ML <b-<b" +\
        "MS e L16 <b<b L8 ML <b-<b" +\
        "L16 <a-<a<b-<bcd-de- L8 MS fe ML e- MS e"
    
    pirates_theme = \
        "O5 L4 T120 " +\
        "E F G A B C D E " +\
        "B- A G A B- A G F " +\
        "E- F G A B C D E " +\
        "B- A G A B- A G F "  

    rgb_leds.set(0, [255, 0, 0])
    rgb_leds.set(1, [192, 64, 0])
    rgb_leds.set(2, [128, 128, 0])
    rgb_leds.set(3, [0, 255, 0])
    rgb_leds.set(4, [0, 0, 255])
    rgb_leds.set(5, [128, 0, 128])
    rgb_leds.show()

    buzzer.play_in_background(circus)

    max = motors.MAX_SPEED
    step = max // 100

    for i in range(0, max, step):
        motors.set_speeds(i, -i)
        time.sleep_ms(10)

    time.sleep_ms(500)

    for i in range(max, 0, -step):
        motors.set_speeds(i, -i)
        time.sleep_ms(15)
    buzzer.off()    
    buzzer.play_in_background(pirates_theme)
    
    for i in range(0, -max, -step):
        motors.set_speeds(i, -i)
        time.sleep_ms(15)

    time.sleep_ms(500)

    for i in range(-max, 0, step):
        motors.set_speeds(i, -i)
        time.sleep_ms(10)
    buzzer.play("a32")  # Play buzzer
    display.fill(0)  # Clear display
    display.text("Good Bye", 0, 0)  # Display text
    display.show()
    display.fill(0)
    display.show()
    motors.off()
    rgb_leds.off()
    buzzer.off()
 
def follow_directions(directions_list):
    global motors
    global encoders
    
    for i in range(len(directions_list)):
        current_direction = directions_list[i]
        if i == 0:  # Check if it's the first element
            if current_direction == 'right':
                # Call the function for moving right
                right()
            elif current_direction == 'left':
                # Call the function for moving left
                left()
            elif current_direction == 'down':
                # Call the function for moving down
                down()
            elif current_direction == 'up':
                forward()
        
        elif i == len(directions_list) - 1:  # Check if it's the last element
                forward()
                spin()
        else:
            previous_direction = directions_list[i - 1]
            
            if current_direction == previous_direction:
                forward()
            elif current_direction != previous_direction:
                motors.set_speeds(0, 0)  # Stop the motors first
                if current_direction == 'right':
                    right()  # Follow the current direction to the right
                elif current_direction == 'left':
                    left()  # Follow the current direction to the left
                elif current_direction == 'down':
                    down()  # Follow the current direction down
                elif current_direction == 'up':
                    forward()  # Follow the current direction forward
            else:
                motors.set_speeds(0, 0)
        time.sleep_ms(1000)

follow_directions(directions_list)  # Call the function with the provided directions list