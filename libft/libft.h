#ifndef LIBFT_H
# define LIBFT_H
# include <stddef.h>
# include <stdlib.h>
# include <stdint.h>

size_t	ft_strlen(const char *str);
int	ft_strncmp(const char *s1, const char *s2, size_t n);
void	*ft_memset(void *s, int c, size_t n);
void	*ft_memcpy(void *dest, const void *src, size_t n);
int	ft_isalpha(char c);
int	ft_isdigit(char c);
char	*ft_strdup(const char *s);
void	*ft_memmove(void *dest, const void *src, size_t n);

#endif
