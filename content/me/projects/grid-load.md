+++
date = '2026-06-01T00:00:00+05:30'
title = 'grid-load forecast'
summary = "daily electricity demand dataset and rolling 48-hour forecast dashboard"
tech = ['python', 'github actions']
github = 'https://github.com/jitendradara12/grid-load'
live = 'https://grid-load.indevs.in/'
year = 'jun 2026'
weight = 9
+++


grid-load predicts India's electricity Demand for the next 48 hours.
the whole pipeline is automated from data scraping to the forecast [dashboard](https://grid-load.indevs.in) .

### workflow

![workflow diagram](/grid-load-workflow.png)

source code is available at: https://github.com/jitendradara12/grid-load

### row notes which i wrote during development...

> 1. The best data yet is found on [npp](https://npp.gov.in/dashBoard/gc-map-dashboard-meritchart).
> 2. The api is unprocted and dumps json directly on `curl 'https://npp.gov.in/dashBoard/demandmet1chartdata?date=2026-06-08'`
> 3. The Endpoints served data all the way from sep25, my `scripts/fetch_yesterday` script runs everyday and updates the dataset with latest rows.
> 4. ICED dataset is longer and `scripts/clean_datasets.py` cleans and `src/data_pipeline.py` merges them to get
>    Combined time series spans from 2017-01-01 00:00:00 to present.
> 5. Currently, using merged data for training and NPP dataset for inference.
> 6. Most reasonable way for the model is ridge regression. weather/temperature features aren't integrated yet. 
