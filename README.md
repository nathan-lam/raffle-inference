# What is this?
Statistical analysis on a raffle Ive been participating in since 2015.
The raffle is conducted every December and lasts around a month. The data I analyze is from the results I get.

This is data I use to play around with statistical concepts

# How the raffle works
Every 24 hours, a user gets a chance to "roll" on a website to get rewards.

The (observed) rewards are the following:
- 0 Points
- 25 Points
- 50 Points
- 100 Points
- 250 Points
- 500 Points
- 1000 Points
- Random product

# Analysis 
- [x] Estimate the frequentist multinomial distribution
- [x] Estimate the Bayesian multinomial distribution
- [x] Estimate the (frequentist) multinomial distribution with markov chains
- [ ] Create an Auto Regressive model
  - [ ]   Figure out how to conduct categorical time series
     
I am open to more types of analysises if it makes sense in this context.

# Results 

| Method      | 0 Points | 25 Points | 50 Points | 100 Points | 250 Points | 500 Points | 1000 Points |Random Product |
|-------------|----------|-----------|-----------|------------|------------|------------|-------------|---------------|
| Frequentist | 43.3%    | 8.26%     | 32.48%    | 11.97%     | 2.28%      | 0.28%      | 0.28%       | 1.14%         |
| Markov      | 41.98%   | 8.83%     | 32.67%    | 12.44%     | 2.34%      | 0.29%      | 0.3%        | 1.17%         |
| Bayesian    | 43.34%   | 8.43%     | 32.3%     | 11.91%     | 1.99%      | 0.44%      | 0.44%       | 1.11%         |
Last updated 2025-02-20



