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

static int	no_newline(char *buf)
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

static char	*trim_buf(char *buf)
{
	size_t	i;
	size_t	len_trm;
	char	*trm;

	i = 0;
	while (buf[i] != '\n' && buf[i])
		i++;
	if (buf[i] == '\0')
		return (free(buf), NULL);
	len_trm = ft_strlen(&buf[++i]);
	if (!len_trm)
		return (free(buf), NULL);
	trm = malloc(len_trm + 1);
	if (!trm)
		return (free(buf), NULL);
	gnl_memmove(trm, &buf[i], len_trm);
	trm[len_trm] = '\0';
	return (free(buf), trm);
}

static char	*set_gnl(char *buf)
{
	size_t	i;
	size_t	k;
	char	*gnl;

	i = 0;
	while (buf[i] != '\n' && buf[i])
		i++;
	if (buf[i] == '\n')
		i++;
	gnl = malloc(i + 1);
	if (!gnl)
		return (NULL);
	k = -1;
	while (++k < i)
		gnl[k] = buf[k];
	gnl[k] = '\0';
	return (gnl);
}

static char	*set_buf(char *buf, int fd)
{
	ssize_t	size;
	char	dst[BUFFER_SIZE + 1];

	size = 1;
	while (no_newline(buf) && size)
	{
		size = read(fd, dst, BUFFER_SIZE);
		if (size == -1)
			return (free(buf), NULL);
		dst[size] = '\0';
		buf = gnl_strjoin(buf, dst);
		if (!buf)
			return (NULL);
		if (!buf[0])
			return (free(buf), NULL);
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
	gnl = set_gnl(buf);
	if (!gnl)
		return (free(buf), NULL);
	buf = trim_buf(buf);
	return (gnl);
}
/*
#include <stdio.h>
#include <fcntl.h>
int	main(int argc, char **argv)
{
	int		fd;
	char	*gnl;

	if (argc < 2)
		return (write(1, "NAH BRO\n", 8));
	fd = open(argv[1], O_RDONLY);
	if (fd == -1)
		return (write(1, "invalid file\n", 13), 1);
	while (42)
	{
		gnl = get_next_line(fd);
		if (!gnl)
			break ;
		printf("%s", gnl);
		free(gnl);
	}
	close(fd);
	return (0);
}
*/
