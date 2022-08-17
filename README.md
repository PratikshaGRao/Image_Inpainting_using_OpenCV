# Image_Inpainting_using_OpenCV

Image In-painting is a process of restorative conservation of images, where damaged, deteriorating, or missing parts of an artwork are reconstructed, ultimately with the goal of presenting the artwork as it was originally created.

It involves application of sophisticated algorithms to replace lost or corrupted parts of the image data using mainly pixel prediction.

![image](https://user-images.githubusercontent.com/88997340/185057974-3a16e685-4209-4274-8fb9-88088645979f.png)

OpenCV is a massive open-source library for various fields like computer vision, machine learning, image processing and plays a critical function in real-time operations, which are fundamental in today’s systems. It is deployed for the detection of objects, faces, diseases, number plates, and even handwriting in various images and videos. With help of OpenCV in Deep Learning, we are trying to regenerate damaged imgages for their restoration.

Let's see what all OpenCV Python provides to do this inpainting!!

### Fast Marching Method

This method is to solve the boundary value problems of the Eikonal equation:

F(x)|∇T(x)|=1

Where F(x) is a speed function in the normal direction at a point x on the boundary curve. T is the time at which the contour crosses a point x which is obtained by solving the equation. We have used cv2.inpaint() function with a parameter cv2.INPAINT_TELEA. The name "telea" is from the author (Alexandru Telea) from his paper, "An Image Inpainting Technique Based on the Fast Marching Method".

### Navier-Stokes Method

This method restores the selected region in an image using the region neighborhood. The function reconstructs the selected image area from the pixel near the area boundary.

I have presented my code on this with the help of a few sources, study and vidoes!! Go and try for yourself and play with these algorithms for Image Inpainting!!

