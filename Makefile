newday:
	python3.9 2022/new_day.py $(day_no) $(name)

freeze:
	@echo "Freezing requirements..."
	pip freeze > requirements.txt
	@echo "Done!"
	@cat requirements.txt