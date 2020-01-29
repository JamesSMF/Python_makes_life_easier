#include <string.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <math.h>

float Sin(double x){
   float sqr = x * x;
   float self_sin = x * ((sqr * (52785432- 479249 * sqr)-1640635920)*sqr 
      + 11511339840) / (((18361*sqr +3177720)*sqr +277920720)*sqr +
      11511339840);

   return self_sin;
}

float Cos(double x){
   float sqr = x * x;
   float self_cos = ((sqr*(1075032-14615*sqr)-18471600)*sqr+39251520) 
      / (((127*sqr + 16632)*sqr+1154160)*sqr + 11511339840);

   return self_cos;
}

void Tan(){
   for (double x = -2.0 * M_PI; x <= 2 * M_PI; x += (M_PI / 16.0)){
      printf("%.4f   %.8f\n", x, tan(x));
   }
   return;
}

float Exp(double x){
   float curr = 1;
   int counter = 0;
   float Ex = 1;
   float standart = exp(x);
   while(fabs(Ex - standart) > 0.00001){
      curr = curr * x / (++counter);
      Ex += curr;
      printf("\n%f   %f    %f   %d\n",Ex, curr, standart ,counter);
   }

   return Ex;
}

int main(int argc, char** argv){
   // Check number of arguments
   if(argc!=2){
      puts("error: incorrect number of command-line arguments");
      puts("Usage: ./math <flag>");
   }

   // Get the flag option
   switch(argv[1][1]){
      case 's':
         puts("x        Sin             Library         Difference");
         puts("-        ---             -------         ----------");
         for (double x = -2.0 * M_PI; x <= 2 * M_PI; x += (M_PI / 16.0)){
            Sin(x);
            float diff = fabs(Sin(x) - sin(x));
            printf("%.4f", x);
            if(x<0) printf("  ");
            else printf("   ");

            printf("%.8f", sin(x));
            int len = 7 - fabs(sin(x)) / 10;
            if(sin(x) < 0) --len;
            /* if(sin(x)>-0.00000001 && sin(x)<0.00000001) --len; */
            for(int i=0; i<len; ++i)
               printf(" ");

            printf("%.8f", Sin(x));
            len = 7 - fabs(Sin(x)) / 10;
            if(Sin(x) < 0) --len;
            /* if(Sin(x)>-0.00000001 && Sin(x)<0.00000001) --len; */
            for(int i=0; i<len; ++i)
               printf(" ");

            printf("%.8f\n", diff);
         }
         break;
      case 'c':
         puts("x        Cos             Library         Difference");
         puts("-        ---             -------         ----------");
         for (double x = -2.0 * M_PI; x <= 2 * M_PI; x += (M_PI / 16.0)){
            Cos(x);
            float diff = fabs(Cos(x) - cos(x));
            printf("%.4f", x);
            if(x<0) printf("  ");
            else printf("   ");

            printf("%.8f", cos(x));
            int len = 7 - fabs(cos(x)) / 10;
            if(cos(x) < 0) --len;
            /* if(cos(x)>-0.00000001 && cos(x)<0.00000001) --len; */
            for(int i=0; i<len; ++i)
               printf(" ");

            printf("%.8f", Cos(x));
            len = 7 - fabs(Cos(x)) / 10;
            if(Cos(x) < 0) --len;
            /* if(Cos(x)>-0.00000001 && Cos(x)<0.00000001) --len; */
            for(int i=0; i<len; ++i)
               printf(" ");

            printf("%.8f\n", diff);
         }
         break;
      case 't':
         Tan();
         break;
      case 'e':
         for (float x = 0; x<=10; x+=0.1){
            printf("%.4f  ", x);
            printf("%.8f    ", Exp(x));
            printf("%.8f    ", exp(x));
            printf("%.8f\n", Exp(x)-exp(x));
         }
         break;
      case 'a':
         /* Sin(x); */
         /* Cos(x); */
         /* Tan(); */
         /* Exp(); */
         break;
      default:
         break;
   }

   return 0;
}
