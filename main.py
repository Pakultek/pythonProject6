from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from pymysql import connect
from datetime import datetime

Window.size = (320, 500)
Window.clearcolor = ('#FAF0E6')
Window.title = "Конвертер"


class MyApp(App):
    def __init__(self):
        super().__init__()

        self.art = Label(text='1', size_hint=(1, 0.25), color=[0, 0, 0, 1])
        self.date = Label(text='2', halign='center', size_hint=(1, 0.25), color=[0, 0, 0, 1])
        self.status = Label(text='3', halign='center', size_hint=(1, 0.25), color=[0, 0, 0, 1])

        self.input_number = TextInput(hint_text='', multiline=False, size_hint=(1, 0.05))
        self.input_number.bind(text=self.on_text)

    def on_text(self, *args):
        data = self.input_number.text
        length = len(data)
        if length == 11:
            con = connect(host="10.10.3.41", user="vadim", password="1q2w3e4r5t6y", database="TUBOG")
            cur = con.cursor()
            cur.execute("SELECT * FROM Proizvodstvo INNER JOIN Radiatori_Zakazi ON Radiatori_Zakazi.N_pp = Proizvodstvo.id_poz_zakaza WHERE Proizvodstvo.IND_Num = %s", (data,))
            row = cur.fetchone()
            if row:
                self.art.text = str(row[22])
                self.date.text = str(row[46])

                TekDate = datetime.now()

                if row[46] < TekDate:
                    self.date.color = [1, 0, 0, 1]  # Set red color
                else:
                    row[46] = TekDate
                    self.date.color = [0, 0, 0, 1]  # Set black color

                if row[8] < 2:
                    self.status.text = "бла бла бла"
                    self.status.color = [1, 0, 0, 1]  # Set red color
                else:
                    self.status.text = "Принято"
                    self.status.color = [0, 0, 1, 1]  # Set blue color

    def build(self):
        box = BoxLayout(orientation='vertical')
        box.add_widget(self.input_number)
        box.add_widget(self.art)
        box.add_widget(self.date)
        box.add_widget(self.status)
        return box


if __name__ == "__main__":
    MyApp().run()




