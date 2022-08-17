import numpy as np
import cv2 as cv

class Sketcher:
    def __init__(self, windowname, dests, colors_func):
        self.prev_pt = None
        self.windowname = windowname
        self.dests = dests
        self.colors_func = colors_func
        self.dirty = False
        self.show()
        cv.setMouseCallback(self.windowname, self.on_mouse)

    def show(self):
        cv.imshow(self.windowname, self.dests[0])
        cv.imshow(self.windowname+": Mask", self.dests[1])

    def on_mouse(self, event, x, y, flags, param):
        pt = (x, y)
        if event == cv.EVENT_LBUTTONDOWN:
            self.prev_pt = pt
        elif event == cv.EVENT_LBUTTONUP:
            self.prev_pt = None
        if self.prev_pt and flags & cv.EVENT_FLAG_LBUTTON:
            for dst, color in zip(self.dests, self.colors_func()):
                cv.line(dst, self.prev_pt, pt, color, 5)
            self.dirty = True
            self.prev_pt = pt
            self.show()


def main():
    print("Enter key 1 to choose Method 1: Damaged Inpaint")
    print("enter key 2 to choose Method 2: Own Inpaint")
    key = int(input("Enter key to choose the method: "))

    if key == 1:
        damagedInpaint()
    elif key == 2:
        OwnInpaint()
    cv.destroyAllWindows()


def OwnInpaint():
    print("Usage: Python Inpaint")
    print("Keys: ")
    print("t - inpaint using FMM")
    print("n - inpaint using NS technique")
    print("r - reset the inpaint mask")
    print("ESC - exit")

    #Read image in color mode
    img = cv.imread("MyPhoto3.jpg", cv.IMREAD_COLOR)

    if img is None:
        print('Failed to load image file: {}'.format([img]))
        return
    img_mask = img.copy()

    inpaintMask = np.zeros(img.shape[:2], np.uint8)

    sketch = Sketcher('image', [img_mask, inpaintMask], lambda:((255,255,255), 255))

    while True:
        ch = cv.waitKey(0)

        if ch == 27:
            break
        if ch == ord('t'):
            res = cv.inpaint(src=img_mask, inpaintMask=inpaintMask, inpaintRadius=3, flags=cv.INPAINT_TELEA)
            cv.imshow("Inpaint output using FMM", res)
        if ch == ord('n'):
            res = cv.inpaint(src=img_mask, inpaintMask=inpaintMask, inpaintRadius=3, flags=cv.INPAINT_NS)
            cv.imshow("Inpaint output using NS", res)
        if ch == ord('r'):
            img_mask[:] = img
            inpaintMask[:] = 0
            sketch.show()
    print("Completed")

def damagedInpaint():
    print("Method 1: Damaged Inpaint")
    img = cv.imread('Old_Photo3.jpg')
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Original image', img)
    cv.waitKey(0)
    print("Image size is: ", img.shape)

    _, th1 = cv.threshold(gray_img, 247, 255, cv.THRESH_TOZERO)
    kernel = np.ones((3, 3), np.uint8)
    mask = cv.dilate(th1, kernel, 1)
    cv.imshow('Mask', mask)

    cv.resize(img, (300, 300))
    cv.resize(mask, (300, 300))

    print("Press 't' to apply FMM Method for inpainting", end='\n')
    print("Press 'n' to apply NS Method for inpainting", end='\n')

    ch = cv.waitKey(0)
    if ch == ord('t'):
        print("FMM Method for inpainting")
        res = cv.inpaint(src=img, inpaintMask=mask, inpaintRadius=200, flags=cv.INPAINT_TELEA)
        cv.imshow("Output using FMM Method", res)
        cv.waitKey(0)

    elif ch == ord('n'):
        print("NS Method for inpainting")
        res = cv.inpaint(src=img, inpaintMask=mask, inpaintRadius=200, flags=cv.INPAINT_NS)
        cv.imshow("Output using NS Method", res)
        cv.waitKey(0)
    else:
        print("Non-Valid key entered! Run the code again")

    print('Completed Inpainting')
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()
    cv.destroyAllWindows()



