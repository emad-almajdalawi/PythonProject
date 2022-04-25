import cv2
from detect import SignDetection
import pytest



def test_i_love_you():
    sign_detect = SignDetection()
    cap = sign_detect.cap
    cap = cv2.VideoCapture("images/Iloveyou_sign.jpg")
    sign_detect.hand_detection(cap)

    actual=sign_detect.letter

    expected="I Love You"
    assert actual==expected

def test_Hello():
    sign_detect = SignDetection()
    cap = sign_detect.cap
    cap = cv2.VideoCapture("images/hello_sign.jpg")
    sign_detect.hand_detection(cap)

    actual=sign_detect.letter

    expected="Hello"
    assert actual==expected

def test_yellow():
    sign_detect = SignDetection()
    cap = sign_detect.cap
    cap = cv2.VideoCapture("images/yellow_sign.jpg")
    sign_detect.hand_detection(cap)

    actual=sign_detect.letter

    expected="Yellow"
    assert actual==expected

def test_nice():
    sign_detect = SignDetection()
    cap = sign_detect.cap
    cap = cv2.VideoCapture("images/nice_sign.jpg")
    sign_detect.hand_detection(cap)

    actual=sign_detect.letter

    expected="Nice"
    assert actual==expected

def test_camera():
    sign_detect=SignDetection()
    actual=sign_detect.cap.isOpened()
    expected=True
    assert  actual==expected

def test_landmarks():
    sign_detect = SignDetection()
    cap = sign_detect.cap
    cap = cv2.VideoCapture("images/yellow_sign.jpg")
    sign_detect.hand_detection(cap)
    actual=sign_detect.lm_id
    expected=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    assert  actual==expected

def test_leave():
    sign_detect = SignDetection()
    cap = sign_detect.cap
    cap = cv2.VideoCapture("images/leave_sign.mp4")
    sign_detect.hand_detection(cap)
    while sign_detect.hand_detection(cap):
        result=True
    else:
        result=False
    actual=result
    expected=False
    assert actual==expected









