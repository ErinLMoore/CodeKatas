def log(results):
    with open('logfile.txt', 'a') as f:
        f.write(results+ '\n')
    print f.closed
