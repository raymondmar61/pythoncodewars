#https://www.codewars.com/kata/53f0f358b9cb376eca001079
'''
Regular Ball Super Ball 8 kyu

Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.

If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

ball1 = Ball()
ball2 = Ball("super")
ball1.ball_type  #=> "regular"
ball2.ball_type  #=> "super"
'''
class Ball(object):
    def __init__(self, ball_type="regular"): #default ball_type is regular
        self.ball_type = ball_type


ball1 = Ball()
ball1.ball_type
ball2 = Ball("super")
ball2.ball_type
ball1printfunction = Ball()
print(ball1printfunction.ball_type) #print regular
ball2printfunction = Ball("super")
print(ball2printfunction.ball_type) #print super

class Ball:
    def __init__(self, balltype):
        self.balltype = balltype
        if self.balltype == "":
            self.balltype = "regular"
        else:
            self.balltype


ball1 = Ball("")
print(ball1) #print <__main__.Ball object at 0x770917563fd0>
print(ball1.balltype) #print regular
ball2 = Ball("super")
print(ball2) #print <__main__.Ball object at 0x770917563eb0>
print(ball2.balltype) #print super

#Google AI Solution
class BallGoogleAI:
    def __init__(self, balltype="reguar"):
        self.balltype = balltype


ballGoogleAI1 = BallGoogleAI()
print(ballGoogleAI1) #print <__main__.BallGoogleAI object at 0x7b17f7167d30>
print(ballGoogleAI1.balltype) #print regular
ballGoogleAI2 = BallGoogleAI("super")
print(ballGoogleAI2) #print <__main__.BallGoogleAI object at 0x7b17f7167cd0>
print(ballGoogleAI2.balltype) #print super
