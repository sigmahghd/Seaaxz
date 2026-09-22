from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
import webbrowser

LINK = "https://boosty.to/enjoythevr/posts/53849ce1-04dc-4319-a7b3-c35497fc8bef?share=post_link"


class RedirectApp(App):
    def build(self):
        Clock.schedule_once(self.open_link, 0.5)
        return Label(text="Открываем...")

    def open_link(self, dt):
        webbrowser.open(LINK)


if __name__ == "__main__":
    RedirectApp().run()
