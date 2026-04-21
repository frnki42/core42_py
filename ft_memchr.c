#include "libft.h"

void	*ft_memchr(const void *s, int c, size_t n)
{
	unsigned char *ptr;

	ptr = (unsigned char *)s;
	while (n--)
	{
		if (*ptr == (unsigned char)c)
			return (ptr);
		ptr++;
	}
	return (NULL);
}
/*
#include <stdio.h>
int main()
{
	char *test = "42Vienna";
	void *mem_adr;
	
	mem_adr = ft_memchr(test, 'X', 42);
	if (mem_adr)
		printf("match found at %p\n", mem_adr);
	else
		printf("no match found in %s\n", test);
}
*/
