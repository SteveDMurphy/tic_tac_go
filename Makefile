.PHONY: tictac
.DEFAULT_GOAL := tictac-help

tictac-help:
	@echo Some help should go here on how to use the app

init-db:
	@echo Initializing the postgres db
	@docker-compose down -v
	@docker-compose build --no-cache tictac_db
	@docker-compose up -d tictac_db
	@docker exec composed_tictac_db sleep 5
	@docker-compose run tictac_server flask db upgrade

tictac:
	@echo Let\'s play tic-tac-toe!
	@docker-compose down
	@docker-compose up -d tictac_db
	@docker exec composed_tictac_db sleep 5
	@docker-compose up tictac_server
# @docker-compose up -d tictac_server
# @docker exec -ti composed_tictac_server /bin/bash