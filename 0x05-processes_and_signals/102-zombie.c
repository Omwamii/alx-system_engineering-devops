#include <stdio.h>
#include <unistd.h>

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
		}
	}
	infinite_while();
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
