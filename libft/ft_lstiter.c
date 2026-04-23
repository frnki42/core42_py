/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_lstiter.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: elfemboc <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/23 15:01:21 by elfemboc          #+#    #+#             */
/*   Updated: 2026/04/23 15:06:32 by elfemboc         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

void	ft_lstiter(t_list *lst, void (*f)(void *))
{
	if (!lst || !f)
		return ;
	while (lst)
	{
		f(lst->content);
		lst = lst->next;
	}
}
/*
#include <stdio.h>
void	print_content(void *content)
{
	printf("%s\n", (char *)content);
}

int	main()
{
	t_list	*tmp;
	t_list	*lst = ft_lstnew("1");

	ft_lstadd_back(&lst, ft_lstnew("2"));
	ft_lstadd_back(&lst, ft_lstnew("3"));
	ft_lstiter(lst, print_content);
	while (lst)
	{
		tmp = lst;
		lst = lst->next;
		free(tmp);
	}
}
*/
