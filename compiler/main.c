#include <stdio.h>
extern int our_code() asm("our_code_label");

int main(int argc, char** argv) {
	int result = our_code();
	printf("%d\n", result);
	return 0;
} 
