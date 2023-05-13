#include <stddef.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - check if a linked list is palindrome
 * @head: the linked list to be checked
 *
 * Return: 1 if palindrome 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	char lis[1024], f = 1;
	int i = 0, n;
	listint_t *ptr = NULL;

	ptr = *head;
	while (ptr != NULL)
	{
		lis[i] = ptr->n;
		ptr = ptr->next;
		i++;
	}
	lis[i] = '\0';
	if (!i)
		return (0);
	for (i -= 1, n = 0; i != n - 1 && i >= 0; i--, n++)
	{
		if (lis[i] != lis[n])
		{
			f = 0;
			break;
		}
	}
	if (f && ((i == -1 && !lis[n]) || i == n - 1))
		return (1);
	return (0);
}
