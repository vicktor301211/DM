from tkinter import*
#Область переменных
w =
h =
player_size =
x1, y1 =
player_1_color =
x_finish =
#Область функций
def key_handler():
    pass
#Область создания окна
window = Tk()
window.title("Игра 'Догони меня если ссможешь'")
canvas = Canvas(window, width=w, height=h, bg = 'white')
canvas.pack()
#Область создания объектов
player_1_id =
finish_id =
#Область вызова
window.bind('<KeyRelease>', key_handler())
window.mainloop()