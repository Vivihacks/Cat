import time
import sys

# Define the text to be typed out
text = "Привет, Соня. Я знаю, что может показаться, что я занят, но я всегда думаю о тебе, даже в напряженные моменты. Я люблю тебя, Соня! Всегда и навсегда, до конца времен. Не забывай мяукать!"

# Cat ASCII Art
cat_art = """
 /\_/\  
( o.o ) 
 > ^ <
Meow!
"""

# Function to simulate typing
def simulated_typing(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line after the text is finished

# Run the simulated typing function
simulated_typing(text, delay=0.05)

# Pause before showing the cat
time.sleep(1)
print(cat_art)
