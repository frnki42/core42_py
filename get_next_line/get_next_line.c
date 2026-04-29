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
char	*get_next_line(int fd)
{
	char	buf[BUFFER_SIZE];

	if (read(fd, buf, BUFFER_SIZE) == -1)
		return (NULL);
	printf("%s", buf);
}

#include <fcntl.h>
int	main(int argc, char **argv)
{
	int	fd;

	if (argc < 2)
		return (write(1, "NAH BRO\n", 8));
	fd = open(argv[1], O_RDONLY);
	if (fd == -1)
		return (write(1, "invalid file\n", 13), 1);
	get_next_line(fd);
	close(fd);
	return (0);
}
