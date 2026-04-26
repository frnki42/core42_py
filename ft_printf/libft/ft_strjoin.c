/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: elfemboc <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/23 15:04:09 by elfemboc          #+#    #+#             */
/*   Updated: 2026/04/23 15:04:11 by elfemboc         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

char	*ft_strjoin(char const *s1, char const *s2)
{
	char	*str;
	size_t	len_s1;
	size_t	len_s2;

	if (!s1 || !s2)
		return (NULL);
	len_s1 = ft_strlen(s1);
	len_s2 = ft_strlen(s2);
	str = malloc(len_s1 + len_s2 + 1);
	if (!str)
		return (NULL);
	ft_memmove(str, s1, len_s1);
	ft_memmove(&str[len_s1], s2, len_s2 + 1);
	return (str);
}
/*
#include <stdio.h>
int	main()
{
	char	*s1 = "yo wsg? this ";
	char	*s2 = "is a test. 42";
	char	*free_me;

	free_me = ft_strjoin(s1, s2);
	printf("%s\n", free_me);
}
*/
