# ge_demo

Simple demo of Great Expectations with data + an expectation suite

## The data

The CSV files in the data directory have been downloaded from the NYC taxi data website:
* Data: https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page
* Data dictionary: https://www1.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf

We created 10,000 row samples from those files for convenience and loaded them to a Postgres database to access them in this demo.

## Slides instructions
We check in the generated HTML for these slides, so the HTML in the repo should be up-to-date. If you want to make changes to the slides and recompile them, follow the instructions below.

### Installing Marp
* Install npm: https://www.npmjs.com/get-npm
* Allow global install of npm modules: `sudo mkdir /usr/local/lib/node_modules; chown -R `whoami` /usr/local/lib/node_modules` 
* Install marp CLI: `npm install -g @marp-team/marp-cli`
* This seems to be the most helpful documentation: https://marpit.marp.app/

### Compiling markdown to HTML
* Compile markdowns: `marp *.md --theme theme.css` then open the HTML output in a browser window. Each change requires re-compiling and refreshing the browser. The `theme` flag is needed to compile with the custom CSS.
* You can also run these in "watch" mode which will keep a compile server running and refresh the browser window for both markdown and CSS changes (pretty cool): `marp *.md --theme theme.css --watch`
