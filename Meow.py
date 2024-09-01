# -*- coding: utf-8 -*-
import time
import sys

# Define the text to be typed out
text = "Привет, Соня. Я знаю, что может показаться, что я занят, но я всегда думаю о тебе, даже в напряженные моменты. Я люблю тебя, Соня! Всегда и навсегда, до конца времен. Не забывай мяукать!"

# Function to simulate typing
def simulated_typing(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line after the text is finished

# Run the simulated typing function
simulated_typing(text, delay=0.05)

# Pause before starting the "мяу" loop
time.sleep(1)

# Infinite loop to print "мяу" (meow in Russian)
try:
    while True:
        print("мяу")
        time.sleep(0.5)  # Adjust the delay as needed
except KeyboardInterrupt:
    print("\nProgram terminated by user.")
