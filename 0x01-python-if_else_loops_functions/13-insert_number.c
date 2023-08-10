#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
/**
 * *insert_node - A function that inserts a number in a singly linked list
 * @head: The pointer to the start of the list
 * @number: Number in question
 *
 * Return: Address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new_node;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = number;

	if (node == NULL || node->n >= number)
	{
		new_node->next = node;
		*head = new_node;
		return (new_node);
	}
	while (node && node->next && node->next->n < number)
	{
		node = node->next;
	}
	new_node->next = node->next;
	node->next = new_node;
	return (new_node);
}

