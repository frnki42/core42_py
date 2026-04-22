#include "libft.h"

char	*ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	size_t	i;
	char	*str;

	if (!s)
		return (NULL);
	i = -1;
	str = malloc(ft_strlen(s) + 1);
	if (!str)
		return (NULL);
	while (s[++i])
		str[i] = f(i, s[i]);
	str[i] = '\0';
	return (str);
}
/*
#include <stdio.h>
char	add_index(unsigned int i, char c)
{
	return (i + c);
}

int main()
{
	char	*mapi;

	mapi = ft_strmapi("00000", add_index);
	printf("add_index applied to 00000: %s\n", mapi);
	free(mapi);

	mapi = ft_strmapi("aaaaa", add_index);
	printf("add_index applied to 00000: %s\n", mapi);
	free(mapi);
}
*/
