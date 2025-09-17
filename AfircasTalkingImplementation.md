# Africa's Talking USSD & SMS Integration Guide

To make the platform accessible to students in remote areas with limited or no internet access, we will integrate the platform with **Africa's Talking USSD** and **Africa's Talking SMS** services. This allows students to enroll and receive their login credentials via basic mobile phones using GSM networks, without requiring data or internet connectivity.

## Overview of the Feature

Students will be able to:

* Dial a provided USSD code (e.g. `*123#`) from any phone.
* Navigate a simple menu to register themselves.
* Once registered, they will receive an SMS containing their default login credentials (username and password) and instructions on how to access the system later when they have internet access or can reach a digital center.

This creates a **low-barrier entry point** for learners in rural or underserved areas, ensuring that enrollment is not limited to internet-enabled devices.

## How It Will Work

1. **Student dials the USSD code**  
   The student enters the short code (e.g. `*123#`) on their phone to open the USSD application.

2. **USSD menu is displayed**  
   The USSD menu is served from our backend through Africa's Talking USSD. The menu will guide the student through:
   * Selecting "Enroll as a student"
   * Entering their full name
   * Entering their phone number (pre-filled from SIM if supported)
   * Choosing their level of study (e.g. Secondary, Vocational, College)

3. **Backend receives and stores registration details**  
   Our CLI-based backend system will receive this data through Africa's Talking USSD API and store it in our main user database, assigning each new student a unique student ID.

4. **Send confirmation SMS with credentials**  
   Once enrollment is successful, the backend will use **Africa's Talking SMS** to send an SMS back to the student with:
   * Their student ID
   * A default password
   * A short URL to the platform
   * Instructions to change their password on first login

## Why This Is Useful

* **Bridges the digital divide**: Students without smartphones or internet can still join and access learning opportunities.
* **Frictionless onboarding**: No need for data bundles or app downloads to register.
* **Improved outreach**: Schools and organizations can enroll large numbers of students quickly during outreach campaigns.
* **Offline-first approach**: Students can complete enrollment offline and later transition to online access when they get connectivity.

## Tools Available via USSD

* **Student Enrollment**: Register new students with basic details.
* **Enrollment Status Check**: Students can check if they are already registered.
* **Password Reset Request**: Students can request a new password which will be sent via SMS.
* **Information Menu**: Basic info about how to use the platform or where to get help.

## Tools Available via SMS

* **Welcome/Onboarding SMS**: Sent immediately after registration with credentials.
* **Password Reset SMS**: If a user requests a new password through USSD.
* **Notifications/Alerts**: System can broadcast messages to all registered users (e.g. reminders, new courses, announcements).

## Implementation Summary

1. **Set up Africa's Talking account**
   * Create a developer account at Africa's Talking.
   * Activate the **USSD** and **SMS** products on the dashboard.

2. **Configure USSD application**
   * Request a USSD short code or use a shared code with a unique service code.
   * Set the callback URL to your CLI app endpoint (which will serve the menu and handle user responses).

3. **Configure SMS application**
   * Set up a sender ID or use the default Africa's Talking shortcode.
   * Use the SMS API to send messages from the backend when registration is complete.

4. **Integrate with your CLI backend**
   * Write USSD menu logic to capture user input and save it to your user database.
   * Generate default credentials (username + password).
   * Call the SMS API to deliver the credentials to the student.