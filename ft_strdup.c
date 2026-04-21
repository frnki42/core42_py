#include "libft.h"

char	*ft_strdup(const char *s)
{
	char	*dup;
	size_t	len;

	len = ft_strlen(s) + 1;
	dup = malloc(len);
	if (!dup)
		return (NULL);
	return (ft_memcpy(dup, s, len));
}
/*
#include <stdio.h>
int	main()
{
	char *s = "wsg? does this work, or no?";
	printf("%s\n", ft_strdup(s));
}
*/
