### Makefile for sigalgo ###


### --- Linting --- ###
lint-zca:
	black ./zca --diff

format-zca:
	black ./zca


### --- Testing --- ###
test:
	docker-compose -f local.yml run --rm -e ZCA_ENVIRONMENT=testing zca pytest /tests/
