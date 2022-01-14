#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"

/**
 * infinite_while - infinite loop
 * Return: 0 in the end
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 zombie process
 * Return: 0 on sucess
*/
int main(void)
{
	int num_zombie = 0;

	pid_t pid;

	while (num_zombie < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			num_zombie++;
		}
		else
			break;
	}
	infinite_while();

	return (0);
}
