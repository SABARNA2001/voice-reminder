import time
from plyer import notification
import pyttsx3

# Initialize the text-to-speech engine
text_speech = pyttsx3.init()

# Set the voice property to a specific voice
voices = text_speech.getProperty('voices')
text_speech.setProperty('voice', voices[0].id)  # Set the voice to the second voice in the list

text_speech.say("Enter your title here , please !")
text_speech.runAndWait()

title_enter = input("Enter your title here: ")

text_speech.say("Enter your message here , please !")
text_speech.runAndWait()

message_enter = input("Enter your message here: ")

text_speech.say("AFTER, HOW LONG DO YOU WANT TO ACTIVATE , YOUR REMINDER")
text_speech.runAndWait()
time_sleep = int(input("AFTER HOW LONG DO YOU WANT TO ACTIVATE YOUR REMINDER =>>>"))

text_speech.say(f"Reminder set up , this reminder for  , {title_enter} ,start remind you , again for, {time_sleep} second.")
text_speech.runAndWait()

if __name__ == "__main__":
    while True:
        # Provide the correct path to the icon file
        icon_path = "E:/projects/riminder/iconic.ico"

        notification.notify(
            title=title_enter,
            message=message_enter,
            app_icon=icon_path,
            timeout=20
        )
        time.sleep(time_sleep)
