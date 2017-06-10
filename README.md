# oakland_home_price_model
A model of home values in my favorite neighborhoods in Oakland

Downloaded Redfin data for 7 elementary school districts in Oakland (Emerson, Piedmont, Rockridge, Crocker, Glenview, Chabot, Peralta), limited to a reasonable price range for single family houses (600k-1.5M) and within past 1.5 years.

Here are the result for the current model.  See model.py for complete variable definitions.  Dependent variable is price/sqft. Model includes:
* dummies per school district
* square feet (negative in price/sqft model)
* bathroom count
* 4 variables for different time periods
* whether I favorited the house
* lot size
* prewar (historic houses)
* walkscore

Bedroom count was not positive so was removed.

```
const                708.138537
SQUARE FEET           -0.251568
BATHS                 34.057259
recent                49.545652
target               -57.288701
thisspring             9.578131
lastfall             -39.910019
FAVORITE              58.796615
walkscore              1.929512
LOT SIZE               0.014656
historic              33.158759
chabot               156.026660
peralta               79.286202
crocker_highlands     77.134351
piedmont              56.810591
emerson                0.387973
```
To run again

* sample.py merges data and runs filters
* add_walkscore.py fetches walkscore for the whole sample
* model.py runs the model
