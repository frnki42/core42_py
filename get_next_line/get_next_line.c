/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: .frnki <frnki@42.fr>                       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/04/20 04:20:42 by .frnki            #+#    #+#             */
/*   Updated: 2026/04/20 16:20:42 by .frnki           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "get_next_line.h"
#include <stdio.h>					//remove me
#include <fcntl.h>					//remove me

size_t	ft_strlen(const char *str)
{
	int	len;

	len = 0;
	while (str[len])
		len++;
	return (len);
}

void	*ft_memmove(void *dest, const void *src, size_t n)
{
	unsigned char		*d;
	const unsigned char	*s;

	if (!dest && !src)
		return (NULL);
	d = dest;
	s = src;
	if (d > s)
		while (n--)
			d[n] = s[n];
	else
		while (n--)
			*d++ = *s++;
	return (dest);
}

char	*gnl_strjoin(char const *s1, char const *s2)
{
	char	*str;
	size_t	len_s1;
	size_t	len_s2;

	if (!s1 || !s2)
		return (NULL);
	len_s1 = ft_strlen(s1);
	len_s2 = ft_strlen(s2);
	str = malloc(len_s1 + len_s2 + 1);
	if (!str)
		return (NULL);
	ft_memmove(str, s1, len_s1);
	ft_memmove(&str[len_s1], s2, len_s2 + 1);
	return (str);
}

int	no_newline(char *buf)
{
	int	i;

	if (!buf)
		return (1);
	i = -1;
	while (buf[++i])
		if (buf[i] == '\n')
			return (0);
	return (1);
}

char	*set_buf(char *buf, int fd)
{
	ssize_t	size;
	char	src[BUFFER_SIZE + 1];

	size = 1;
	while (no_newline(buf) && size > 0 )
	{
		size = read(fd, src, BUFFER_SIZE);
		if (size == -1)
			return (free(buf), buf = NULL, NULL);
		src[size] = '\0';
		buf = gnl_strjoin(buf, src);
		if (!buf)
			return (NULL);
	}
	return (buf);
}

char	*get_next_line(int fd)
{
	static char	*buf;
	char		*gnl;

	if (fd < 0 || BUFFER_SIZE < 1)
		return (NULL);
	buf = set_buf(buf, fd);
	if (!buf)
		return (NULL);
	return (gnl);
}

int	main(int argc, char **argv)
{
	int		fd;
	char	*gnl;

	if (argc < 2)
		return (write(1, "NAH BRO\n", 8));
	fd = open(argv[1], O_RDONLY);
	if (fd == -1)
		return (write(1, "invalid file\n", 13), 1);
	gnl = get_next_line(fd);
	printf("%s\n",gnl);
	free(gnl);
	close(fd);
	return (0);
}
