import numpy as np
import sys
from math import sqrt, pi, cos, sin
from random import random, shuffle
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import plot_model


# 0 = raw_data
# 1 = expected
# 2 = random_noise
# 3 = expected_random
def generateData(file):
    inp_file = ""
    out_file = ""
    if file == "0":
        inp_file = open("input_rawdata.txt", 'r').read().splitlines()
        out_file = open("output_rawdata.txt", 'r').read().splitlines()
    if file == "1":
        inp_file = open("input_expected.txt", 'r').read().splitlines()
        out_file = open("output_expected.txt", 'r').read().splitlines()
    if file == "2":
        inp_file = open("input_random_noise.txt", 'r').read().splitlines()
        out_file = open("output_random_noise.txt", 'r').read().splitlines()
    if file == "3":
        inp_file = open("input_expected_random.txt", 'r').read().splitlines()
        out_file = open("output_expected_random.txt", 'r').read().splitlines()
    if file != "0":
        for item in range(len(out_file)):
            out_file[item] = out_file[item][1:-1]
        for item in range(len(inp_file)):
            inp_file[item] = inp_file[item][1:-1]
    input_num = [[int(y) for y in x.split(",")] for x in inp_file]
    output_num = [[float(y) for y in x.split(",")] for x in out_file]
    return input_num, output_num

data_type = sys.argv[1]
xt, yt = generateData(data_type)
shuffle(xt)
shuffle(yt)
x_train = np.array(xt[0:int(len(xt)*.9)])
y_train = np.array(yt[0:int(len(yt)*.9)])
x_test = np.array(xt[int(len(xt)*.9)::])
y_test = np.array(yt[int(len(yt)*.9)::])


print(x_train)

model = Sequential()
model.add(Dense(512, input_dim=5, activation='relu'))
model.add(Dropout(0.01))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.01))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.01))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.01))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.01))
model.add(Dense(5, activation='sigmoid'))

model.compile(loss='mean_squared_logarithmic_error', optimizer='adam', metrics=['accuracy'])
weights_file = "crayfish_weights_" + data_type + ".h5" 
model.load_weights(weights_file)
model.fit(x_train, y_train, epochs=100, batch_size=1000)
score = model.evaluate(x_test, y_test)
final_accuracy = str(score[1])
print("Final accuracy:", final_accuracy)
model.save_weights(weights_file)
plot_model(model, to_file="model.png", show_shapes=True)
#input_weights = model.layers[0].get_weights()
#for item in range(len(input_weights)):
#    print(item, sum(abs(input_weights)))
    
