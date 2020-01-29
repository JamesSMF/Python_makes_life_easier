math : math.o
	gcc -o math math.o
	rm math.o

math.o : math.c
	gcc -c -std=c99 -Wall math.c

clean :
	rm -f math math.o
check :
	valgrind --leak-check=full math in out
