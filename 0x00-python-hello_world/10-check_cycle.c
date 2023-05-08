#include "lists.h"

/**
 * check_cycle - check for cycle existence in a linked list
 * @list: the list to be checked
 *
 * Return: 0(no cycle) or 1(cycle exists)
 */
int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (!list)
		return (0);
	fast = list->next->next, slow = list->next;

	while (slow->next && fast->next->next)
	{
		if (slow->n == fast->n)
			return (1);
		slow = slow->next, fast = fast->next->next;
	}
	return (0);
}
