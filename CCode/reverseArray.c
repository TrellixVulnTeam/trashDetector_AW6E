#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>



int* reverseArray(int a_count, int* a, int* result_count) {
	if(a_count == 1){
		*result_count = 1;
		return a;
		  }
	 else{
            *result_count = a_count; 
             int temp = 0;
            for (int i = 0; i < (int)floor(a_count/2); i++)
	    {
	      temp = a[i]; 
	      a[i] = a[a_count-1-i];
	      a[a_count-1-i] = temp;
	

	   
	    
	    }
	    return a;
	 }	



	 
}


	 int main()

	 {
		 int TestArray[9] = {1,2,3,4,5,6,7,8,9 };
		 int *reverse = reverseArray(9,TestArray,0);
	 
	 }
