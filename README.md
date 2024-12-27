# mass-data-import
Simple tool to import CSV formatted data into a Postgres database

## To run the program

1. Install the environment, based on the `environment.yml` file, using the command ```conda env create -f environment.yml``` 
2. Activate the environment with `conda activate mass-import`
3. Run the program with `python main.py -f dummy_data.csv`

## SQLite

This example is run with SQLite, and the database and table used is provided in the code. Since this is an example, the code uses the only table available `people` (same name as DB). In case you want to try the code using a different table, you need to change the `base_query` variable in the `main.py` file. Also change the `executemany` statement to accomodate for more or less columns accordingly.
