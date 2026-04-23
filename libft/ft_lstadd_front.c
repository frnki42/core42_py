/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_front.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: elfemboc <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/23 15:00:35 by elfemboc          #+#    #+#             */
/*   Updated: 2026/04/23 15:00:37 by elfemboc         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

void	ft_lstadd_front(t_list **lst, t_list *new)
{
	if (!lst || !new)
		return ;
	new->next = *lst;
	*lst = new;
}
/*
#include <stdio.h>
int	main()
{
	t_list	*tmp;
	t_list	*nde1 = ft_lstnew("into a linked list?");
	t_list	*nde2 = ft_lstnew("does this turn");

	ft_lstadd_front(&nde1, nde2);
	while (nde1)
	{
		printf("%s\n", (char *)nde1->content);
		tmp = nde1;
		nde1 = nde1->next;
		free(tmp);
	}
}
*/
