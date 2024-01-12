import customtkinter
import time

is_running = False
elapsed_time = 0

def update_time():
    global elapsed_time
    if is_running:
        elapsed_time += 1
        minutes, seconds = divmod(elapsed_time, 60)
        time_str = f'{minutes:02d}:{seconds:02d}'
        timer_label.configure(text=time_str)
        app.after(1000, update_time)

def start():
    global is_running
    if not is_running:
        is_running = True
        update_time()

def stop():
    global is_running
    is_running = False

def reset():
    global is_running, elapsed_time
    is_running = False
    elapsed_time = 0
    timer_label.configure(text='00:00')
    
def register():
    "Esta funcion imprime en pantalla el tiempo transcurrido hasta que se le da a stop"
    global is_running, elapsed_time
    is_running = False
    minutes, seconds = divmod(elapsed_time, 60)
    time_str = f'{minutes:02d}:{seconds:02d}'
    print(time_str)

app = customtkinter.CTk()
app.title('ReTask')

timer_label = customtkinter.CTkLabel(app, text='00:00', font=('Arial', 24))
timer_label.pack()

start_button = customtkinter.CTkButton(app, text='Start', command=lambda: start())
stop_button = customtkinter.CTkButton(app, text='Stop', command=lambda: stop())
reset_button = customtkinter.CTkButton(app, text='Reset', command=lambda: reset())

register_button = customtkinter.CTkButton(app, text='Registrar', command=lambda: register())

start_button.pack()
stop_button.pack()
reset_button.pack()
register_button.pack()

app.mainloop()