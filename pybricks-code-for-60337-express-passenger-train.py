from pybricks.pupdevices import ColorDistanceSensor, DCMotor # ColorSensor instead of ColorDistanceSensor if using Mindstorms sensor
from pybricks.parameters import Color, Port
from pybricks.tools import wait

motor = DCMotor(Port.A)
sensor = ColorDistanceSensor(Port.B) # ColorSensor instead of ColorDistanceSensor if using Mindstorms sensor

station_stop_time_ms = 2500
eol_stop_time_ms = 5000
forward_speed = 20
check_color_interval_ms = 20

def check_for_color(color):
    while sensor.color() != color:
        wait(check_color_interval_ms)

while True:
    print("looking for green")
    check_for_color(Color.GREEN)

    print("green detected, at station, stopping and continuing")
    motor.brake()
    wait(station_stop_time_ms)
    motor.dc(forward_speed)

    print("looking for yellow")
    check_for_color(Color.YELLOW)

    print("yellow detected, at end of line, stopping and going back to station")
    motor.brake()
    wait(eol_stop_time_ms)
    motor.dc(-forward_speed)

    print("looking for green")
    check_for_color(Color.GREEN)

    print("green detected, at station, stopping and continuing")
    motor.brake()
    wait(station_stop_time_ms)
    motor.dc(-forward_speed)

    print("looking for red")
    check_for_color(Color.RED)

    print("red detected, at end of line, stopping and going back to station")
    motor.brake()
    wait(eol_stop_time_ms)
    motor.dc(forward_speed)
