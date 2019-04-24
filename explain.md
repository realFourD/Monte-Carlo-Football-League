# Simulation Method

The goal is to create a program to take random samples from a distribution to simulate the goals scored for each team in each game of the 2017/18 BPL Season. This requires comparing the recorded scores from the real season to generate a different distribution based of which teams are playing and where they are playing.
Then this simulated scored from each game is used to update a league table. Once the league table is completed, it starts over again until one million season are completed.

## Relative Strengths
To create a simulation that is based on the 2017/18 BPL Season we need a metric of how strong each team is compared to another during that season.


### **Definition 1**
Define $M_{i,j} = (h_{i,j}, a_{i,j}) \in \N^2 :  i,j \in \{1,...,20\}$ a vector of the number of goals for the match team $\text{i}$ against team $\text{j}$

**Note:** $\nexists M_{i,i} : i \in \{1,...,20\}$ as teams can't play themselves

**Note:** In general $M_{i,j} \neq M_{j,i}$ as they represent different matches ($\text{i}$ is the home team and $\text{j}$ is the away team)


### **Definition 2**
The average number of _Goals For_ team $\text{i} \in \{1,...,20\}$ is
$$\bar H_{i} = \frac{1}{19} \sum_{j=1, j \neq i}^{20} h_{i,j}$$

The average number of _Goals Against_ team $\text{i} \in \{1,...,20\}$ is
$$\bar A_{i} = \frac{1}{19} \sum_{j=1, j \neq i}^{20} a_{j,i}$$


### **Definition 3**
The average number of _Goals For_ across the whole league is
$$\bar H_{PL} = \frac{1}{380} \sum_{i=1}^{20} \sum_{j=1, j \neq i}^{20} h_{j,i} =\frac{1}{20} \sum_{i=1}^{20} \bar H_{i}$$
The average number of _Goals Against_ across the whole league is
$$\bar A_{PL} = \frac{1}{380} \sum_{i=1}^{20} \sum_{j=1, j \neq i}^{20} a_{j,i} = \frac{1}{20} \sum_{i=1}^{20} \bar A_{i}$$

### **Data 1**
An extract from the table of these values from our simulation, comparing $\text{PL}, i=1, i=2$:
| _Team:_ $\text{i}$| _Goals For:_ $\bar H_{i}$| _Goals Against:_ $\bar A_{i}$|
| :--: |:------:| :------:|
| PL | 1.5316 | 1.1474 |
| 1  | 2.8421 | 1.0526 |
| 2  | 1.3684 | 1.5789 |

Using these values we can give each team a relative strength compared to the whole league average

### **Definition 4**
The Strength metrics are define as the ratio of the teams goals against the league average and provide a estimate of the measure of a teams ability compared to another. Combined these four metrics are used to determine the the outcome of each game in the simulation based on how well they performed previously.

The _Home Attack Strength_ of team $\text{i} \in \{1,...,20\}$ is
$$\mu_{i} = \frac{\bar H_{i}}{\bar H_{PL}}$$

The _Home Defensive Strength_ of team $\text{i} \in \{1,...,20\}$ is
$$\theta_{i} = \frac{\bar H_{i}}{\bar A_{PL}}$$

The _Away Attack Strength_ of team $\text{i} \in \{1,...,20\}$ is
$$\rho_{i} = \frac{\bar H_{i}}{\bar A_{PL}}$$

The _Away Defensive Strength_ of team $\text{i} \in \{1,...,20\}$ is
$$\tau_{i} = \frac{\bar H_{i}}{\bar H_{PL}}$$

The _Attack Strengths_ can be interpreted as how productive a team is compared to the average at scoring goals.
The _Defensive Strengths_ can be interpreted as how unproductive a team is compared to the average at stopping the opponent getting goals.

### **Data 2**
An extract from the table of Strength metrics from our simulation, comparing team 1 vs team 2:
| _Team:_ $\text{i}$ | _Home Attack Strength:_ $\mu_{i}$ | _Home Defensive Strength_ $\theta_{i}$ | _Away Attack Strength_ $\rho_{i}$ | _Away Defensive Strength_ $\tau_{i}$ |
| :--: |:------:| :------:|:------:| :------:|
| 1  | 1.8557 | 0.9174 | 0.9174 | 1.0653 |
| 2  | 0.8935 | 1.3761 | 0.8716 | 1.0653 |


## Distributions
To generate a random number of goals to we will use a Poisson Distribution, as we can provide the expected value of number of times the event of a goal will happen for the fixed interval of a match. We will assume goals are independent events and will happen at a constant rate.


### **Definition 5**
For each match we need two distributions

The _Home Goals_ distribution is
$$
X \sim Pois( \lambda_{i,j} )
$$
$$
\text{where } \lambda_{i,j} = \bar H_{PL} * \mu_{i} * \rho_{j}
$$

The _Away Goals_ distribution is
$$
Y \sim Pois( \gamma_{i,j} )
$$
$$
\text{where } \gamma_{i,j} = \bar A_{PL} * \theta_{i} * \tau_{i}
$$


### **Data 3**
An extract from the table of $\lambda$ from our simulation, comparing team 1 vs team 2:
| $\text{i, j}$ | $\text{Exp(X)}=\lambda_{i,j}$| $\text{Exp(Y)}=\gamma_{i,j}$ |
| :--: |:------:| :------:|
| 1, 2  | 3.0277 | 0.9174 |
| 2, 1  | 1.4578 | 1.4486 |


# Monte Carlo
Now we have got a system to take random sample from, we can create a random league table based of the relative strengths of the teams by sampling both distributions of all combinations of teams and locations in the 2017/18 season (380 games). This is then repeated to one million times to provide a large data set to work from.


### **Data 4**
The average of each team across the one million games, ordered by points
| Team: $\text{i}$ |Wins| Draw |Loses | Goals For | Goals Against | Points |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 11| 30.0784| 4.8544| 3.0672| 108.6174| 25.4654| 95.0896|
| 10| 24.8517| 6.4416| 6.7067| 85.2132| 36.7837| 80.9967|
| 12| 23.9282| 7.8319| 6.24| 69.6161| 27.517| 79.6163|
| 17| 23.2561| 7.4921| 7.2518| 75.1294| 35.1381| 77.2603|
| 5| 20.2851| 8.6451| 9.0697| 62.8351| 37.5641| 69.5005|
| 1| 19.0866| 7.216| 11.6973| 73.9149| 49.6972| 64.4759|
| 9| 14.6632| 8.5295| 14.8073| 55.5999| 59.7837| 52.519|
| 4| 12.9196| 11.3036| 13.7768| 36.4468| 39.6026| 50.0624|
| 13| 12.6619| 10.1471| 15.191| 39.1741| 47.5888| 48.1327|
| 6| 12.5084| 9.1944| 16.2973| 44.8662| 55.3766| 46.7195|
| 7| 12.2159| 8.7634| 17.0207| 43.6441| 58.3841| 45.4112|
| 2| 11.6469| 8.848| 17.505| 44.5324| 61.3937| 43.7888|
| 20| 11.5945| 8.3639| 18.0416| 47.2011| 68.2646| 43.1475|
| 18| 10.9375| 8.6386| 18.4239| 43.4271| 64.4938| 41.4512|
| 14| 10.3721| 9.5793| 18.0486| 36.8058| 56.7882| 40.6956|
| 3| 9.776| 9.6668| 18.5572| 33.9263| 54.9812| 38.9947|
| 19| 8.5363| 9.8108| 19.6529| 30.9103| 57.2255| 35.4196|
| 16| 7.9923| 9.8009| 20.2068| 27.8505| 57.3303| 33.7778|
| 15| 8.3082| 8.5703| 21.1215| 34.3849| 69.1344| 33.4948|
| 8| 7.7102| 9.6444| 20.6455| 27.7929| 59.3754| 32.7748|