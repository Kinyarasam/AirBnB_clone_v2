#!/usr/bin/env bash
set -e

cd "$(dirname "$(readlink -f "$BASH_SOURCE")")/.."

# see also ".mailmap" fo how email addesses and names are deduplicated

{
	cat <<- 'EOH'
		# These individuals contributed to the hbnb project in this repository

		Ezra Nobrega <ezra.nobrega@outlook.com>
		Justin Majetich <justinmajetich@gmail.com>
	EOH
	git log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf
} > AUTH
