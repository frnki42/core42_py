/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   pf_putnbr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: .frnki <marvin@42.fr>                      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/20 04:20:42 by .frnki            #+#    #+#             */
/*   Updated: 2026/04/20 16:20:42 by .frnki           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "ft_printf.h"

int	pf_putnbr(long long nbr, int size)
{
	char		tmp;

	if (nbr < 0)
	{
		size += write(1, "-", 1);
		nbr = -nbr;
	}
	if (nbr > 9)
		size = pf_putnbr(nbr / 10, size);
	tmp = nbr % 10 + '0';
	size += write(1, &tmp, 1);
	return (size);
}
/*
#include <stdio.h>
int	main()
{
	printf(" returns size: %i\n", pf_putnbr(0, 0));
	printf(" returns size: %i\n", pf_putnbr(2147483647, 0));
	printf(" returns size: %i\n", pf_putnbr(-2147483648, 0));
	printf(" returns size: %i\n", pf_putnbr(4294967295, 0));
}
*/
