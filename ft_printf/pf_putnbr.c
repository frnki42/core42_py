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

int	pf_putnbr(int nbr, int size)
{
	long long	n;
	char		tmp;

	n = nbr;
	if (n < 0)
	{
		size += write(1, "-", 1);
		n = -n;
	}
	if (n > 9)
		size = pf_putnbr(n / 10, size);
	tmp = n % 10 + '0';
	size += write(1, &tmp, 1);
	return (size);
}
/*
#include <stdio.h>
int	main()
{
	pf_putnbr(0, 0);
	write(1, "\n", 1);
	pf_putnbr(2147483647, 0);
	write(1, "\n", 1);
	pf_putnbr(-2147483648, 0);
	write(1, "\n", 1);
}
*/
