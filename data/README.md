# DATA
The raw data comes from **PUMS**:
http://www.census.gov/programs-surveys/acs/technical-documentation/pums.html

## Data format 
Raw data: `ss15pusa.csv`, `ss15pusa.csv`. 
Generated samples: `sample*.csv`

## Usage

`gen_data.sh` selects the columns we need for this task.
`gen_sample.sh` selects the migrants (10k at a time).

	bash gen_data.sh
	bash gen_sample.sh

`awk` is required to run this code.

## Notice
Only the preprocessing scripts and samples were preserved in this directory because of the limitation of repository size.