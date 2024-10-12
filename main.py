# With function
with open('Codingal.txt', 'r') as file:
    print(file.read())
file.close()

with open('Codingal.txt', 'w') as file:
    file.write("I am a penguine and I am 10 years old.")
file.close()

# Split function
with open('Codingal.txt', 'r') as file:
    data = file.readlines()
    print("The words are:")
    for line in data:
        word = line.split()
        print(word)
file.close()
