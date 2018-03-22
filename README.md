# Reddit Comment Engagement Exploration
Determining features that drive comment engagement on Reddit posts

See blog post here: https://tucker-allen.github.io/Reddit_Comment_blog/

---

## Repo Layout

- README.md
- code
  - Reddit_Scraper_AWS.py <-- The scraper that was hosted on AWS to collect data
  - code.ipynb <-- Where I executed my code and models
- data
  - Data_16.csv <-- Checkpoint file
  - Data_96.csv <-- Checkpoint file
  - Data_192.csv <-- Final accumulation of scraped data

-----------------------

## Summary:
Analyzing the results of 48hrs worth of webscraping data from the Reddit API, we have constructed a classification model that determines the "engagement" attached to a Reddit post from the front page with ~82% average accuracy. "Engagement" is designated as a either 'High', or 'Low', with the boundary drawn at the median number of comments per post determined from the scraped data. The features that appeared to heavily favor higher engagement included if a post is about tragic current events (a school shooting) or emotionally weighted topics (Ajit Pai). Higher engagement was also linked to, expectedly, more upvotes/higher score (usually meaning more visibility). While the findings of this scraping project were interesting, I don't believe that any of the correlation measures will hold true universally, since we only scraped information for 48 hours, and during a time when there was a tragic crisis unfolding in the U.S., rendering the window in which this excercise was conducted, an outlier. Further, I believe a high level of variability was introduced by the fact that it was not evident when a post was determined to "expire", and disappear from the front page.