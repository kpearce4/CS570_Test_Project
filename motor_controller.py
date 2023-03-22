    class MotorController:

        def __init__(self, list_of_motors:list[motor]):
            self.motors = list_of_motors

        def set_speed(self, speed):
            for motor in self.motors:
                motor.set_speed(speed)


        def speed_up(self):
            for motor in self.motors:
                motor.speed_up()

        def slow_down(self):
            for motor in self.motors:
                motor.slow_down()

        def add_Motor(self, motor:Motor):
            self.motors.append(motor)