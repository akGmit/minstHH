<h1>Handwritten digit recognition using Neural Net</h1>

<h2>Intro</h2>

A web application which can recognize handwritten digits. Application contains a pre-trained CNN model which is used to make predictions. 
App prediction process:
  1. User draws digit using browser canvas.
  2. Image is stripped of RGB values(which is nil since image is black and white), leaving only alpha values.
  3. Using JS image is converted to 1d array of pixel values.
  4. Using AJAX async call, image array is sent to back-end app.
  5. Array is reshaped to 2D array.
  6. Image processed to MNIST data standart.
  7. Image arrays is fed to Keras CNN model for prediction.
  8. Prediction result is returned to web browser.
  
<h2>Application structure</h2>

<h3>Recognition</h3>
<b>Nnet module</b>

A module which contains CNN model implementation. Defined here are specific for this application functions dealing with reading MNIST data, building CNN model, training model, loading pre-trained model. This module acts as an interface for all functonality required by application.

<b>Cfunc module</b>

To increase performance of reading MNIST files and processing them to required format this application uses Python Ctypes library which enables calling of foreign C functions. Here are defined functions which called returns a Ctype function which delegates calls to C shared object.

<b>Mnist_fread</b>

Function implementations to read MNIST files to memmory. Contains two functions: reading MNIST image data and MNIST labels data. Data is read using functions defined in Cfunc and returned pointers from C foreing functions are further processed to match format required for training/testing model.

<b>C library</h>

This library provides implementations of C functions to read MNIST imgae, label data. Also it processes a raw bytes to more practical 2D arrays. From this library a shared object is compiled which can be used by Python scripts.


<h3>Web app</h3>

Using a Wsgiref web server, which supposed to be production ready unlike Flask.
Web app serves index page for the user, which contains canvas to draw digits in. After user makes async call to app, user drawn image is sent as an array, data is processed to fit format suitable for feeding to Keras model for prediction. The changes made are:
  1. From a 1D array we reshape it to 200x200 2D array.
  2. Boundries box of actual digit is found.
  3. Data representing image is extracted according to boundries.
  4. Image is resized to 28x28 and centerd, this way it guarantees maximum accuracy when predicting.
  5. Procesed image array is fed to CNN model and prediction result is served to front-end.


<h2>Final word</h2>

The development process was challenging and interesting, most importanly - rewarding. The most standing out feature of the application is Python calling C foreing functions. After testing python functions to read files against stdio C library functions of same purpose - C implementation provides a lot better performance. It took quite a bit of work to make Python and C to work together - the hardest being to make Ctype function returns work with Python data structures. 




References

Offical Keras website;

C stdio
http://www.cplusplus.com/reference/cstdio/fread/

Call c function from python
https://docs.python.org/3/library/ctypes.html
https://www.csestack.org/calling-c-functions-from-python/

C-types
https://docs.python.org/3/library/ctypes.html

Center of mass
https://stackoverflow.com/questions/37519238/python-find-center-of-object-in-an-image
