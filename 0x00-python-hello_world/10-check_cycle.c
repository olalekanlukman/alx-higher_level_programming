#include "lists.h"

int check_cycle(listint_t *list)
{
	const listint_t *current;
	
	if (list == NULL)
		return (0);
	current = list;
	if (list == current->next)
		return (0);
	while (current->next != NULL)
	{
		current = current->next;
		if (current->next == list)
			return (1);
	}
	return (0);
}
