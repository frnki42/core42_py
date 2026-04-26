/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: elfemboc <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/23 15:05:48 by elfemboc          #+#    #+#             */
/*   Updated: 2026/04/23 15:05:51 by elfemboc         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	char	*dst;
	size_t	size;

	size = ft_strlen(s);
	if (start >= size)
		return (ft_strdup(""));
	if (len > size - start)
		len = size - start;
	dst = malloc(len + 1);
	if (!dst)
		return (NULL);
	ft_memcpy(dst, &s[start], len);
	dst[len] = '\0';
	return (dst);
}
/*	
#include <stdio.h>
int	main()
{
	char			*s = "yo what's up? let's test this rq!";
	size_t			len = ft_strlen(s);
	unsigned int	start = 3;
	char			*free_me = ft_substr(s, start, len);

	printf("%s\n", free_me);
	free(free_me);
}
*/
