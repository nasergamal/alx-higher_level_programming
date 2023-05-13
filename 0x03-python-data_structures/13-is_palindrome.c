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
	int i = 0, e = 0;
	listint_t *ptr = NULL, *s = NULL;

	if (head == NULL)
	      return (0);
	ptr = s = *head;
	while (ptr != NULL &&  ptr->next != NULL)
	{
		ptr = ptr->next;
		i += 2;
	}
	for (;  i > e ; i -= 2, e += 2)
	{
		if (s[i].n != s[e].n)
		{
			return (0);
		}
	}
	return (1);
}
