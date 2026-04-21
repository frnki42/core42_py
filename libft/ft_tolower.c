int	ft_tolower(int c)
{
	if (c >= 'A' && c <= 'Z')
		return (c + 32);
	return (c);
}
/*
#include <stdio.h>
int	main()
{
	printf("%i\n", ft_tolower('W'));
}
*/
