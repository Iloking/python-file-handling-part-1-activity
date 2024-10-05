file = open('Codingal.txt', 'r')
content = file.read()
print(content)
file.close()

print("\n=====================\n")

file_8_char = open('Codingal.txt', 'r')
content_8_char = file_8_char.read(8)
print(content_8_char)
file_8_char.close()
