/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstmap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: elfemboc <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/23 15:01:50 by elfemboc          #+#    #+#             */
/*   Updated: 2026/04/23 15:01:53 by elfemboc         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

t_list	*ft_lstmap(t_list *lst, void *(*f)(void *), void (*del)(void *))
{
	t_list	*nde;
	t_list	*new;
	void	*cnt;

	if (!lst || !f || !del)
		return (NULL);
	new = NULL;
	while (lst)
	{
		cnt = f(lst->content);
		nde = ft_lstnew(cnt);
		if (!nde)
			return (del(cnt), ft_lstclear(&new, del), NULL);
		ft_lstadd_back(&new, nde);
		lst = lst->next;
	}
	return (new);
}
/*
#include <stdio.h>
void	del(void *content)
{
	free(content);
}

void	*make_zero(void *content)
{
	(void)content;
	return (ft_strdup("0"));
}

int	main()
{

	t_list	*tmp;
	t_list	*lst;
	t_list	*new;

	lst = ft_lstnew("1");
	ft_lstadd_back(&lst, ft_lstnew("2"));
	ft_lstadd_back(&lst, ft_lstnew("3"));
	new = ft_lstmap(lst, make_zero, del);
	while (new)
	{
		printf("%s\n", (char *)new->content);
		tmp = new;
		new = new->next;
		del(tmp->content);
		free(tmp);
	}
	while (lst)
	{
		tmp = lst;
		lst = lst->next;
		free(tmp);
	}
}
*/
