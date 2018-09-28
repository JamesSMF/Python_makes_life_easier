# A simple Makefile
HelloUser: HelloUser.class
	echo Main-class: HelloUser > Manifest
	jar cvfm HelloUser.jar Manifest HelloUser.class
	rm Manifest

HelloUser.class: HelloUser.java
	javac -Xlint HelloUser.java

clean:
	rm -f HelloUser.jar HelloUser.class
