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

int	print_spec(const char **fmt, va_list lst)
{
	(*fmt)++;
	if (**fmt == 'd' || **fmt == 'i')
		return (pf_putnbr(va_arg(lst, int), 0));
	else if (**fmt == 'c')
		return (pf_putchar(va_arg(lst, int)));
	else if (**fmt == 's')
		return (pf_putstr(va_arg(lst, char *)));
	else if (**fmt == 'p')
		return (pf_putptr(va_arg(lst, void *)));
	else if (**fmt == 'u')
		return (pf_putnbr(va_arg(lst, unsigned int), 0));
	else if (**fmt == 'x')
		return (pf_puthexa(va_arg(lst, unsigned int), 0));
	else if (**fmt == 'X')
		return (pf_puthexa(va_arg(lst, unsigned int), 1));
	else if (**fmt == '%')
		return (pf_putchar('%'));
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
#include <stdio.h>
int	main()
{
	char	str[] = "+test42_";
	ft_printf("char test: %c\n", 'c');
	ft_printf("str test: %s\n", str);
	ft_printf("ptr test: %c\n", str);
	ft_printf("dec test: %c\n", 'c');
	ft_printf("int test: %c\n", 'c');
	ft_printf("uint test: %c\n", 'c');
	ft_printf("hexa test: %c\n", 'c');
	ft_printf("HEXA test: %c\n", 'c');
	ft_printf("% test: %c\n", 'c');
	printf("va_list%% test: %c\n", 'c');
}
