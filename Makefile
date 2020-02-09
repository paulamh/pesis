build:
	pip install -r requirements
test: build
	coverage run -m pytest
	codecov --token "c77e6355-3723-4f32-9c50-f3c2b13e11d1"
release: test
	pip install --upgrage setuptools, twine
	python setup.py sdist
	twine upload dist/*
clean:
	rm -rf dist
