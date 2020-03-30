# telemed-onboarding
To onboard doctors on telemed


### Rough outline:

- Doctors receive a form via link --> they fill up and submit.
- Basic validation (doctor is from India and not expecting money) _Drop if invalid_
- Update the response in a database of master list (sheet) with certain tags and additional info.
- Verify by Practo. _Drop if invalid_
- Create credentials via freshdesk and update sheet with credentials
- Update master list (sheet) with webinar attendance status
- If webinar attendance is negative, send emails, sms and other reminders like call from volunteers for self training material.
- If trained self, ask to fill a form B with further questions. If didn't take up training, discard as _not interested/serious_
- If webinar attendance is positive, send credentials and finish onboarding by making a call from volunteer. 
- Update master list with sheet.
