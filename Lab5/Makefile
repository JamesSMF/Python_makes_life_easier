queueClient : queueClient.o
	gcc -o queueClient queueClient.o

queueClient.o : queueClient.c
	gcc -c -std=c99 -Wall queueClient.c

clean :
	rm -f queueClient queueClient.o
check :
	valgrind --leak-check=full queueClient in out
