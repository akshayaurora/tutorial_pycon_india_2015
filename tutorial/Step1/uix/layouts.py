'''Custom layouts
'''

from kivy.factory import Factory
from kivy.lang import Builder

Builder.load_string('''
<VBoxLayout>
    orientation: 'vertical'
    padding: dp(10)
    spacing: dp(10)
''')

class VBoxLayout(Factory.BoxLayout):
    pass
