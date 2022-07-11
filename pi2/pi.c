// from https://cffi.readthedocs.io/en/latest/overview.html#if-you-don-t-have-an-already-installed-c-library-to-call
# include <stdlib.h>
# include <math.h>

/* Returns a very crude approximation of Pi
   given a int: a number of iteration */
float pi_approx(unsigned int n) { // change to unsigned

  double i,x,y,sum=0;

  if (n < 10) {  // minimal value guard
    n = 10;
  }

  for (i=0;i<n;i++) {

    x=rand();
    y=rand();

    if (sqrt(x*x+y*y) < sqrt((double)RAND_MAX*RAND_MAX))
      sum++;
  }

  return 4*(float)sum/(float)n; }