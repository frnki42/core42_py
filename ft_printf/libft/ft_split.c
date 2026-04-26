/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: elfemboc <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/23 15:03:35 by elfemboc          #+#    #+#             */
/*   Updated: 2026/04/23 15:08:50 by elfemboc         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

static size_t	get_size(const char *s, char c)
{
	size_t	i;
	size_t	size;

	i = 0;
	size = 0;
	while (s[i] && s[i] == c)
		i++;
	while (s[i])
	{
		size++;
		while (s[i] && s[i] != c)
			i++;
		while (s[i] && s[i] == c)
			i++;
	}
	return (size);
}

static void	free_splt(char **splt, size_t pos)
{
	while (pos--)
		free(splt[pos]);
	free(splt);
}

static char	**set_splt(char **splt, const char *s, char c)
{
	size_t	i;
	size_t	len;
	size_t	pos;

	i = 0;
	pos = 0;
	while (s[i])
	{
		while (s[i] && s[i] == c)
			i++;
		len = 0;
		while (s[i + len] && s[i + len] != c)
			len++;
		if (len)
		{
			splt[pos] = ft_substr(s, i, len);
			if (!splt[pos])
				return (free_splt(splt, pos), NULL);
			pos++;
		}
		i += len;
	}
	splt[pos] = NULL;
	return (splt);
}

char	**ft_split(char const *s, char c)
{
	size_t	size;
	char	**splt;

	if (!s)
		return (NULL);
	size = get_size(s, c) + 1;
	splt = malloc(size * sizeof(char *));
	if (!splt || !set_splt(splt, s, c))
		return (NULL);
	return (splt);
}
/*
#include <stdio.h>
int	main()
{
	char	*s = "4this4should4be4the4tester4i4guess4";
	char	c = '4';
	int		i;
	char	**splt;

	splt = ft_split(s, c);
	i = -1;
	while (splt[++i])
	{
		printf("%s\n", splt[i]);
		free(splt[i]);
	}
	free(splt);
}
*/
