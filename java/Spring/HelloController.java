package com.mycompany.app;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
 
class HelloController{
   // It receives the request "hello" sended from the browser
   @RequestMapping("/")
   @ResponseBody
   public String hello() {
      return "Hello Spring Boot"
   }
}
