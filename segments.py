import furl
url = 'https://www.laptopscreen.com/English/model/Acer/ONE~10~S1002-19DM/'
# segments = url.rpartition('/')
# clear_segments = segments[-1]
# print(clear_segments)
f = furl.furl(url)
clear_f = str(f.path).split('/')

print(clear_f[3])

