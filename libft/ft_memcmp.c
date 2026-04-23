/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: elfemboc <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/23 15:02:29 by elfemboc          #+#    #+#             */
/*   Updated: 2026/04/23 15:07:09 by elfemboc         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

int	ft_memcmp(const void *s1, const void *s2, size_t n)
{
	size_t	i;

	i = 0;
	while (i < n && ((unsigned char *)s1)[i] == ((unsigned char *)s2)[i])
		i++;
	if (i == n)
		return (0);
	return (((unsigned char *)s1)[i] - ((unsigned char *)s2)[i]);
}
/*
#include <stdio.h>
#include <string.h>
int	main(void)
{
	const void	*s1 = "FOURTYtwo";
	char		*s2 = "FOURTYTWO";

	printf("s1 is: %s\n", (char *)s1);
	printf("s2 is: %s\n", s2);
	printf("42_memcmp result: %i\n", ft_memcmp(s1, s2, 6));
	printf("OG_memcmp result: %i\n", memcmp(s1, s2, 6));
}
*/
