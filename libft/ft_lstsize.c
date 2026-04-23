/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstsize.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: elfemboc <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/23 15:02:06 by elfemboc          #+#    #+#             */
/*   Updated: 2026/04/23 15:02:08 by elfemboc         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

int	ft_lstsize(t_list *lst)
{
	int	size;

	size = 0;
	while (lst)
	{
		size++;
		lst = lst->next;
	}
	return (size);
}
/*
#include <stdio.h>
int	main()
{
	t_list	*tmp;
	t_list	*nde1;
	t_list	*nde2;
	t_list	*nde3;

	nde1 = ft_lstnew("if i'm not mistaken");
	nde2 = ft_lstnew("list of size 3");
	nde3 = ft_lstnew("this should be a linked");
	ft_lstadd_front(&nde1, nde2);
	ft_lstadd_front(&nde1, nde3);
	printf("size: %i\n", ft_lstsize(nde1));
	while (nde1)
	{
		printf("%s\n", (char *)nde1->content);
		tmp = nde1;
		nde1 = nde1->next;
		free(tmp);
	}
}
*/
