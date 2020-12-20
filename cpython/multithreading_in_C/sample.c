/*
Geeks for Geeks Article:
https://www.geeksforgeeks.org/multithreading-in-cpp/
*/
#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h> //Header file for sleep(). man 3 sleep for details. 
#include <pthread.h> 

// A normal C function that is executed as a thread 
// when its name is specified in pthread_create() 

/*
SAMPLE CODE:


void *myThreadFun(void *vargp) 
{ 
	sleep(1); 
	printf("Printing GeeksQuiz from Thread \n"); 
	return NULL; 
} 

int main() 
{ 
	pthread_t thread_id; 
	printf("Before Thread\n"); 
	pthread_create(&thread_id, NULL, myThreadFun, NULL); 
	pthread_join(thread_id, NULL); 
	printf("After Thread\n"); 
	exit(0); 
}
*/
void *workerFunction(void *vargp)
{
	long long int count=0;
	for(long long int index=0;index<1000000;index++)
	{
		count+=index;
	}
	printf("\n%lld",count);
	printf("\nThread Runnning!");
}
int main(){
	int var;
	pthread_t thread_id[10];
	printf("Before Threading!");
	clock_t begin=clock();
	for(int thread_index=0;thread_index<10;thread_index++)
	{
		pthread_create(&thread_id[thread_index],NULL,workerFunction,NULL);
	}
	for(int thread_index=0;thread_index<10;thread_index++)
	{
		pthread_join(thread_id[thread_index], NULL);
	}
	clock_t end=clock();
	printf("\nTime Taken in s: %f",(float)(end-begin));
	return 0;
}