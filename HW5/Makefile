NQueens: Bard.class
	echo Main-class: Bard > Manifest
	jar cvfm Bard.jar Manifest Bard.class
	rm Manifest

NQueens.class: Bard.java
	javac -Xlint Bard.java

clean:
	rm -f Bard.jar Bard.class
