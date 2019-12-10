import struct

struct_fmt = '=16s2fi'
city_info = [
    #city,latitude, longitude, population
    ('서울'.encode(encoding='utf-8'), 37.566535,126.977969,9820000),
    ('서울'.encode(encoding='utf-8'), 37.566535,126.977969,9820000),
    ('서울'.encode(encoding='utf-8'), 37.566535,126.977969,9820000),
    ('서울'.encode(encoding='utf-8'), 37.566535,126.977969,9820000)
]

with open('data/cities.data','wb') as file:
    for city in city_info:
        file.write(struct.pack(struct_fmt, *city))

struct_len = struct.calcsize(struct_fmt)

cities=[]
with open('data/cities.data','rb') as file:
    while True:
        buffer=file.read(struct_len)
        if not buffer: break
        city = struct.unpack(struct_fmt, buffer)
        cities.append(city)

    for city in cities:
        name = city[0].decode(encoding='utf-8'.replace('\x00',''))
        print('city:{0}, Lat/Long: {1}/{2}, Population:{3}'.format(name,city[1],city[2],city[3]))
