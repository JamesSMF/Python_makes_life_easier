package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@SpringBootApplication
public class SpringBoot01HelloworldApplication {

	public static void main(String[] args) {
		SpringApplication.run(SpringBoot01HelloworldApplication.class, args);
	}

}

@Controller 
class HelloController{
   // It receives the request "hello" sended from the browser
   @RequestMapping("/")
   @ResponseBody
   public String hello() {
      return "Hello Spring Boot\n";
   }
}
