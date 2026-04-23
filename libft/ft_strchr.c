#include "libft.h"

char	*ft_strchr(const char *s, int c)
{
	char	*ptr;

	ptr = (char *)s;
	while (*ptr)
	{
		if (*ptr == (char)c)
			return (ptr);
		ptr++;
	}
	if (c == '\0')
		return (ptr);
	return (NULL);
}

/*
#include <stdio.h>
int	main()
{
	const char *test = "test";
	printf("%s\n", ft_strchr(test, 101));
}
*/
