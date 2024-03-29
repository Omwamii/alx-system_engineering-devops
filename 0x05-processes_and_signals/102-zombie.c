#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int infinite_while(void);

/**
 * main - creates zombies
 *
 * Return: exit status
 */
int main(void)
{
	int i;

	for (i = 0; i < 5; i++)
	{
		if (fork() == 0) /* child */
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
		else
			sleep(1);
	}
	infinite_while(); /* prevent parent from terminating and orphaning children */
	return (0);
}

/**
 * infinite_while - runs an infinite "sleep" loop
 *
 * Return: exit status
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
