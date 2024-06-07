import machine
import utime
from pololu_3pi_2040_robot import robot

# Initialize robot components
rgb_leds = robot.RGBLEDs()
motors = robot.Motors()
#buzzer = robot.Buzzer()
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
    utime.sleep_ms(1000)

def left():
    global motors, display, rgb_leds
    rgb_leds.set(3, [0, 255, 0])
    rgb_leds.show()
    motors.set_speeds(-500, 500)  # Set motors speed
    display.fill(0)  # Clear display
    display.text("Turning Left", 0, 0)  # Display text
    display.show()  # Update display
    rgb_leds.off()
    utime.sleep_ms(1000)
    forward()

def main():
    while True:
        # Read analog value from ADC
        adc_value = analog_pin.read_u16()

        # Print ADC value
        #print("ADC Value:", adc_value)

        # Perform action based on ADC value
        if adc_value > 40000:
            left()
        else:
            forward()

        # Wait for a short period before taking the next reading
        utime.sleep(0.2)

if __name__ == "__main__":
    main()
