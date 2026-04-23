/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: elfemboc <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/23 15:05:23 by elfemboc          #+#    #+#             */
/*   Updated: 2026/04/23 15:05:25 by elfemboc         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

char	*ft_strnstr(const char *s1, const char *s2, size_t n)
{
	size_t	i;
	size_t	len;

	if (!*s2)
		return ((char *)s1);
	len = ft_strlen(s2);
	i = -1;
	while (s1[++i] && i + len <= n)
		if (!ft_strncmp(&s1[i], s2, len))
			return ((char *)&s1[i]);
	return (NULL);
}
/*
#include <stdio.h>
int	main()
{
	const char	*s1 = "yo wsg? this is a test for 42";
	const char	*s2 = "this";
	int			n = 4;
	char		*test;

	test = ft_strnstr(s1, s2, n);
	if (test)
		printf("%s\n", test);
	else
		printf("\"%s\" was not found inside \"%s\" for %i chars\n", s2, s1, n);
}
*/
