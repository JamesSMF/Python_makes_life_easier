queue : queue.o
	gcc -o queue queue.o queueClient.c

queue.o : queue.c
	gcc -c -std=c99 -Wall queue.c queueClient.c

clean :
	rm -f queue queue.o queueClient
check :
	valgrind --leak-check=full queue in out
