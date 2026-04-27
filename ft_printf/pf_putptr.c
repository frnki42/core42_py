/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: .frnki <marvin@42.fr>                      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/20 04:20:42 by .frnki            #+#    #+#             */
/*   Updated: 2026/04/20 16:20:42 by .frnki           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "ft_printf.h"

static int	pf_printptr(uintptr_t ptr, int size)
{
	char	*base;

	base = "0123456789abcdef";
	if (ptr > 15)
		size = pf_printptr(ptr / 16, size);
	size += write(1, &base[ptr % 16], 1);
	return (size);
}

int	pf_putptr(void *p)
{
	uintptr_t	ptr;

	if (!p)
		return (write(1, "(nil)", 5));
	ptr = (uintptr_t)p;
	write(1, "0x", 2);
	return (pf_printptr(ptr, 0) + 2);
}
/*
#include <stdio.h>
int	main()
{
	uintptr_t	test = 42;
	printf(" size: %i\n", pf_putptr(test));
}
*/
