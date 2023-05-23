# p4: NYC Higher or Lower by Yammers
### Overview: 
Inspired by the higher or lower game, our project will feature an interactive game where users compare two different neighborhoods based on an arbitrary data set. For each round, users will face a random order of data sets, such as the number of street trees, or teacher salaries, in two randomized boroughs around NYC. They will be asked to compare the two, with a question along the lines of “Which borough has more water fountains?” or “Which borough has a higher average firefighter salary?” After users answer a question, they will see an interactive map of NYC that shows the distribution of the data set across all boroughs in NYC. This will be done via different bubble sizes indicating higher amounts/densities. Thirteen unique datasets and nineteen unique questions are included and after the user strings together ten correct answers in a row, they are able to claim victory.

## Maya Nelson (PM)
## Sam Lubelsky
## Sam Cowan
## Ameer Alnasser

## Launch Codes:
Run:
```java
 git clone git@github.com:mayanelson/p4.git
 cd p4
 pip install -r ./requirements.txt    
 cd app
 python3 __init__.py
 ```
Then it should appear at 127.0.0.1:5000

Also viewable on Newsify.social

### Data
Our data is pulled exclusively from NYC OpenData, using their Socrata Open Data API. The following datasets were pulled from and stats from each borough are either averaged or counted up depending on the question:
- [Citywide Payroll Data](https://data.cityofnewyork.us/City-Government/Citywide-Payroll-Data-Fiscal-Year-/k397-673e)
  - Names, agency, pay, etc about everyone who was paid by the city each year
- [Dog Licenses](https://data.cityofnewyork.us/Health/NYC-Dog-Licensing-Dataset/nu7n-tubp)
  - List of all dogs currently licensed in the City, with zip code, which we used the geopy library/api to convert to borough
- [Film Permits](https://data.cityofnewyork.us/City-Government/Film-Permits/tg4x-b46p)
  - List of all film permits in NYC
- [Police Officer Complaint History](https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i)
  - List of all complaints responded to by police
- [Street Tree Census](https://data.cityofnewyork.us/Environment/2015-Street-Tree-Census-Tree-Data/uvpi-gqnh)
  - List of all trees in NYC
- [Public Recycling Bins](https://data.cityofnewyork.us/Environment/Public-Recycling-Bins/sxx4-xhzg)
  - List of all public recycling bins (this is not the same as total recycling bins, the number is vastly lower)
- [Rodent Inspections](https://data.cityofnewyork.us/Health/Rodent-Inspection/p937-wjvj)
  - List of all rat inspections and their results.
- [School Bus Breakdowns](https://data.cityofnewyork.us/Transportation/Bus-Breakdown-and-Delays/ez4e-fazm)
  - List of school bus breakdowns and delays
- [Water Fountains](https://data.cityofnewyork.us/dataset/Cool-It-NYC-2020-Drinking-Fountains/wxhr-qbhz)
  - Locations of all public drinking fountains as of 2020
- [Asbestos Abatemants](https://data.cityofnewyork.us/Environment/Asbestos-Control-Program-ACP7-/vq35-j9qm)
  - Location/results of all asbestos abatements in the city
- [Elevator Permits](https://data.cityofnewyork.us/Housing-Development/DOB-NOW-Build-Elevator-Permit-Applications/kfp4-dz4h)
  - List of all elevators in City
- [Firehouses](https://data.cityofnewyork.us/Public-Safety/FDNY-Firehouse-Listing/hc8x-tcnd)
  - Locations of all firehouses in NYC
- [Fires Started](https://data.cityofnewyork.us/Public-Safety/Bureau-of-Fire-Investigations-Fire-Causes/ii3r-svjz)
  - Causes of every fire started in NYC
