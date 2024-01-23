#include <stdio.h>
#include "dog.h"

/**
 * print_dog - Prints a struct dog.
 * @d: A pointer to a dog type structure.
 */

void print_dog(struct dog *d)
{
	if (d)
	{
		printf("Name: %s\n", d->name == NULL ? "(nil)" : d->name);
		printf("Name: %f\n", d->age);
		printf("Name: %s\n", d->owner == NULL ? "(nil)" : d->owner);
	}
}
