# Great Expectations 101: Getting started

This repo contains materials for a simple demo of Great Expectations with data and an expectation suite. It was created by Sam Bail at Superconductive in July 2020. 

**Note**: This setup will soon be replaced by a Docker container that has all the relevant


## The `data` directory

### About the NYC taxi data

The CSV files in the data directory are yellow taxi trip data that have been downloaded from the NYC taxi data website:
* Data: https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page
* Data dictionary: https://www1.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf

We created 10,000 row samples (using the pandas sample function) from original CSV files for convenience and manually added some breaking changes (0s in the passenger_count column) to demonstrate potential data issues. 

In a future version of this tutorial, we might use "naturally occurring" data bugs :)

### About the load script
The SQL load script is a simple script to load the provided data tables to a postgres database. They're provided for convenience, you can also use a different backend and your own method to make the data available for this demo.

### About the analysis
This is a very simple Jupyter notebook that creates histograms of the passenger count variable in the data. We created this for the purpose of this demo.


## The `great_expectations` directory
Currently, this demo contains the following:
* A single expectation suite, taxi.demo, containing a handful of simple expectations
    * The expectation suite will pass when run against the January data, and fail when run against the February data in the staging table (due to the messy data we introduced)
* A checkpoint taxi.demo.staging.chk that is set up to run the suite against the staging table

### Setting up `my_postgres_db`

In order to access the data, we need to add the credentials to the DB where we loaded the data into `great_expectations/uncommitted/config_variables.yml`:

```
my_postgres_db:
  drivername: postgresql
  host: ...
  port: '5432'
  username: ...
  password: ...
  database: ...
```

## The `slides` directory
We check in the generated HTML for these slides, so the HTML in the repo should be up-to-date. If you want to make changes to the slides and recompile them, follow the instructions below.

### Installing Marp
* Install npm: https://www.npmjs.com/get-npm
* Allow global install of npm modules: `sudo mkdir /usr/local/lib/node_modules; chown -R `whoami` /usr/local/lib/node_modules` 
* Install marp CLI: `npm install -g @marp-team/marp-cli`
* This seems to be the most helpful documentation: https://marpit.marp.app/

### Compiling markdown to HTML
* Compile markdowns: `marp *.md --theme theme.css` then open the HTML output in a browser window. Each change requires re-compiling and refreshing the browser. The `theme` flag is needed to compile with the custom CSS.
* You can also run these in "watch" mode which will keep a compile server running and refresh the browser window for both markdown and CSS changes (pretty cool): `marp *.md --theme theme.css --watch`
