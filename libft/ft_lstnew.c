#include "libft.h"

t_list	*ft_lstnew(void *content)
{
	t_list	*node;

	node = malloc(sizeof(t_list));
	if (!node)
		return (NULL);
	node->content = content;
	node->next = NULL;
	return (node);
}
/*
#include <stdio.h>
int	main()
{
	t_list	*nde;

	nde = ft_lstnew("test42");
	if (nde)
		printf("content: %s, next: %p\n", (char *)nde->content, nde->next);
	free(nde);
}
*/
