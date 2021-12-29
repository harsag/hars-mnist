# hars-mnist
Handwritten digit classifier based on Deep Learning model trained on MNIST data

This application uses fastai library (https://fast.ai) which internally uses PyTorch.

1. The application has a canvas (ipycanvas) to draw a digit and Identify button for the user.
https://github.com/harsag/hars-mnist/blob/main/harshad_mnist_app1.ipynb

2. The model has 2 linear layers and is trained on MNIST dataset for 40 epochs using CrossEntophyLossFlat loss function.
https://github.com/harsag/hars-mnist/blob/main/harshad_mnist_classifier_jupyter.ipynb
CrossEntrophyLoss uses log and softmax operations to distribute the probabilities to the last layer that has 10 activations.

The code has some other files for other variations of the neural network but are mostly similar to the main files mentioned above.

References taken from
1. https://fast.ai
2. Thanks to many contributors in https://forums.fast.ai. Some links that were really helpful are below.
https://forums.fast.ai/t/lesson-4-official-topic/68643/311
https://forums.fast.ai/t/mnist-loss-function-from-chapter-4/87464

3. A big thanks to https://github.com/martinRenou who has created many libraries like https://github.com/martinRenou/ipycanvas.

4. Special thanks to Jeremy Howard and fast.ai team for the amazing course to learn Deep Learning.

How to run this app
---------------------
Simply click https://mybinder.org/v2/gh/harsag/hars-mnist/HEAD?urlpath=%2Fvoila%2Frender%2Fharshad_mnist_app1.ipynb and it will launch a docker for you form mybinder.
If this does not work, please follow below steps.
1. Go to https://mybinder.org/
2. GitHub repository name or URL = https://github.com/harsag/hars-mnist
3. URL to open (optional) = /voila/render/harshad_mnist_app1.ipynb 
4. Select the value "URL" from the dropdown next to /voila/render/harshad_mnist_app1.ipynb
5. Click launch button

![image](https://user-images.githubusercontent.com/89522672/147566406-754d5590-cf57-44c4-829e-b420fae6f54a.png)

The app looks like the screen below
![image](https://user-images.githubusercontent.com/89522672/147563354-bbac25c1-8e99-4a88-90ca-a03007f0a1c6.png)
