// This package is your groupID, which tells the compiler which dependencies
// to use.
package com.mycompany.app;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;


/*
 * This tells the compiler that we are writing a Spring Boot App
 */

@SpringBootApplication
public class DemoApplicationJAR {
   public static void main(String[] args) {
      // start the spring app
      SpringApplication.run(DemoApplicationJAR.class, args);
   }
}
