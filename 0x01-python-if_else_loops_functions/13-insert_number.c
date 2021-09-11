#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a num into a sorted linked list
 * @head: of the list
 * @number: of the node
 *
 * Return: listint_t
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *ptr1, *ptr2;

	ptr1 = *head;
	ptr2 = malloc(sizeof(listint_t));
	if (ptr2 == NULL)
	{
		free(ptr2);
		return (NULL);
	}
	ptr2->n = number;
	ptr2->next = NULL;

	if (ptr1->n >= number)
	{
		ptr2->next = ptr1;
		*head = ptr2;
	}
	while (ptr1->next)
	{
		if (ptr1->n >= number)
		{
			ptr2->next = ptr1;
			temp->next = ptr2;
			break;
		}
		temp = ptr1;
		ptr1 = ptr1->next;
	}
	if (ptr1->next == NULL)
	{
		ptr2->next = ptr1;
		temp->next = ptr2;
	}
	return (ptr2);
}
