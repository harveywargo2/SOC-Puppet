# DetectCon
- DetectCon is a rating tag to help weight your detections
- Very similar to DefCon Readiness Ratings 
  - https://simple.wikipedia.org/wiki/DEFCON

## Detect Con Numerical Rating

| DetectCon   | Urgency     | Investigation Effort | Precision | Noise     | Volume           | Confidence |
|-------------|-------------|----------------------|-----------|-----------|------------------|------------|
| DetectCon 1 | Rapid       | Very Low             | Very High | None      | Only Atk Pattern | Very High  |
| DetectCon 2 | High        | Low                  | High      | Low       | Very Low         | High       |
| DetectCon 3 | Normal      | Moderate             | Mixed Bag | Mixed Bag | Low              | Moderate   |  
| DetectCon 4 | Low         | High                 | Enrich    | High      | Moderate         | Low        |
| DetectCon 5 | Low/Unknown | Very High            | Unknown   | Unknown   | High/Excessive   | Unknown    |

### Categories
##### DetectCon 
  - Similar to DefCon a ranking of 1-5 with 1 being you are at war 
##### Urgency  
  - The manner at which the detection should be prioritized in an alert or incident queue 
##### Investigation Effort 
  - The expected amount of work or effort on the Responder/Analyst to validate the detection represents an actual attack pattern
  - This may be improved with enrichment to the detection
##### Precision 
  - How precise is the detection does it match the Attack Pattern and nothing else 
##### Noise 
- How much noise will come from detection
##### Volume  
- Expected or measured volume per period of reporting 
##### Confidence  
- Confident are you in your ratings of Urgency/Load/Precision/Noise/Volume 
- May be 

### How to Use
- The goal is to make everything a DetectCon 1 or 2 from Logic or Enrichment
- It is more of a scale and a hard ranking system
- Also meant to track metrics and compare against your DetectCon ratings
- Instead of using Fidelity combine and measure (Precision-Noise-Volume)
  - Emulation helps on this front 