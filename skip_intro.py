import cv2
import numpy as np
import pyautogui
import pytesseract

pytesseract.pytesseract.tesseract=r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


while True:
    # make a screenshot
    img = pyautogui.screenshot()
    # convert these pixels to a proper numpy array to work with OpenCV
    frame = np.array(img)
    # convert colors from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cropped_frame = frame[560:650, 1170:, ]
    a=pytesseract.image_to_string(cropped_frame)
    # show the frame
    cv2.imshow("screenshot", cropped_frame)
    # if the user clicks q, it exits
    if a.strip()=='SKIP INTRO':
        pyautogui.click(1275,631)
        print('Found')
        break
    if cv2.waitKey(1) == ord("q"):
        break

# make sure everything is closed when exited
cv2.destroyAllWindows()