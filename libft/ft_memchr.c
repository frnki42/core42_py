/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: elfemboc <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/23 15:02:18 by elfemboc          #+#    #+#             */
/*   Updated: 2026/04/23 15:06:52 by elfemboc         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

void	*ft_memchr(const void *s, int c, size_t n)
{
	unsigned char	*ptr;

	ptr = (unsigned char *)s;
	while (n--)
	{
		if (*ptr == (unsigned char)c)
			return (ptr);
		ptr++;
	}
	return (NULL);
}
/*
#include <stdio.h>
int main()
{
	char *test = "42Vienna";
	void *mem_adr;
	
	mem_adr = ft_memchr(test, 'X', 42);
	if (mem_adr)
		printf("match found at %p\n", mem_adr);
	else
		printf("no match found in %s\n", test);
}
*/
