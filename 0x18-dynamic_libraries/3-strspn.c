#include "main.h"
#include <string.h>
#include <stdio.h>
/**
 * _strspn - a function that gets the length of a prefix substring.
 * @s: an input string
 * @accept: an input character with to locate into string s
 * Return: returns pointer to c position
 */
unsigned int _strspn(char *s, char *accept)
{
	return (strspn(s, accept));
}
