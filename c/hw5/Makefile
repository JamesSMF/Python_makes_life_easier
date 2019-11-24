#------------------------------------------------------------------------------
# CSE120 hw5
# Group members: Yufan Zhu, James Li
# Makefile:
#    % Usage:
#       make                   -- generates executable files
#       make clean             -- clean up executable files
#------------------------------------------------------------------------------

all: matmul matmul_transpose matmul_blocking

matmul : matmul.c
	gcc -o matmul matmul.c

matmul_blocking : matmul_blocking.c
	gcc -o matmul_blocking matmul_blocking.c

matmul_transpose : matmul_transpose.c
	gcc -o matmul_transpose matmul_transpose.c

clean :
	rm -f matmul matmul_transpose matmul_blocking
