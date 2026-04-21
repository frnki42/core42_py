#include "libft.h"

size_t	ft_strlcat(char *dst, const char *src, size_t size)
{
	size_t	i;
	size_t	len;

	len = ft_strlen(dst);
	if (len >= size)
		return (ft_strlen(src) + size);
	i = -1;
	while (src[++i] && len + i < size - 1)
		dst[len + i] = src[i];
	dst[len + i] = '\0';
	return (ft_strlen(src) + len);
}
