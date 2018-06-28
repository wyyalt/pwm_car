import time
import RPi.GPIO as GPIO
from flask import Flask,render_template
from flask import request
from flask import session
import threading
import redis
app = Flask(__name__)
app.secret_key = "fjdksafjowejlfdashjlewq"
r = redis.Redis(host='127.0.0.1',port=6379)

def init():

    GPIO.setmode(GPIO.BCM)
    
    IN1 = 17
    IN2 = 18
    IN3 = 22
    IN4 = 23
    
    GPIO.setup(IN1,GPIO.OUT)
    GPIO.setup(IN2,GPIO.OUT)
    GPIO.setup(IN3,GPIO.OUT)
    GPIO.setup(IN4,GPIO.OUT)

    PWM1 = GPIO.PWM(IN1,60)
    PWM2 = GPIO.PWM(IN2,60)
    PWM3 = GPIO.PWM(IN3,60)
    PWM4 = GPIO.PWM(IN4,60)
    
    #GPIO.setup(40,GPIO.IN)

    PWM1.start(0)
    PWM2.start(0)
    PWM3.start(0)
    PWM4.start(0)

    def run():
        while r.get('run') == '1':
            PWM1.ChangeDutyCycle(int(r.get('IN1')))
            PWM2.ChangeDutyCycle(int(r.get('IN2')))
            PWM3.ChangeDutyCycle(int(r.get('IN3')))
            PWM4.ChangeDutyCycle(int(r.get('IN4')))
       
        PWM1.stop()
        PWM2.stop()
        PWM3.stop()
        PWM4.stop()
        GPIO.cleanup()
        r.set('init','0')

    t =  threading.Thread(target=run)
    t.start()

    #PWM1.stop()
    #PWM2.stop()
    #PWM3.stop()
    #PWM4.stop()

    #GPIO.cleanup()

    #GPIO.output(IN1,LEVEL_IN1)
    #GPIO.output(IN2,LEVEL_IN2)
    #GPIO.output(IN3,LEVEL_IN3)
    #GPIO.output(IN4,LEVEL_IN4)


@app.route('/back/<speed>/')
def back(speed):

    r.set('IN1',0)
    r.set('IN2',speed)
    r.set('IN3',0)
    r.set('IN4',speed)
  
    return 'Back'


@app.route('/')
def index():
    r.set('IN1',0)
    r.set('IN2',0)
    r.set('IN3',0)
    r.set('IN4',0)
    r.set('run',1)
    if r.get('init') == '0':
        init()
        r.set('init','1')
    return render_template('index.html')


@app.route('/front/<speed>/')
def front(speed):
    r.set('IN1',speed)
    r.set('IN2',0)
    r.set('IN3',speed)
    r.set('IN4',0)
    
    return 'Front'


@app.route('/right/<speed>/')
def right(speed):
    r.set('IN1',0)
    r.set('IN2',speed)
    r.set('IN3',0)
    r.set('IN4',0)
    return 'Right'


@app.route('/left/<speed>/')
def left(speed):
    r.set('IN1',0)
    r.set('IN2',0)
    r.set('IN3',0)
    r.set('IN4',speed)
    return 'Right'

@app.route('/stop/')
def stop():
    GPIO.cleanup()
    return 'Stoped'

if __name__ == '__main__':
    app.run(host='10.0.0.116')

