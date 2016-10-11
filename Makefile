test:
		py.test -s tests
.PHONY: test

build: clean
		python setup.py sdist bdist_wheel
.PHONY: build

clean:
		rm -rf dist build *.egg-info
.PHONY: clean

upload:
		make clean
		make build
		devpi upload dist/*
		pip uninstall saturn-es
.PHONY: upload
