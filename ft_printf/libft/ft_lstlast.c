/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstlast.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: elfemboc <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/23 15:01:32 by elfemboc          #+#    #+#             */
/*   Updated: 2026/04/23 15:01:34 by elfemboc         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

t_list	*ft_lstlast(t_list *lst)
{
	if (!lst)
		return (NULL);
	while (lst->next)
		lst = lst->next;
	return (lst);
}
/*
#include <stdio.h>
int	main()
{
	t_list	*nde1 = ft_lstnew("i come from nde1");
	t_list	*nde2 = ft_lstnew("i come from nde2");
	t_list	*nde3 = ft_lstnew("i come from nde3");
	t_list	*nde4 = ft_lstnew("i come from nde4");
	t_list	*nde5 = ft_lstnew("i come from nde5");
	t_list	*nde6 = ft_lstnew("i come from nde6");
	t_list	*tmp;

	ft_lstadd_front(&nde1, nde2);
	ft_lstadd_front(&nde1, nde3);
	ft_lstadd_front(&nde1, nde4);
	ft_lstadd_front(&nde1, nde5);
	ft_lstadd_front(&nde1, nde6);
	
	tmp = ft_lstlast(nde1);
	printf("%s\n", (char *)tmp->content);
	while (nde1)
	{
		printf("%s\n", (char *)nde1->content);
		tmp = nde1;
		nde1 = nde1->next;
		free(tmp);
	}
}
*/
