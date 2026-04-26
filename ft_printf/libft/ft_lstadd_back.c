/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstadd_back.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: elfemboc <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/23 15:00:23 by elfemboc          #+#    #+#             */
/*   Updated: 2026/04/23 15:00:27 by elfemboc         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

void	ft_lstadd_back(t_list **lst, t_list *new)
{
	t_list	*tmp;

	if (!lst || !new)
		return ;
	if (!*lst)
	{
		*lst = new;
		return ;
	}
	tmp = *lst;
	while (tmp->next)
		tmp = tmp->next;
	tmp->next = new;
}
/*
#include <stdio.h>
int	main()
{
	t_list	*nde1 = ft_lstnew("nde1");
	t_list	*nde2 = ft_lstnew("nde2");

	ft_lstadd_back(&nde1, nde2);
	printf("%i\n", ft_lstsize(nde1));
	free(nde1);
	free(nde2);
}
*/
