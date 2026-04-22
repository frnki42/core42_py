char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	char	*dst;
	size_t	

	dst = malloc(len + 1);
	if (!dst)
		return (NULL);
	ft_memcpy(dst, &s[start], len);
	dst[len] = '\0';
	return (dst);
}
