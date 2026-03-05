VENV=.venv
PYTHON=$(VENV)/bin/python

.PHONY: venv install check clean

venv:
	python3 -m venv $(VENV)

install:
	@if [ ! -f requirements.txt ]; then \
		echo "❌ Falta requirements.txt"; \
		exit 1; \
	fi
	$(PYTHON) -m pip install -r requirements.txt

check:
	PYTHON=$(PYTHON) ./scripts/check_estructura.sh

clean:
	rm -f scripts/estado_editorial_raw.txt
