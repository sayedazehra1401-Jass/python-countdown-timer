import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02}:{secs:02}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("⏰ Time's up!")

if __name__ == "__main__":
    try:
        user_input = int(input("Enter time in seconds: "))
        countdown_timer(user_input)
    except ValueError:
        print("Please enter a valid number.")
