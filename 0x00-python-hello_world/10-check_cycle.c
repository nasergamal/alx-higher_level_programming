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

	fast = slow = list;
	while (slow && fast && fast->next)
	{
		slow = slow->next, fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
