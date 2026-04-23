/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: elfemboc <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/23 15:04:18 by elfemboc          #+#    #+#             */
/*   Updated: 2026/04/23 15:04:21 by elfemboc         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

size_t	ft_strlcat(char *dst, const char *src, size_t size)
{
	size_t	i;
	size_t	len;

	len = ft_strlen(dst);
	if (len >= size)
		return (ft_strlen(src) + size);
	i = -1;
	while (src[++i] && len + i < size - 1)
		dst[len + i] = src[i];
	dst[len + i] = '\0';
	return (ft_strlen(src) + len);
}
