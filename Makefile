### --- Linting --- ###
lint-zca:
	black ./zca --diff

format-zca:
	black ./zca


### --- Testing --- ###
test:
	docker-compose -f local.yml run --rm -e ZCA_ENVIRONMENT=testing zca pytest /tests/

debug-tests:
	test -s

coverage:
	test --cov=zca --cov-report term-missing


### --- ZCA --- ###
build-local:
	docker-compsoe -f local build 

run-local:
	docker-compose -f local.yml up

build-and-run-local:
	docker-compose -f local.yml up --build
