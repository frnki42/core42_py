/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: .frnki <frnki@42.fr>                       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/20 04:20:42 by .frnki            #+#    #+#             */
/*   Updated: 2026/04/20 16:20:42 by .frnki           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "get_next_line.h"

size_t	ft_strlen(const char *str)
{
	size_t	len;

	len = 0;
	while (str[len])
		len++;
	return (len);
}

void	*gnl_memmove(void *dest, const void *src, size_t n)
{
	unsigned char		*d;
	const unsigned char	*s;

	if (!dest || !src)
		return (NULL);
	d = dest;
	s = src;
	if (d > s)
		while (n--)
			d[n] = s[n];
	else
		while (n--)
			*d++ = *s++;
	return (dest);
}

char	*gnl_strjoin(char *buf, char *dst)
{
	char	*str;
	size_t	len_buf;
	size_t	len_dst;

	if (!dst)
		return (free(buf), NULL);
	len_buf = 0;
	if (buf)
		len_buf = ft_strlen(buf);
	len_dst = ft_strlen(dst);
	str = malloc(len_buf + len_dst + 1);
	if (!str)
		return (free(buf), NULL);
	if (buf)
		gnl_memmove(str, buf, len_buf);
	gnl_memmove(&str[len_buf], dst, len_dst + 1);
	free(buf);
	return (str);
}
