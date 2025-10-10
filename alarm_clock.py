import tkinter as tk
from time import strftime
from datetime import datetime
import winsound

main = tk.Tk()
main.title("Alarm Clock")
main.geometry("240x200")
main.config(bg="#101820")

# Display current time
def time_setting():
    label.config(text=strftime('%H:%M:%S'))
    label.after(1000, time_setting)

# Validate  entry format (HH:MM, 24-hour time)
def valid_time(t:str) -> bool:
    if not isinstance(t, str):
        return False
    try:
        # parse string into a time using strptime
        datetime.strptime(t, "%H:%M")
        return True
    except ValueError:
        return False

#Check alarm
def check_alarm():
    alarm_time = alarm_entry.get().strip()
    if not valid_time(alarm_time):
        main.after(1000, check_alarm)
        return

    current_time = datetime.now().strftime('%H:%M')

    # Check if current time matches alarm time
    if alarm_time == current_time:
        status.config(text="")
        # Beep 5 times
        for i in range(5):
            winsound.Beep(1000, 800)
        return

    # Check every second
    main.after(1000, check_alarm)

# Set alarm
def set_alarm():
    alarm_time = alarm_entry.get().strip()
    if not valid_time(alarm_time):
        status.config(
            text=f"Please enter time in HH:MM format",
            font=('TkDefaultFont', 10),fg="yellow"
        )
        return

    status.config(
        text=f"Alarm set for {alarm_time}",
        font=('TkDefaultFont', 11), fg="green"
    )
    check_alarm()

# Clock label
label = tk.Label(
    main, font=('TkDefaultFont', 40, 'bold'), bg='#101820', fg='white'
)
label.pack(anchor='center')

# Alarm input
frame = tk.Frame(main, bg='#101820')
frame.pack()

tk.Label(
    frame, text="Set Alarm (HH:MM):",
    font=('TkDefaultFont', 11), bg="#101820", fg="white"
).pack()
alarm_entry = tk.Entry(
    frame, font=('TkDefaultFont', 14), justify="center", width=8
)
alarm_entry.pack(pady=5)

# Button to set alarm
tk.Button(
    main, text="Set Alarm", command=set_alarm, bg= "blue",
    font=('TkDefaultFont', 10, "bold")
).pack(pady=2)

status = tk.Label(
    main, text="", font=('TkDefaultFont', 12), bg="#101820", fg="white"
)
status.pack(pady=2)

time_setting()

main.mainloop()
