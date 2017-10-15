# Book/Article Reader suitable for Fast Reading

Converts PDF to HTML with pdf2htmlEX and serves them as webpage per page, then i.e. Reedy may be used for fast reading.

## Convert
pdf file `algo.pdf`

`docker-compose run conv`

## Serve
`docker-compose up -d prod`

## Dev
`docker-compose up dev`

Then visit `localhost:5000/1` for the first page.
