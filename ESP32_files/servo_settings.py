from machine import Pin, PWM
from utime import sleep_ms

class arm_servo:
    servo = PWM(Pin(15))
    # arm servo, connected to Pin 15
    bot = int
    mid = int
    top = int
    
    def move_bot(self):
        self.servo.duty_ns(self.bot)
        sleep_ms(50)
        print("bottom")
        
    def move_mid(self):
        self.servo.duty_ns(self.mid)
        sleep_ms(50)
        print("middle")
        
    def move_top(self):
        self.servo.duty_ns(self.top)
        sleep_ms(50)
        print("top")
        
    def __init__(self, a, b, c):
        self.servo.freq(50) 
        sleep_ms(50)
        self.bot = a
        self.mid = b
        self.top = c
        

def servo_settings(): 
    
    MID = 1845000
    MAX = 420000
    MIN = 3270000
    
    MID_2 = 1500000
    MIN_2 = 455000
    MAX_2 = 3240000
    
    
    #initalize servos
    arm = arm_servo(1560000,1200000,750000)
    #TODO: table_servo = table_servo()
    
    arm.move_top()
    sleep_ms(1200)
    arm.move_mid()
    sleep_ms(1200)
    arm.move_bot()
    
    
    
servo_settings()