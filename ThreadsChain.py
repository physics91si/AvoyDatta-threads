import threading

def main():
	nThreads = 50
	threads=[]
	for i in range(1, nThreads + 1):
		threadName = "thread" + str(i)
		threadName = threading.Thread(target = helloCmd, args = (i,))
		threadName.start()
		threads.append(threadName)
	
	for t in threads:
		threadName.join()


def helloCmd(i):
	msg = "Hello from Thread" + str(i) + "!"
	print (msg)

main()