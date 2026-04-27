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

int	pf_putnbr(long long nbr, int size, int base, int upper)
{
	char	*hexa;

	hexa = "0123456789abcdef";
	if (upper)
		hexa = "0123456789ABCDEF";
	if (nbr < 0)
	{
		size += write(1, "-", 1);
		nbr = -nbr;
	}
	if (nbr > base - 1)
		size = pf_putnbr(nbr / base, size, base, upper);
	size += write(1, &hexa[nbr % base], 1);
	return (size);
}
/*
#include <stdio.h>
int	main()
{
	printf(" returns size: %i\n", pf_putnbr(0, 0, 16, 1));
	printf(" INT_MAX size: %i\n", pf_putnbr(2147483647, 0, 16, 1));
	printf(" INT_MIN size: %i\n", pf_putnbr(-2147483648, 0, 16, 1));
	printf(" UINT_MAX size: %i\n", pf_putnbr(4294967295, 0, 16, 1));
	printf(" LLONG_MAX size: %i\n", pf_putnbr(9223372036854775807, 0, 16, 1));
}
*/
