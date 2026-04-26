/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: elfemboc <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/23 14:58:47 by elfemboc          #+#    #+#             */
/*   Updated: 2026/04/23 15:10:04 by elfemboc         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

static size_t	get_size(long nbr)
{
	size_t	size;

	size = 0;
	if (nbr < 1)
		size++;
	while (nbr)
	{
		size++;
		nbr /= 10;
	}
	return (size);
}

static char	*set_str(long nbr, size_t size)
{
	char	*str;
	size_t	start;

	str = malloc(size + 1);
	if (!str)
		return (NULL);
	start = 0;
	if (nbr < 0)
	{
		nbr = -nbr;
		str[0] = '-';
		start = 1;
	}
	str[size] = '\0';
	while (size-- > start)
	{
		str[size] = nbr % 10 + '0';
		nbr /= 10;
	}
	return (str);
}

char	*ft_itoa(int n)
{
	long	nbr;
	size_t	size;

	nbr = n;
	size = get_size(nbr);
	return (set_str(nbr, size));
}
/*
#include <stdio.h>
int	main()
{
	char	*free_me;

	free_me = ft_itoa(0);
	printf("%s\n", free_me);
	free(free_me);
}
*/
