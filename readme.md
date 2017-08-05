# Book reader suitable for fast reading

Converts PDF to HTML with pdf2htmlEX and serves them per page.

## Convert
pdf file `algo.pdf`

`docker-compose run conv`

## Serve
`docker-compose up -d prod`

Then visit `localhost:5000/1` for the first page.