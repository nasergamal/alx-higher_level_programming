#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - insert node in a sorted singly linked list
 * @head: the orginal list
 * @number: the nuber to be added
 *
 * Return: address of newnode if succeded or NULL in failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newnode, *ptr = *head;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;
	newnode->next = NULL;
	while (ptr)
	{
		if (ptr->next == NULL || ptr->next->n > number)
		{
			newnode->next = ptr->next;
			ptr->next = newnode;
			return (newnode);
		}
		ptr = ptr->next;
	}
	return (NULL);
}
