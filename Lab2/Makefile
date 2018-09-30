FileReverse: FileReverse.class
	echo Main-class: FileReverse > Manifest
	jar cvfm FileReverse.jar Manifest FileReverse.class
	rm Manifest

FileReverse.class: FileReverse.java
	javac -Xlint FileReverse.java

clean:
	rm -f FileReverse.jar FileReverse.class
