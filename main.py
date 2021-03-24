from kivymd.app import MDApp
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

test = '''
BoxLayout:
    orientation:'vertical'

    MDToolbar:
        title: "GIO's APP"
        md_bg_color: 0.784, 0.784, 0.784, 1
        specific_text_color: 1, 1, 1, 1

    MDBottomNavigation:
        panel_color: 0.784, 0.784, 0.784, 1

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Coupons'
            icon: 'sale'


            ScrollView:
                MDList:

                    TwoLineAvatarIconListItem:
                        on_release: print("Click!")

                        text: 'coupon1'
                        secondary_text: 'Expired in 30 days'
                        IconLeftWidget:
                            icon: "sale"

                    TwoLineAvatarIconListItem:
                        on_release: print("Click 2!")

                        text: 'coupon2'
                        secondary_text: 'Expired in 30 days'
                        IconLeftWidget:
                            icon: "sale"

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Camera'
            icon: 'camera'

            MDLabel:
                text: 'ngl this is camera'
                halign: "center"


        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Settings'
            icon: 'settings'




'''

class MainApp(MDApp):
    def build(self):
        x = Builder.load_string(test)
        return x

MainApp().run()
