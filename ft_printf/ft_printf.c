/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: elfemboc <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/23 15:06:14 by elfemboc          #+#    #+#             */
/*   Updated: 2026/04/23 15:08:19 by elfemboc         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "ft_printf.h"

void	print_spec(const char **fmt, va_list lst, int *size)
{
	if (++fmt == 'c')
		pf_putchar(va_arg(lst, int), 1);
	if (fmt == 's')
		pf_putstr(va_arg(lst, char *);
	if (fmt == 'p')
		pf_putptr(va_arg(lst, );
	if (fmt == 'd' || fmt == 'i')
		pf_putnbr();
	if (fmt == 'u')
		pf_putuint();
	if (fmt == 'x')
		pf_puthexa();
	if (fmt == 'X')
		pf_puthexa();
	if (fmt == '%')
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
			print_spec(&fmt, lst, &size);
		else
			print_fmt(&fmt, &size);
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
