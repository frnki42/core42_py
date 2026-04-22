#include "libft.h"

void	ft_striteri(char *s, void (*f)(unsigned int, char*))
{
	unsigned int	i;

	if (!s)
		return ;
	i = -1;
	while (s[++i])
		f(i, &s[i]);
}
/*
#include <stdio.h>
void	zero_char(unsigned int i, char *str)
{
	 *str = '0';
	 (void)i;
}

int main()
{
	char	str[21] = "42424242424242424242";

	ft_striteri(str, zero_char);
	printf("%s\n", str);
}
*/
