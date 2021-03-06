# -*- coding: utf-8 -*-
"""harshad_mnist_classifier_colab.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lxE18IMRNVaxWQU-zFFhD0R3gsBGY6Gf
"""

#hide
!pip install -Uqq fastbook
import fastbook
fastbook.setup_book()

#hide
from fastai.vision.all import *
from fastai.vision.widgets import *

path = untar_data(URLs.MNIST)

#hide
Path.BASE_PATH = path

path.ls()

(path/'training').ls()

training = path/'training'
training.ls().sorted()

testing = path/'testing'
testing.ls().sorted()

ones = (path/'training'/'1').ls().sorted()
twos = (path/'training'/'2').ls().sorted()
threes = (path/'training'/'3').ls().sorted()
fours = (path/'training'/'4').ls().sorted()
fives = (path/'training'/'5').ls().sorted()
sixes = (path/'training'/'6').ls().sorted()
sevens = (path/'training'/'7').ls().sorted()
eights = (path/'training'/'8').ls().sorted()
nines = (path/'training'/'9').ls().sorted()
zeros = (path/'training'/'0').ls().sorted()
valid_ones = (path/'testing'/'1').ls().sorted()
valid_twos = (path/'testing'/'2').ls().sorted()
valid_threes = (path/'testing'/'3').ls().sorted()
valid_fours = (path/'testing'/'4').ls().sorted()
valid_fives = (path/'testing'/'5').ls().sorted()
valid_sixes = (path/'testing'/'6').ls().sorted()
valid_sevens = (path/'testing'/'7').ls().sorted()
valid_eights = (path/'testing'/'8').ls().sorted()
valid_nines = (path/'testing'/'9').ls().sorted()
valid_zeros = (path/'testing'/'0').ls().sorted()
ones

one_tensors = [tensor(Image.open(o)) for o in ones]
two_tensors = [tensor(Image.open(o)) for o in twos]
three_tensors = [tensor(Image.open(o)) for o in threes]
four_tensors = [tensor(Image.open(o)) for o in fours]
five_tensors = [tensor(Image.open(o)) for o in fives]
six_tensors = [tensor(Image.open(o)) for o in sixes]
seven_tensors = [tensor(Image.open(o)) for o in sevens]
eight_tensors = [tensor(Image.open(o)) for o in eights]
nine_tensors = [tensor(Image.open(o)) for o in nines]
zero_tensors = [tensor(Image.open(o)) for o in zeros]
valid_1_tensors = [tensor(Image.open(o)) for o in valid_ones]
valid_2_tensors = [tensor(Image.open(o)) for o in valid_twos]
valid_3_tensors = [tensor(Image.open(o)) for o in valid_threes]
valid_4_tensors = [tensor(Image.open(o)) for o in valid_fours]
valid_5_tensors = [tensor(Image.open(o)) for o in valid_fives]
valid_6_tensors = [tensor(Image.open(o)) for o in valid_sixes]
valid_7_tensors = [tensor(Image.open(o)) for o in valid_sevens]
valid_8_tensors = [tensor(Image.open(o)) for o in valid_eights]
valid_9_tensors = [tensor(Image.open(o)) for o in valid_nines]
valid_0_tensors = [tensor(Image.open(o)) for o in valid_zeros]
len(one_tensors)

img=one_tensors[1]
show_image(one_tensors[1]);

stacked_ones = torch.stack(one_tensors).float()/255
stacked_twos = torch.stack(two_tensors).float()/255
stacked_threes = torch.stack(three_tensors).float()/255
stacked_fours = torch.stack(four_tensors).float()/255
stacked_fives = torch.stack(five_tensors).float()/255
stacked_sixes = torch.stack(six_tensors).float()/255
stacked_sevens = torch.stack(seven_tensors).float()/255
stacked_eights = torch.stack(eight_tensors).float()/255
stacked_nines = torch.stack(nine_tensors).float()/255
stacked_zeros = torch.stack(zero_tensors).float()/255
stacked_1_valid = torch.stack(valid_1_tensors).float()/255
stacked_2_valid = torch.stack(valid_2_tensors).float()/255
stacked_3_valid = torch.stack(valid_3_tensors).float()/255
stacked_4_valid = torch.stack(valid_4_tensors).float()/255
stacked_5_valid = torch.stack(valid_5_tensors).float()/255
stacked_6_valid = torch.stack(valid_6_tensors).float()/255
stacked_7_valid = torch.stack(valid_7_tensors).float()/255
stacked_8_valid = torch.stack(valid_8_tensors).float()/255
stacked_9_valid = torch.stack(valid_9_tensors).float()/255
stacked_0_valid = torch.stack(valid_0_tensors).float()/255
stacked_ones

train_x = torch.cat([stacked_ones, stacked_twos, stacked_threes, stacked_fours, stacked_fives, stacked_sixes, stacked_sevens, stacked_eigths, stacked_nines, stacked_zeros]).view(-1, 28*28)
train_y = tensor([1]*len(ones) + [2]*len(twos) + [3]*len(threes) + [4]*len(fours) + [5]*len(fives) + [6]*len(sixes) + [7]*len(sevens) + [8]*len(eights) + [9]*len(nines) + [0]*len(zeros)).unsqueeze(1)
train_dset = list(zip(train_x,train_y))

x,y = train_dset[0]
x.shape,y, len(train_dset)

valid_x = torch.cat([stacked_1_valid, stacked_2_valid, stacked_3_valid, stacked_4_valid, stacked_5_valid, stacked_6_valid, stacked_7_valid, stacked_8_valid, stacked_9_valid, stacked_0_valid]).view(-1, 28*28)
valid_y = tensor([1]*len(stacked_1_valid) + [2]*len(stacked_2_valid) + [3]*len(stacked_3_valid) + [4]*len(stacked_4_valid) + [5]*len(stacked_5_valid) + [6]*len(stacked_6_valid) + [7]*len(stacked_7_valid) + [8]*len(stacked_8_valid) + [9]*len(stacked_9_valid) + [0]*len(stacked_0_valid)).unsqueeze(1)
test_dset = list(zip(valid_x,valid_y))
x,y = test_dset[0]
x.shape,y, len(test_dset)

train_dl = DataLoader(train_dset, batch_size=256, shuffle=True)
xb,yb = first(train_dl)
xb.shape,yb.shape

test_dl = DataLoader(test_dset, batch_size=256, shuffle=False)
xb,yb = first(test_dl)
xb.shape,yb.shape

dls = DataLoaders(train_dl, test_dl)

class NeuralNetwork(nn.Module):
  def __init__(self, input_size, hidden_size, num_classes):
    super(NeuralNetwork, self).__init__()
    self.linear1 = nn.Linear(input_size, hidden_size)
    self.relu = nn.ReLU()
    self.linear2 = nn.Linear(hidden_size, num_classes)

  def forward(self, xb):
    res = self.linear1(xb)
    res = self.relu(res)
    res = self.linear2(res)

    return res

model = NeuralNetwork(input_size=28*28, hidden_size=30, num_classes=10)

def init_params(size, std=1.0): 
  return (torch.randn(size)*std).requires_grad_()

w1 = init_params((28*28,30))
b1 = init_params(30)
w2 = init_params((30,10)) # 10 final activations
b2 = init_params(10) # 10 final activations 
params = w1,b1,w2,b2

loss_function1 = nn.CrossEntropyLoss()
#loss_f = CrossEntropyLossFlat()

# check shape of model predictions one a single batch xb
prediction_xb = model(xb)
prediction_xb.shape

#learn = Learner(dls, simple_net, opt_func=SGD, loss_func=mnist_loss, metrics=batch_accuracy)
learn = Learner(dls, model,loss_func=loss_function1, metrics=accuracy)
#learn = Learner(dls, model,loss_func=loss_f, metrics=accuracy)

learn.fit_one_cycle(5)
#learn.fit(40, 0.1)
#learn.fit_one_cycle(1, 0.1)

learn.export()

path = Path()
path.ls(file_exts='.pkl')

learn_inf = load_learner(path/'export.pkl')

learn_inf.predict(img)

learn_inf.dls.vocab