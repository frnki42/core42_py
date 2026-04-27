/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   pf_putstr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: .frnki <marvin@42.fr>                      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/20 04:20:42 by .frnki            #+#    #+#             */
/*   Updated: 2026/04/20 16:20:42 by .frnki           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "ft_printf.h"

int	pf_putstr(char *str)
{
	if (!str)
		return (write(1, "(null)", 6));
	return (write(1, str, ft_strlen(str)));
}
/*
#include <stdio.h>
int	main()
{
	printf(" returns size: %i\n", pf_putstr("42test"));
	printf(" returns size: %i\n", printf("%s", "42test"));
	printf(" returns size: %i\n", pf_putstr(""));
	printf(" returns size: %i\n", printf("%s", ""));
	printf(" returns size: %i\n", pf_putstr(NULL));
	printf(" returns size: %i\n", printf("%s", NULL));
}
*/
