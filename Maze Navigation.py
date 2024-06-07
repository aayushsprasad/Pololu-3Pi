import machine
import utime
from pololu_3pi_2040_robot import robot

# Initialize robot components
rgb_leds = robot.RGBLEDs()
motors = robot.Motors()
buzzer = robot.Buzzer()
display = robot.Display()
encoders = robot.Encoders()

# Define the ADC pin
analog_pin = machine.ADC(27)


def forward():
    global motors, display, rgb_leds
    rgb_leds.set(0, [255, 0, 0])
    rgb_leds.show()
    motors.set_speeds(1000, 1000)  # Set motors speed
    display.fill(0)  # Clear display
    display.text("Moving forward", 0, 0)  # Display text
    display.show()  # Update display
    rgb_leds.off()
    initial_counts = encoders.get_counts()
    utime.sleep_ms(500)  # Wait for a short period
    
    if abs(encoders.get_counts()[0] - initial_counts[0]) < 10:
        # If encoder counts haven't changed much, robot likely halted
        # Move back a little
        motors.set_speeds(-800, -800)  # Move back with reduced speed
        utime.sleep_ms(500)  # Move back for 500 milliseconds
        motors.set_speeds(0, 0)  # Stop motors
    
    utime.sleep_ms(500)

def left():
    global motors, display, rgb_leds, encoders
    encoders.get_counts(reset=True)  # Reset encoder counts
    while True:
        c = encoders.get_counts()[0]  # Get current encoder counts
        if abs(c) >= 60:  # Check if encoder count reaches approximately 90
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
    forward()

def main():
    while True:
        # Read analog value from ADC
        adc_value = analog_pin.read_u16()

        # Print ADC value and calculated distance
        print("ADC Value:", adc_value)

        # Perform action based on distance
        if adc_value > 30000:
            left()
        else:
            forward()

        # Wait for a short period before taking the next reading
        utime.sleep(0.1)

main()
