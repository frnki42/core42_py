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

int	no_newline(char **buf)
{
	printf("no_newline got executed\n");
	return (1);
}

char	*set_buf(char **buf, int fd)
{
	ssize_t	size;

	*buf = malloc(BUFFER_SIZE + 1);
	if (!*buf)
		return (NULL);
	size = 42;
	while (size > 0 && no_newline(buf))
	{
		size = read(fd, *buf, BUFFER_SIZE);
		if (size == -1)
			return (free(*buf), *buf = NULL, NULL);
		printf("%s\n", *buf);
		if (size == 0)
			printf("size = 0");
	}
	(*buf)[size] = '\0';
	return (*buf);
}

char	*get_next_line(int fd)
{
	static char	*buf;
	char		*gnl;

	if (fd < 0 || BUFFER_SIZE < 1)
		return (NULL);
	buf = set_buf(&buf, fd);
	if (!buf)
		return (NULL);
	return (buf);
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
