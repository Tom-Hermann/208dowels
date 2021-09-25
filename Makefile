##
## EPITECH PROJECT, 2021
## B-MAT-400-RUN-4-1-208dowels-tom.hermann
## File description:
## Makefile
##

MAIN = src/main.py

MAIN_TEST = test/main.py

NAME = 208dowels

NAME_TEST = unit_test

all: $(NAME) test

$(NAME):
	cp $(MAIN) ./$(NAME)
	chmod +x $(NAME)

fclean:
	rm -f $(NAME)
	rm -f $(NAME_TEST)

test:
	cp $(MAIN_TEST) ./$(NAME_TEST)
	chmod +x $(NAME_TEST)

re: fclean all

.PHONY: test all fclean re