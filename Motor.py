    class Motor:
        def __init__(self):
            self.speed=0.5

        def set_speed(self,speed):
            speed=max(-1, speed) #says that if speed is 7 it makes it the highest number (max) which is 7
            speed=min(1, speed) #says that if speed is 7 it makes it the lowest number (min) which is 1
            speed=speed^3 #making a dead zone (you want the speed to maintain the same at the start then increase)
            self.speed = speed

        def speed_up(self):
            self.speed = 2*self.speed

        def slow_down(self):
            self.speed = 0.5 * self.speed