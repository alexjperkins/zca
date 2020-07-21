### --- Linting --- ###
lint-zca:
	. ./venv/bin/activate && black ./zca --diff

format-zca:
	. ./venv/bin/activate && black ./zca


### --- Testing --- ###
test:
	docker-compose -f local.yml run --rm -e ZCA_ENVIRONMENT=testing zca pytest /tests/

debug-tests:
	test -s

coverage:
	test --cov=zca --cov-report term-missing


### --- ZCA --- ###
run-zk:
	docker-compose -f local.yml up zookeeper 


build-local:
	docker-compose -f local.yml build 

run-local:
	docker-compose -f local.yml up

build-and-run-local:
	docker-compose -f local.yml up --build
