# NBA Player Value Analysis: Finding the Most Undervalued Players

A data analytics project that identifies undervalued NBA players by analyzing their performance metrics relative to their salaries (2022-2024 seasons).

## Project Overview

This project uses the NBA API and salary data to calculate a comprehensive "value score" for NBA players, revealing which players provide the best performance per dollar spent. The analysis considers multiple statistics including points, rebounds, assists, steals, and blocks.



## 📈 Visualization

![Player Value Analysis](player_value_detailed.png)

*Green dots indicate undervalued players (high performance relative to salary), while red dots indicate overvalued players (low performance relative to salary).*

## Methodology

### Data Sources
- **Player Statistics**: NBA API (`nba_api` Python package)
- **Salary Data**: NBA player salaries (2022-2024)


# Sample Results

Stats data: 157 rows
Salary data: 1214 rows

Merged data: 47 rows

Qualified players (40+ games, 20+ MPG): 35

ALL QUALIFIED PLAYERS RANKED BY VALUE (40+ GP, 20+ MPG)


             PLAYER_NAME SEASON_ID       MPG       PPG       RPG      APG      SPG      BPG  COMPOSITE_SCORE     Salary  VALUE_SCORE
           Jose Alvarado   2022-23 21.475410  9.016393  2.311475 3.049180 1.098361 0.163934        18.888525  1563518.0    12.080785
           Jose Alvarado   2024-25 24.392857 10.339286  2.428571 4.625000 1.321429 0.250000        23.333929  1988598.0    11.733859
            Cole Anthony   2022-23 25.866667 13.016667  4.800000 3.916667 0.616667 0.516667        26.918333  3613680.0     7.449009
        Precious Achiuwa   2022-23 20.745455  9.236364  5.963636 0.909091 0.563636 0.545455        19.974545  2840160.0     7.032894
             Deni Avdija   2023-24 30.093333 14.693333  7.200000 3.813333 0.800000 0.480000        31.613333  6263188.0     5.047483
        Precious Achiuwa   2023-24 24.224490  7.591837  7.163265 1.081633 0.612245 1.142857        21.320408  4379526.0     4.868200
             Deni Avdija   2022-23 26.578947  9.171053  6.407895 2.776316 0.855263 0.381579        23.498684  4916160.0     4.779886
        Precious Achiuwa   2023-24 21.945946  7.635135  6.581081 1.310811 0.621622 0.918919        20.579730  4379526.0     4.699077
            Ochai Agbaji   2024-25 27.171875 10.421875  3.781250 1.531250 0.906250 0.468750        20.006250  4310280.0     4.641520
            Cole Anthony   2023-24 22.432099 11.567901  3.839506 2.913580 0.790123 0.456790        23.039506  5539771.0     4.158928
             Deni Avdija   2024-25 30.013889 16.930556  7.250000 3.902778 0.986111 0.486111        34.429167  8486619.0     4.056877
            Ochai Agbaji   2022-23 20.491525  7.915254  2.050847 1.135593 0.271186 0.254237        13.130508  3918360.0     3.351021
            Ochai Agbaji   2023-24 21.051282  5.833333  2.769231 1.064103 0.602564 0.564103        13.085897  4114200.0     3.180666
           Kyle Anderson   2022-23 28.362319  9.376812  5.333333 4.855072 1.130435 0.913043        27.146377  8780488.0     3.091671
           Grayson Allen   2023-24 33.506667 13.520000  3.933333 3.026667 0.920000 0.600000        25.820000  8925000.0     2.892997
        Precious Achiuwa   2024-25 20.526316  6.649123  5.561404 0.964912 0.824561 0.736842        17.892982  6275861.0     2.851080
Nickeil Alexander-Walker   2023-24 23.426829  7.987805  2.036585 2.487805 0.780488 0.512195        16.748780  7073602.0     2.367787
           Grayson Allen   2022-23 27.388889 10.416667  3.291667 2.263889 0.861111 0.194444        19.873611  8925000.0     2.226735
           Kyle Anderson   2023-24 22.556962  6.405063  3.455696 4.189873 0.898734 0.594937        19.824051  9219512.0     2.150228
           Jarrett Allen   2023-24 31.714286 16.506494 10.532468 2.727273 0.688312 1.051948        36.716883 20000000.0     1.835844
              OG Anunoby   2022-23 35.611940 16.776119  4.955224 1.955224 1.910448 0.746269        30.968657 17357143.0     1.784202
            Steven Adams   2022-23 26.976190  8.595238 11.547619 2.309524 0.857143 1.095238        29.821429 17926829.0     1.663508
           Jarrett Allen   2022-23 32.647059 14.250000  9.794118 1.661765 0.794118 1.235294        32.554412 20000000.0     1.627721
              OG Anunoby   2024-25 36.567568 18.000000  4.837838 2.216216 1.486486 0.878378        31.859459 19928571.0     1.598683
           Jarrett Allen   2024-25 28.000000 13.451220  9.731707 1.926829 0.939024 0.890244        31.678049 20000000.0     1.583902
              OG Anunoby   2023-24 34.040000 14.660000  4.160000 2.140000 1.360000 0.720000        27.022000 18642857.0     1.449456
   Giannis Antetokounmpo   2022-23 32.126984 31.095238 11.777778 5.698413 0.825397 0.809524        57.046032 42492492.0     1.342497
             Bam Adebayo   2022-23 34.640000 20.386667  9.173333 3.200000 1.173333 0.813333        40.168000 30351780.0     1.323415
   Giannis Antetokounmpo   2023-24 35.164384 30.438356 11.520548 6.520548 1.191781 1.082192        58.591781 45640084.0     1.283779
             Bam Adebayo   2023-24 34.028169 19.253521 10.380282 3.915493 1.140845 0.929577        41.723944 32600060.0     1.279873
   Giannis Antetokounmpo   2024-25 34.164179 30.388060 11.910448 6.462687 0.865672 1.164179        58.434328 48787676.0     1.197727
             Bam Adebayo   2024-25 34.282051 18.076923  9.602564 4.320513 1.256410 0.679487        39.952564 34848340.0     1.146470
           Deandre Ayton   2022-23 30.373134 17.955224  9.955224 1.716418 0.552239 0.791045        35.162687 30913750.0     1.137445
           Deandre Ayton   2023-24 32.418182 16.727273 11.072727 1.636364 1.018182 0.763636        36.032727 32459438.0     1.110085
           Deandre Ayton   2024-25 30.150000 14.400000 10.150000 1.600000 0.775000 0.975000        32.480000 34005126.0     0.955150

Full results saved to data/undervalued_players_comprehensive.csv


SUMMARY STATISTICS

Total qualified players: 35
Average salary: $16,327,634
Average MPG: 28.4
Average composite score: 29.64
Average value score: 3.29


MOST EFFICIENT PLAYER

2022-23 Jose Alvarado
  MPG: 21.5
  PPG: 9.0, RPG: 2.3, APG: 3.0
  SPG: 1.1, BPG: 0.2
  Composite Score: 18.89
  Salary: $1,563,518
  Value Score: 12.08


LEAST VALUABLE PLAYER

2024-25 Deandre Ayton
  MPG: 30.1
  PPG: 14.4, RPG: 10.2, APG: 1.6
  SPG: 0.8, BPG: 1.0
  Composite Score: 32.48
  Salary: $34,005,126
  Value Score: 0.96


## 📝 Insights

- Players on rookie contracts tend to provide exceptional value
- Guard positions often show higher value scores due to assists and steals
- Role players with strong defensive stats (steals/blocks) are frequently undervalued

This project is open source and available under the [MIT License](LICENSE).
