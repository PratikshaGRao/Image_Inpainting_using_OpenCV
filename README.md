# Image_Inpainting_using_OpenCV

Image In-painting is a process of restorative conservation of images, where damaged, deteriorating, or missing parts of an artwork are reconstructed, ultimately with the goal of presenting the artwork as it was originally created.

It involves application of sophisticated algorithms to replace lost or corrupted parts of the image data using mainly pixel prediction.

![image](https://user-images.githubusercontent.com/88997340/185057974-3a16e685-4209-4274-8fb9-88088645979f.png)

OpenCV Python provides two methods to do this process of inpainting.

# Fast Marching Method

This method is to solve the boundary value problems of the Eikonal equation:

F(x)|∇T(x)|=1

Where F(x) is a speed function in the normal direction at a point x on the boundary curve. T is the time at which the contour crosses a point x which is obtained by solving the equation. We have used cv2.inpaint() function with a parameter cv2.INPAINT_TELEA. The name "telea" is from the author (Alexandru Telea) from his paper, "An Image Inpainting Technique Based on the Fast Marching Method".


