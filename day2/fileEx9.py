lines=['안녕하세요','반갑습니다.']

with open('data/greet_utf8.txt', 'w', encoding='utf-8') as file:
    for line in lines:
        file.write(line)


