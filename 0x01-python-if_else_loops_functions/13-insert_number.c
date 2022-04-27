#include "lists.h"

/**
 * insert_node - function single lists
 *
 * @head: double pointer listint_t
 * @number: int
 * Return: new
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new = NULL;
	listint_t *new_new = NULL;

	new = malloc(sizeof(listint_t));
	if (new == NULL || head == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (*head);
	}
	while (current != NULL && current->n < number)
	{
		new_new = current;
		current = current->next;
	}
	new_new->next = new;
	new->next = current;

	return (new);
}
