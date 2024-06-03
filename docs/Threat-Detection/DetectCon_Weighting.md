# DetectCon 
- DetectCon is a rating tag to help weight your detections
- Very similar to DefCon Readiness Ratings 
  - https://simple.wikipedia.org/wiki/DEFCON
- This is meant to measure and rate your threat detections

## DetectCon Weighting Categories
- Similar to DefCon a ranking of 1-5 with 1 being you are at war 

##### Urgency 
- The manner at which the detection should be prioritized in an alert or incident queue
- This is where detection engineer passes XP to analyst 

##### In The Wild : Days 
- How common is this pattern reported in the wild

##### Estimated Analysis Effort 
- The expected amount of effort the analyst will perform to validate the detection against Threat Activity
- This only considers the effort of analysis needed to ring the fire alarm, post fire alarm much analyst/response will occur
  - LSASS alerts or OS Cred Dumping are normally very low effort to ring the alarm
  - Some Discovery alert like net clt or scanning might take moderate to high analysis effort
- This may be improved with enrichment to the detection
- This probably shows what detections need enrichment or correlations

##### Noise to Pattern Match Ratio : Days 
- Simple ratio to show the noise to pattern match ratio
- Zero/X is best 
- This should also represent your regression testing
- Potentially could be updated via metrics 

##### Regression Test Volume : Days 
- Expected or measured volume per period of reporting 
- If you run emulations this should just match your emulations or your incidents

##### Confidence 
- How Confident are you in your weighting being correct


## Detect Con Decision Matrix
| Urgency | ITW:Days    | AE        | NTPMR:Days | RTV:Days         | Confidence |
|---------|-------------|-----------|------------|------------------|------------|
| Rapid   | Very Common | Low       | Zero       | Only Atk Pattern | Very High  |
| High    | Common      | Normal    | Low        | Low              | High       |
| Normal  | Probable    | High      | Accepted   | Accepted         | Moderate   |  
| Low     | Not Likely  | Excessive | High       | High             | Low        |
| Unknown | Unknown     | Unknown   | Excessive  | Excessive        | Unknown    |


## How to Use 
- The goal is to make everything a DetectCon 1 or 2 from Logic or Enrichment
- It is more of a method to weigh than a linear ranking system
- Also meant to track metrics and compare against your DetectCon ratings
- Instead of using Fidelity combine and measure (AccuracyToNoise Ratio with Volume)

