import socket
lstNames = ['google.com', 'facebook.com', 'yahoo.com', 'wordpress.com']  
for n in lstNames:
    try:
        print(socket.gethostbyname(n), n, sep = '\t')
    except:
        continue
