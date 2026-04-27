/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: .frnki <frnki@42.fr>                       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/26 04:20:42 by .frnki            #+#    #+#             */
/*   Updated: 2026/04/26 16:20:42 by .frnki           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#ifndef FT_PRINTF_H
# define FT_PRINTF_H
# include "libft/libft.h"
# include <stdarg.h>

int	ft_printf(const char *fmt, ...);
int	pf_putchar(int c);
int	pf_putinvalid(const char c);
int	pf_putnbr(long long nbr, int size, int base, int upper);
int	pf_putptr(void *p);
int	pf_putstr(char *str);

#endif
