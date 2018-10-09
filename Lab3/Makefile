fileReverse : fileReverse.o
	gcc -o fileReverse fileReverse.o

fileReverse.o : fileReverse.c
	gcc -c -std=c99 -Wall fileReverse.c

clean :
	rm -f fileReverse fileReverse.o
