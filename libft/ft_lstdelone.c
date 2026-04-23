/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstdelone.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: elfemboc <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/23 15:01:10 by elfemboc          #+#    #+#             */
/*   Updated: 2026/04/23 15:01:12 by elfemboc         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

void	ft_lstdelone(t_list *lst, void (*del)(void *))
{
	if (!lst || !del)
		return ;
	del(lst->content);
	free(lst);
}
/*
#include <stdio.h>
void	del(void *content)
{
	free(content);
}

int	main()
{
	char	*str;
	t_list	*nde;

	str = malloc(7);
	if (!str)
		return (printf("malloc failed\n"), 1);
	ft_memcpy(str, "test42", 7);
	nde = ft_lstnew(str);
	if (!nde)
		return (printf("ft_lstnew() failed\n"), 1);
	printf("nde->content before ft_lstdelone() = %s\n", (char *)nde->content);
	ft_lstdelone(nde, del);
	printf("ft_lstdelone completed\n");
	return (0);
}
*/
