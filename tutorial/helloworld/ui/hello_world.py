'''This is where our UI starts
'''
from kivy.app import App


class HelloUI(App):
    '''UI for our Hello World App
    '''

    def on_start(self):
        # manage adding stuff to your UI here.
        self.root.text = 'App Started'
        # What is self.root?

    def on_pause(self):
        # return true to pause
        # otherwise app will just be closed on pause
        # save your data here, app is not gaurenteed to return
        return True

    def on_resume(self):
        # manage resumption of state
        pass

    def on_stop(self):
        # our app is going to stop clean up.
        pass
