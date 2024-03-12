#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: Pointer to a list oftype listint_t.
 *
 * Return: # 1 if cycle found.
 *         # 0 otherwise.
 */

int check_cycle(listint_t *list)
{
	listint_t *head = list;
	listint_t *current = list;

	while (current)
	{
		if (current->next == head)
			return (1);
		current = current->next;
	}
	return (0);
}
