#include "libft.h"

void	ft_putnbr_fd(int n, int fd)
{
	char	tmp;
	long	nbr;

	nbr = n;
	if (nbr < 0)
	{
		write(fd, "-", 1);
		nbr = -nbr;
	}
	if (nbr > 9)
		ft_putnbr_fd(nbr / 10, fd);
	tmp = nbr % 10 + '0';
	write(fd, &tmp, 1);
}
/*
int	main()
{
	ft_putnbr_fd(-420, 1);
}
*/
