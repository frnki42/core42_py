/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstclear.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: elfemboc <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/23 15:00:47 by elfemboc          #+#    #+#             */
/*   Updated: 2026/04/23 15:00:51 by elfemboc         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

void	ft_lstclear(t_list **lst, void (*del)(void *))
{
	t_list	*tmp;

	if (!lst || !del)
		return ;
	while (*lst)
	{
		tmp = *lst;
		del(tmp->content);
		*lst = tmp->next;
		free(tmp);
	}
}
/*
#include <stdio.h>
void	del(void *content)
{
	free(content);
}
int	main()
{
	t_list	*nde1 = ft_lstnew(ft_strdup("1"));
	t_list	*nde2 = ft_lstnew(ft_strdup("2"));
	t_list	*nde3 = ft_lstnew(ft_strdup("3"));
	t_list	*nde4 = ft_lstnew(ft_strdup("4"));

	ft_lstadd_back(&nde1, nde2);
	ft_lstadd_back(&nde1, nde3);
	ft_lstadd_back(&nde1, nde4);
	printf("list size before ft_lstclear: %i\n", ft_lstsize(nde1));
	ft_lstclear(&nde1, del);
	printf("list size after ft_lstclear: %i\n", ft_lstsize(nde1));
	printf("nde1 after ft_lstclear: %p\n", nde1);
}
*/
