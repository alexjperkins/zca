### ZCA: The Data Preprocessing Application

## What?

A preprocessing application to clean and pre-process data. It intends to sit inbetween sources and pipelines
in order to produce useability data

## How?

Using Event Driven Architecture it will subscribe to an Event Store (Kafka - Streaming Service) to retrieve events (and commands).
These events will contain all necessary data for the given domain and will be definied at author time.
These events will be what drive the the application, and will be JSON format externally and Dataclasses internally.
The ultimate goal is to only publish data that is certified to be "clean" to a given partition on the Event Store, and provide
a RPC based API and dashboards for clients to interact with.

There will options to interact with the API to publish manually or provide some subscription tool instead.


### Developer Guide

The app is containized and uses `docker-compose` in order to maintain the running and data management of the application.
So developers will need `docker` and `docker-compose` to run the application locally and any tests

Postgres will be used for local storage.

Kafka will is used as an external messagebus. This is where all `important` events & commands will live and will allow outside sources to
publish to this stream 

An API is exposed using the flask framework - however it's TBD whether this will be a GraphQL Server or REST/RPC. This will also handle any authentication to both the dashboard and all exposed endpoints. The authentication backend is to be determined

Furthermore, a dashboard will also be exposed to show clean & dirty data and the difference between the two. This will be built using React and
Typescript.

To test the system as a whole, a BDD Behave framework is planned; this will also serve the purpose of faking data population to the Event Store

## Branching

```
	<function>/<ticket-number>/<description>	

	eg

	feat/ZCA-001/refactor-unit-of-work-abstraction
```

Possible functions: `feat`, `fix`, `hotfix`

## PRs

Acceptance:
	- All tests must pass
	- Must be linted
	- At least one accepted Review

## Merge Strategy:

Squash merges ONLY


## Setup
```
	# Debian based (incl Ubuntu)
	sudo apt-get install docker docker-compose
```


## Tests
```
	$ make test
```
