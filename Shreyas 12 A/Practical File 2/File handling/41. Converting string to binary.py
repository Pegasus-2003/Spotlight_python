# Converting string to Binary
msg="HELLO !"
f=open('myfile.bin','wb')
f.write(msg.encode())
f.write(b'Anyone there ???')
f.close()
