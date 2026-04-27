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

static int	print_spec(const char **fmt, va_list lst)
{
	(*fmt)++;
	if (**fmt == '%')
		return (pf_putchar('%'));
	else if (**fmt == 'c')
		return (pf_putchar(va_arg(lst, int)));
	else if (**fmt == 's')
		return (pf_putstr(va_arg(lst, char *)));
	else if (**fmt == 'd' || **fmt == 'i')
		return (pf_putnbr(va_arg(lst, int), 0, 10, 0));
	else if (**fmt == 'u')
		return (pf_putnbr(va_arg(lst, unsigned int), 0, 10, 0));
	else if (**fmt == 'x')
		return (pf_putnbr(va_arg(lst, unsigned int), 0, 16, 0));
	else if (**fmt == 'X')
		return (pf_putnbr(va_arg(lst, unsigned int), 0, 16, 1));
	else if (**fmt == 'p')
		return (pf_putptr(va_arg(lst, void *)));
	else if (**fmt == '\0')
		return ((*fmt)--, 0);
	else
		return (pf_putinvalid(**fmt));
}

int	ft_printf(const char *fmt, ...)
{
	va_list	lst;
	int		size;

	if (!fmt)
		return (-1);
	va_start(lst, fmt);
	size = 0;
	while (*fmt)
	{
		if (*fmt == '%')
			size += print_spec(&fmt, lst);
		else
			size += write(1, fmt, 1);
		fmt++;
	}
	va_end(lst);
	return (size);
}
/*
#include <stdio.h>
int	main()
{
	char	*str = "42";

	printf(" | size: %i\n", ft_printf("CHR_TEST: %c", 'c'));
	printf(" | size: %i\n", printf("CHR_TEST: %c", 'c'));
	
	printf(" | size: %i\n", ft_printf("STR_TEST: %s", str));
	printf(" | size: %i\n", printf("STR_TEST: %s", str));

	printf(" | size: %i\n", ft_printf("PTR_TEST: %p", &str));
	printf(" | size: %i\n", printf("PTR_TEST: %p", &str));
	
	printf(" | size: %i\n", ft_printf("DEC_TEST: %d", 42));
	printf(" | size: %i\n", printf("DEC_TEST: %d", 42));

	printf(" | size: %i\n", ft_printf("INT_TEST: %i", 42));
	printf(" | size: %i\n", printf("INT_TEST: %i", 42));

	printf(" | size: %i\n", ft_printf("UINT_TEST: %u", 42));
	printf(" | size: %i\n", printf("UINT_TEST: %u", 42));

	printf(" | size: %i\n", ft_printf("hexa_TEST: %x", 42));
	printf(" | size: %i\n", printf("hexa_TEST: %x", 42));

	printf(" | size: %i\n", ft_printf("HEXA_TEST: %X", 42));
	printf(" | size: %i\n", printf("HEXA_TEST: %X", 42));

	printf(" | size: %i\n", ft_printf("PRCNT_TEST: %%"));
	printf(" | size: %i\n", printf("PRCNT_TEST: %%"));
}
*/
