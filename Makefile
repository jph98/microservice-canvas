# Project Makefile

.DEFAULT_GOAL := generate

generate:
	./generate.py

start:
	(cd output && python -m SimpleHTTPServer)
