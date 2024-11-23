from tkinter import*
#Область переменных
w = 800
h = 800
player_size = 100
x1, y1 = 50, 50
player_1_color = 'red'
x_finish = w-50
#Область функций
def key_handler(event):
    canvas.move(player_1_id, 10, 0)
#Область создания окна
window = Tk()
window.title("Игра 'Догони меня если ссможешь'")
canvas = Canvas(window, width=w, height=h, bg = 'white')
canvas.pack()
#Область создания объектов
player_1_id = canvas.create_rectangle(x1, y1, x1+player_size, y1+player_size, fill = player_1_color)
finish_id = canvas.create_rectangle(x_finish, 0, x_finish+10, h, fill = 'black')
#Область вызова
window.bind('<KeyRelease>', key_handler)
window.mainloop()