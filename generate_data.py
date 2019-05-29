import random
inputs_text = open("input_rawdata.txt", 'r').read().splitlines()
outputs_text = open("output_rawdata.txt", 'r').read().splitlines()
input_num = [[int(y) for y in x.split(",")] for x in inputs_text]
output_num = [[float(y) for y in x.split(",")] for x in outputs_text]

input_random_noise = open("input_random_noise.txt", 'w')
output_random_noise = open("output_random_noise.txt", 'w')

input_expected_random = open("input_expected_random.txt", 'w')
output_expected_random = open("output_expected_random.txt", 'w')


for i in range(10000):
    print(i, "/20000")
    for j in range(len(input_num)):
        instr = str(input_num[j]) + "\n"
        outstr = str([x + (random.random()/100) for x in output_num[j]]) + "\n"
        input_random_noise.write(instr)
        output_random_noise.write(outstr)
        input_expected_random.write(instr)
        output_expected_random.write(outstr)


input_expected = open("input_expected.txt", 'w')
output_expected = open("output_expected.txt", 'w')

for l in range(10000):
    print(l+10000, "/20000")
    for m in range(len(input_num)):
        instr = str(input_num[m])
        outstr = str(output_num[m])
        input_expected.write(instr + "\n")
        output_expected.write(outstr + "\n")
        input_expected_random.write(instr + "\n")
        output_expected_random.write(outstr + "\n")
