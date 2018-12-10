NQueens: NQueens.class
	echo Main-class: NQueens > Manifest
	jar cvfm NQueens.jar Manifest NQueens.class
	rm Manifest

NQueens.class: NQueens.java
	javac -Xlint NQueens.java

clean:
	rm -f NQueens.jar NQueens.class
