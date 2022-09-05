#include "main.h"
#include <string.h>
/**
 * *_strchr - a function that locates a character in a string
 * @s: input string in which a character is to be found
 * @c: input character to be located
 * Return: a pointer
 */
char *_strchr(char *s, char c)
{
	return (strchr(s, c));
}
