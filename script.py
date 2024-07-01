# Just playing around with some commands
import pyautogui


def move_to_and_click(image, duration=1):
    x, y = pyautogui.locateCenterOnScreen(image, confidence=0.95)  # type: ignore
    pyautogui.moveTo(x / 2, y / 2, duration)
    pyautogui.click()


def main():
    pyautogui.moveTo(300, 300)
    move_to_and_click("keys/calc7key.png")
    move_to_and_click("keys/calcMultkey.png")
    move_to_and_click("keys/calc7key.png")
    move_to_and_click("keys/calcEqualkey.png")


if __name__ == "__main__":
    main()
