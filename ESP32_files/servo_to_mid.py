def swipe_and_center():
    """ Function that spins the cube holder to both end positions before stopping to the middle one.
        This is meant to:
        1) check the rotation range of the servo before assembling the robot.
        2) set the servos to their mid position, so to properly connect the arms."""
        
    from machine import Pin, PWM
    from utime import sleep_ms

    t_servo= PWM(Pin(15))
    t_servo.freq(50) # top servo, connected to Pin 15
    sleep_ms(50)

    b_servo= PWM(Pin(16))
    b_servo.freq(50)   # bottom servo, connected to Pin 23
    sleep_ms(50)
    
    MID = 1845000
    MIN = 420000
    MAX = 3270000
    
    MID_2 = 1500000
    MIN_2 = 455000
    MAX_2 = 3240000
    
    max_1000to2000us = MAX_2 # 106          # Servo duty value for angle -100deg, beyond limit of a 1 to 2ms servo
    max_500to2500us = MAX_2 # 134           # Servo duty value for angle -100deg, beyond limit of a 0.5 to 2.5ms servo
    min_1000to2000us = MIN_2 # 48           # Servo duty value for angle 100deg, beyond limit of a 1 to 2ms servo
    min_500to2500us = MIN_2 # 20            # Servo duty value for angle 100deg, beyond limit of a 0.5 to 2.5ms servo
    mid_pos = 1500000 # 76                    # Servo duty value for angle 0deg, for 1to2ms and 0.5to2.5ms servo
    
    b_servo.duty_ns(mid_pos)           # servo is set to mid position
    t_servo.duty_ns(mid_pos)           # servo is set to mid position
    print(f"\nservos set to their middle position")
    sleep_ms(1200)                  # time for the servos to reach the mid position
    
    # because of different resolution of servos and accepted value:
    # a 1to2ms servo will sdef swipe_and_center():
    """ Function that spins the cube holder to both end positions before stopping to the middle one.
        This is meant to:
        1) check the rotation range of the servo before assembling the robot.
        2) set the servos to their mid position, so to properly connect the arms."""
        
    from machine import Pin, PWM
    from utime import sleep_ms

    t_servo= PWM(Pin(15))
    t_servo.freq(50) # top servo, connected to Pin 15
    sleep_ms(50)

    b_servo= PWM(Pin(23))
    b_servo.freq(50)   # bottom servo, connected to Pin 23
    sleep_ms(50)
    
    MID = 1845000
    MIN = 420000
    MAX = 3270000
    
    MID_2 = 1500000
    MIN_2 = 455000
    MAX_2 = 3240000
    
    max_1000to2000us = MAX_2 # 106          # Servo duty value for angle -100deg, beyond limit of a 1 to 2ms servo
    max_500to2500us = MAX_2 # 134           # Servo duty value for angle -100deg, beyond limit of a 0.5 to 2.5ms servo
    min_1000to2000us = MIN_2 # 48           # Servo duty value for angle 100deg, beyond limit of a 1 to 2ms servo
    min_500to2500us = MIN_2 # 20            # Servo duty value for angle 100deg, beyond limit of a 0.5 to 2.5ms servo
    mid_pos = 1500000 # 76 top rotating earlier, and each step will take larger rotation
    # while a 500to2500us servo will rotate for longer time, and each step will take smaller rotation
    
    print(f"\nservos rotating in steps toward one rotation extreme (CCW, from servo point of view)")
    for i in range(mid_pos, min_500to2500us, -20000):        # swipe from mid to min position
        print("LOOP 1") 
        b_servo.duty_ns(i)
        t_servo.duty_ns(i)
        sleep_ms(80)
    sleep_ms(1000)
    
    print(f"\nservos rotating in steps toward the other rotation extreme (CW, from servo point of view)")
    for i in range(min_500to2500us, max_500to2500us, 20000): # swipe from min to max position
        print("LOOP 2")
        b_servo.duty_ns(i)
        t_servo.duty_ns(i)
        sleep_ms(80)
    sleep_ms(1000)
    
    print(f"\nservos rotating in steps back to their middle position")
    for i in range(max_500to2500us, mid_pos, -20000):        # swipe from max to mid position
        print("LOOP 3")
        b_servo.duty_ns(i)
        t_servo.duty_ns(i)
        sleep_ms(80)
    
    print(f"\nservos are back to their middle position")
    
swipe_and_center()
