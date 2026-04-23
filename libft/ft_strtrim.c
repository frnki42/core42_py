/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strtrim.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: elfemboc <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/23 15:05:39 by elfemboc          #+#    #+#             */
/*   Updated: 2026/04/23 15:05:42 by elfemboc         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

char	*ft_strtrim(char const *s1, char const *set)
{
	size_t	start;
	size_t	end;

	if (!s1 || !set)
		return (NULL);
	start = 0;
	while (s1[start] && ft_strchr(set, s1[start]))
		start++;
	end = ft_strlen(s1);
	while (end > start && ft_strchr(set, s1[end - 1]))
		end--;
	return (ft_substr(s1, start, end - start));
}

/*
#include <stdio.h>
int	main()
{
	char	*free_me;

	free_me = ft_strtrim("4242tester4242", "42");
	printf("%s\n", free_me);
	free(free_me);

	free_me = ft_strtrim("tester", "42");
	printf("%s\n", free_me);
	free(free_me);

	free_me = ft_strtrim("42424242", "42");
	printf("%s\n", free_me);
	free(free_me);

	free_me = ft_strtrim("", "42");
	printf("%s\n", free_me);
	free(free_me);

	free_me = ft_strtrim("42424242", "");
	printf("%s\n", free_me);
	free(free_me);
	
	free_me = ft_strtrim("4242tester", "42");
	printf("%s\n", free_me);
	free(free_me);

	free_me = ft_strtrim("tester4242", "42");
	printf("%s\n", free_me);
	free(free_me);
}
*/
