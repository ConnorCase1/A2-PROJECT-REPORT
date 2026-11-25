# Real-Time Voice Emotion Analysis

Project status: offline interactive simulation only. Four fictional calls demonstrate rising distress, a fear/frustration mismatch, falling distress, and missing audio. No microphone, real model, personal data or external services. Scores are illustrative and not emergency risk.

Prose word count: 202 (including headings)

## Run
Open Voice Emotion System.html in a browser. Select a scenario, play or step through segments, request clarification, record observations, then inspect and export the completed review. Reset clears the session.

## Technology
HTML, CSS, JavaScript. Playwright and Chromium are optional for automated tests.

## Development record
- Initial replay: timeline, weighted concern score, confidence warnings and correction log.
- Experimental microphone integration was attempted in an earlier revision but not verified end to end.
- Current revision removes microphone and model dependencies, adds recovery and missing-input scenarios, gap-aware plotting, distinct outcome summaries and missing-input warnings.
- Browser tests executed for all four scenarios, exports, reset, low confidence and preserved observations. See development/test-results.txt. Tests do not validate emotion accuracy or usability.

## AI assistance
ChatGPT assisted with the prototype and test scripts. I checked the system and test cases and confirmed that it/they were feasible and consistent with my report. 

## Additional files
Diagrams and storyboards contain sequences and browser screenshots.
