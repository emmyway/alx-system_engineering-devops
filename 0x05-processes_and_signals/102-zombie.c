#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - an infinite loop
 * Return: 0
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
 * main - entry point of program
 * description: fxn creates five zombie process
 * Return: 0 on success
 */
int main()
{
	int i;
	pid_t child_pid;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();

		if (child_pid == -1)
		{
			perror("pid");
			exit(EXIT_FAILURE);
		}
		else if (child_pid == 0)
		{
			printf("Zombie process created, PID: %d\n", child_pid);
			exit(EXIT_SUCCESS);
		}
	}
	infinite_while();
	return (0);
}
