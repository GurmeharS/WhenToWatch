# WhenToWatch
A scraper and analyzer that tells you when to tune into NBA games.


## Get Started:
- To install all required dependencies:
`pip install -r requirements.txt` or `pip3 install -r requirements.txt`.
- To run a demo version locally:
`python3 scrape.py`.

## Threshold Definitions:
If you want to add your own thresholds/stats to look out for, you can add threshold definitions in `thresholds.py`.

Each dictionary in the definitions list consists of:
- comparisons (required) - A list of dicts consisting of: 
  - scope: `<scope of the comparison>`
  - stat: `<statistic to be compared>` 
  - operator: `<comparison operator>` 
  - value: `<threshold value>`
  - I.e. 
         
         {
             scope: <player|team|game>,

             stat: <quarter|time_left|point_differential|points|fg_percentage|three_pt_percentage|assists|rebounds|made_threes>, 

             operator: <gt|ge|eq|le|lt|ne>, 

             value: <integer|float>
         }
- description - A verbal description/summary of the threshold
