# DetectCon

DetectCon is a rating tag to help weight your detections 

#### Urgency
- This is the suggested speed at which a SOC analyst should prioritize this alert
- 

#### Analyst Load
- How much additional DFIR/Investigation is put on the analyst before declaration of Incident

#### Fidelity
- 


## Detect Con Numerical Rating 

| DetectCon   | Urgency     | Analyst Load | Fidelity                                                                           |
|-------------|-------------|--------------|------------------------------------------------------------------------------------|
| DetectCon 1 | Rapid       | Very Low     | Extremely High Fi - Should Never See This Activity Outside of Cyber Threat         | 
| DetectCon 2 | High        | Low          | High Fi - Very Low False Rate and Highly Unlikely Activity Outside of Cyber Threat |
| DetectCon 3 | Moderate    | Moderate     | High Fi - False Rates May Exist Due To Alert Blending With Normal Activity         |     
| DetectCon 4 | Normal      | High         | Medium Fidelity - False Events Likely Without Enrichment or Correlation            |
| DetectCon 5 | Low/Unknown | Very High    | Low/Unknown Alerting Very Intensive Investigation Efforts To Confirm               |

