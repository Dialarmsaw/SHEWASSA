import time
from datetime import datetime
import keyboard


while True:
    input("This test is made to test your WPM. I will give you a paragraph. You will be timed. Once the test starts, please re-write the paragraph. NEVER PRESS ENTER UNTIL YOU ARE FINISHED. To continue, press ENTER.")

    paragraph = "'The quick brown fox jumps over the lazy dog' is a sentence that is often used as a typing exercise or to test typing speeds. It contains all 26 letters of the English alphabet and is a pangram, which means it uses each letter at least once. Typing speed is an important skill in today's digital age, where efficient communication is key. Whether you're writing an email, drafting a document, or chatting with friends, being able to type quickly and accurately can save you time and enhance your productivity. Improving your typing speed takes practice, and there are various online typing tutors and exercises available to help you enhance your skills. By regularly practicing and challenging yourself with different typing tests, you can gradually increase your typing speed and accuracy. Remember, it's not just about how fast you type but also how accurately you do it. So keep practicing, and soon you'll be typing like a pro!"
    errors = 0
    wpm = 0


    startTime = datetime.now()
    print("Here is the paragraph. When you are done, press ENTER: \n \n", paragraph)
    response = input("\n")


    for i in range(len(response)):
        try:
            if response[i] != paragraph[i]:
                errors += 1
        except:
            errors += 1

    endTime = datetime.now()

    wpm = (endTime - startTime)

    while keyboard.read_key()!="home":
        pass
    print("WPM:", wpm,"Errors:", errors)
    
    