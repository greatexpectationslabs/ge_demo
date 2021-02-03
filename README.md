# ge_demo repo - FOR INTERNAL USE ONLY, this is UNSUPPORTED for public use

A small demo using NYC taxi data. **Experimental, the GE core team uses this to test out things**. No guarantee that this actually works consistently. The full demo-able and maintained webinar material is in the superconductive/ge_tutorials repo.

**The postgres database** actually lives in the superconductive/ge_tutorials repo in the getting started tutorial. You can run the docker container with that PG database and add the creds to run the expectations and checkpoints configured here. Or just use the getting_started tutorial repo content itself. 

## Set up

1. Get credentials for the RDS instance.
2. Add these to your `great_expectations` configuration.
3. To run the pipeline, also set these two environment variables:
    ```bash
    PGPASSWORD=<SECRETS!>
    DEMO_USER=<SECRETS!>
    DEMO_HOST=<SECRETS!>
    ```
4. Verify your Great Expectations install with `great_expectations suite list`

## Run the "pipeline"

1. `psql -h $DEMO_HOST -d demo -U $DEMO_USER -f location_frequency.sql`
2. You should see output like
    ```sql
    DROP TABLE
    SELECT 10000
    DROP TABLE
    SELECT 28
    ```
