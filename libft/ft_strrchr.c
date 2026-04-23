#include "libft.h"

char	*ft_strrchr(const char *s, int c)
{
	char	*ptr;

	ptr = NULL;
	while (*s)
	{
		if (*s == (char)c)
			ptr = (char *)s;
		s++;
	}
	if (c == '\0')
		return ((char *)s);
	return (ptr);
}
/*
#include <stdio.h>
int	main()
{
	const char *test = "tester";
	printf("%s\n", ft_strrchr(test, 101));
}
*/
