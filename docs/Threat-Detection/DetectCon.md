# DetectCon
- DetectCon is a rating tag to help weight your detections
- Very similar to DefCon Readiness Ratings 
  - https://simple.wikipedia.org/wiki/DEFCON


## Detect Con Numerical Weighting Scale

| DetectCon   | Urgency     | Analysis Effort | Noise/PatternMatch | In The Wild | Volume           | Confidence |
|-------------|-------------|-----------------|--------------------|-------------|------------------|------------|
| DetectCon 1 | Rapid       | Very Low        | Zero/High          | Guaranteed  | Only Atk Pattern | Very High  |
| DetectCon 2 | High        | Low             | Low/High           | Very Common | Very Low         | High       |
| DetectCon 3 | Normal      | Moderate        | Mixed/Medium       | Common      | Low              | Moderate   |  
| DetectCon 4 | Low         | High            | Blend/High         | Not Common  | Moderate         | Low        |
| DetectCon 5 | Low/Unknown | Very High       | Unknown/Unknown    | Unknown     | High/Excessive   | Unknown    |


### Categories
##### DetectCon 
- Similar to DefCon a ranking of 1-5 with 1 being you are at war 
##### Urgency  
- The manner at which the detection should be prioritized in an alert or incident queue
##### Analysis Effort 
- The expected amount of work or effort on the Responder/Analyst to validate the detection represents an actual attack pattern
- This may be improved with enrichment to the detection
##### Noise/PatternMatch
- Simple ratio to show the noise to pattern match ratio
- Zero/X is best 
##### In The Wild 
- How common is this pattern reported in the wil
##### Volume  
- Expected or measured volume per period of reporting 
##### Confidence  
- How Confident are you in your weighting being correct



### How to Use
- The goal is to make everything a DetectCon 1 or 2 from Logic or Enrichment
- It is more of a method to weigh than a linear ranking system
- Also meant to track metrics and compare against your DetectCon ratings
- Instead of using Fidelity combine and measure (AccuracyToNoise Ratio with Volume)