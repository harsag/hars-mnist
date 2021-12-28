# hars-mnist
Handwritten digit classifier based on Deep Learning model trained on MNIST data

This application uses fastai library (https://fast.ai) which internally uses PyTorch.

1. The application has a canvas (ipycanvas) to draw a digit and Identify button for the user.
https://github.com/harsag/hars-mnist/blob/main/harshad_mnist_app1.ipynb

2. The model has 2 linear layers and is trained on MNIST dataset for 40 epochs using CrossEntophyLossFlat loss function.
https://github.com/harsag/hars-mnist/blob/main/harshad_mnist_classifier_jupyter.ipynb
CrossEntrophyLoss uses log and softmax operations to distribute the probabilities to the last layer that has 10 activations.

3. I faces some issues in exporting the model from step no 2 above. Finally I used transfer learning (resnet18) and exported a model from there.
https://github.com/harsag/hars-mnist/blob/main/transfer_learning_colab.ipynb
This issue is reported in the forum
https://forums.fast.ai/t/not-able-to-export-learner-failing-with-attributeerror-list-object-has-no-attribute-new-empty/81803/6

The code has some other files for other variations of the neural network but are mostly similar to the main files mentioned above.

References taken from
1. https://fast.ai
2. Thanks to many contributors in https://forums.fast.ai. Some links that were really helpful are below.
https://forums.fast.ai/t/lesson-4-official-topic/68643/311
https://forums.fast.ai/t/mnist-loss-function-from-chapter-4/87464

3. A big thanks to https://github.com/martinRenou who has created many libraries like https://github.com/martinRenou/ipycanvas.

4. Special thanks to Jeremy Howard and fast.ai team for the amazing course to learn Deep Learning.
