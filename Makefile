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

rpm: build
	mkdir -p scripts/rpm/build/tmp/saturn-es && \cp -f dist/*.tar.gz scripts/rpm/build/tmp/saturn-es
	cd scripts/rpm && mkdir -p rpms && python build_rpm.py
.PHONY: rpm
