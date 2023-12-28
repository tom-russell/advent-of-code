freeze:
	@echo "Freezing requirements..."
	pip freeze > requirements.txt
	@echo "Done!"
	@cat requirements.txt