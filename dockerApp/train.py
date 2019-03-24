'''
This is will be the first machine learning model, that only use date, 
hours and minutes, people id as the training attributes. This will be 
our baseline model. 
'''

class SmartEnergerA():

    def __init__(self):
        return

    def train(self):
        return

    # date should have the format year-month-day.
    # pid should be one of the six people id strings.
    # sunsetTime should have the format hour:minute:sec
    def predict(self, date, pid):
        light_on_time = "04:00"
        light_off_time = "23:00"
        return light_on_time, light_off_time



'''
This is the second machine learning model, a more advanced one compared with 
SmartEnergerA. It makes the predictions based on on more attributes, which is 
the sunset time for that day in Pittsburgh.
'''
class SmartEnergerB():

    def __init__(self):
        return

    def train(self):
        return

    # date should have the format year-month-day.
    # pid should be one of the six people id strings.
    # sunsetTime should have the format hour:minute:sec
    def predict(self, date, pid, sunsetTime):
        light_on_time = "04:00"
        light_off_time = "23:00"
        return light_on_time, light_off_time

