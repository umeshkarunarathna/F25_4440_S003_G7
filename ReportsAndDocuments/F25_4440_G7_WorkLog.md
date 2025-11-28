# 🧾 Work Log – F25_4440_G7

| **Date**         | **Student** | **Work Summary**                                                                 | **Hours** |
|------------------|-------------|----------------------------------------------------------------------------------|------------|
| 15th Sep 2025    | Both        | Group formed and agreed on individual roles.                                    | 0.5        |
| 6th Oct 2025     | Umesh       | Researched tools and apps suitable for the project.                             | 1.0        |
| 6th Oct 2025     | Sahan       | Conducted research on tools and applications for analysis.                      | 1.0        |
| 7th Oct 2025     | Umesh       | Drafted an email to professor to finalize tools and applications.               | 0.5        |
| 9th Oct 2025     | Both        | Met with professor to discuss project scope and confirm selected tools & apps.  | 0.5        |
| 21st Oct 2025    | Umesh       | Researched and set up ALEAPP and MobSF; drafted extraction workflow for Dropbox & Strava. | 1.0        |
| 22nd Oct 2025    | Sahan       | Researched and set up Drozer and JADX; drafted assessment plan for Trust Wallet & Spotify. | 1.0        |
| 28th Oct 2025    | Umesh       | Installed Android SDK command-line tools and configured AVD, ADB, SDKManager, and APKAnalyzer paths. Created and launched emulator. Installed Dropbox and Strava APKs for testing. | 2 |
| 29th Oct 2025 (Night) | Umesh  | Created an email account, separate Strava and Dropbox test accounts and linked them to emulator. Generated a mock GPX route around Vancouver and imported it to simulate an activity. Activity did not appear on Strava; began troubleshooting and analyzing logs. | 2.0 |
| 30th Oct 2025 (Morning) | Umesh | Investigated Strava database structure using DB Browser for SQLite. Injected mock JSON activity entry into `strava-database`. Encountered app crash due to missing native library (`libFatmapSdk.so`). | 2.5 |
| 1st Nov 2025 (Morning) | Sahan | Setup drover and made a successful connection to the emulator. encountered error connecting it to the emulator and getting the right ip address | 3 |
| 5th Nov 2025 | Umesh | Uploaded prepared sample files to Dropbox to simulate user data and activity. Verified folder structure for forensic testing. | 1.0 |
| 5th Nov 2025 | Umesh | Installed and configured both ALEAPP and MobSF tools in the project environment. Verified successful setup and readiness for analysis. | 1.5 |
| 6th Nov 2025 | Sahan | Tested Drozer connectivity to an Android emulator, learned how to start the Drozer agent, and explored basic commands (run app.package.list, run app.package.info). | 1.0 |
| 7th Nov 2025 | Umesh | Attempted to create sample app data for Strava using emulator. | 1 |
| 8th Nov 2025 | Sahan | Installed JADX-GUI and JADX-CLI, explored interface layout, and learned preferences for decompilation accuracy. | 1.5 |
| 8th Nov 2025 | Umesh | Created sample activities for Strava account using a separate device and made it visible in the emulator. | 1 |
| 9th Nov 2025 | Umesh | Pulled data/data directories of both the apps and ran ALEAPP on those folders. | 1.5 |
| 9th Nov 2025 | Sahan | Practiced decompiling a sample APK using JADX, inspected file tree, learned how to navigate Java source, resources, and smali. | 2.0 |
| 9th Nov 2025 | Sahan | Researched Drozer modules for attack surface mapping (scanner.activity, scanner.provider, scanner.broadcast).| 1.5 |
| 9th Nov 2025 | Umesh | Analyzed permission errors for .mapbox & .fit files in Strava extraction. Reran with elevated privileges. | 1 |
| 9th Nov 2025 | Umesh | Troubleshoot empty ALEAPP reports and manually inspected WAL/SQLite files for forensic artifacts. | 2 |
| 10th Nov 2025 | Sahan | read articles on common Java decompilation issues. | 1.0 |
| 11th Nov 2025 | Umesh | Attempted MobSF local server run via python and failed, then began docker setup for MobSF container | 1.5 |
| 12th Nov 2025 | Umesh | Attempted dynamic analyzer configuration in MobSF. Encountered Android Runtime detection errors, emulator connection failures, and ADB remount issues. Verified that emulator was detected by MobSF but system partition was not writable. | 1 |
| 12th Nov 2025 | Umesh | Investigated MobSF dynamic analysis requirement for API level 30-based emulators and created a fresh Android Studio emulator running Android 11 (API 30) to meet the minimum supported version by MobSF. | 0.5 |
| 12th Nov 2025 | Umesh | Attempted to run dynamic analysis again with API 30 emulator, but MobSF reported system partition as read-only. | 1 |
| 12th Nov 2025 | Umesh | Switched to static analysis workflow. Extracted APK files directly from emulator using ADB. Identified package locations, tested multiple extraction commands, and prepared APKs for Strava & Dropbox for MobSF static analysis. | 1 |
| 13th Nov 2025 | Sahan | Practiced identifying exported components using Drozer; tested simple exploitation of exported activities using Drozer commands. | 1.0 |
| 15th Nov 2025 | Sahan | Prepared notes for progress report. | 2.0 |
| 17th Nov 2025 | Umesh | Began analyzing Dropbox data extracted earlier via ADB. Opened the internal SQLite databases using DB Browser and reviewed folder metadata, sync records, and cached file paths. Added additional sample files to Dropbox to generate richer forensic artifacts. | 2.0 |
| 17th Nov 2025 | Umesh | Investigated Strava login failure. Cleared app data, reinstalled APK, modified network settings. OTP verification consistently failed. | 1.5 |
| 18th Nov 2025 | Umesh | Attempted Strava login on both physical phone and emulator. Physical login succeeded briefly, but emulator repeatedly rejected OTP. Captured and reviewed logcat errors. | 1.0 |
| 19th Nov 2025 | Umesh | Re-opened previously extracted Strava databases. Verified presence of personal profile data (height, weight, DOB, city). Determined further data acquisition impossible without account access. | 1.5 |
| 20th Nov 2025 | Umesh | Performed ALEAPP parsing on the entire emulator /data/data directory and analyzed extracted files. Identified SQLite fragments, WAL files, and partial Strava traces. Confirmed most Strava artifacts were incomplete due to failed login. | 1.0 |
| 21st Nov 2025 | Umesh | Created a TAR archive of the emulator’s /data/data folder for consistency. Re-ran ALEAPP on TAR output to ensure full parsing. Final attempt to inject GPX/JSON mock activities into Strava DB; process failed due to app-side verification checks. Officially documented the Strava abandonment decision. | 1.0 |
| 22nd Nov 2025 | Umesh | Conducted static analysis of the Pinterest APK using MobSF. Reviewed permissions, domain configurations, trackers, signature details, and hardcoded secrets. Summarized MobSF findings for report. | 1.5 |
| 24th Nov 2025 | Umesh | Installed Instagram Lite APK on emulator. Created a fresh test account and performed typical user actions (viewing posts, navigating feed) to generate forensic data. Verified app stability compared to original Instagram app. | 1.0 |
| 24th Nov 2025 (Evening) | Umesh | Extracted /data/data/com.instagram.lite using ADB. Prepared folders for ALEAPP ingestion. | 1.0 |
| 25th Nov 2025 | Umesh | Ran ALEAPP on the extracted Instagram Lite folder. Recovered 1402+ cached images and metadata. Exported and validated HTML reports. | 1.5 |
| 25th Nov 2025 (Night) | Umesh | Inspected Instagram Lite’s internal SQLite databases using DB Browser. Confirmed minimal local storage (mostly cache paths and small configuration tables). Documented findings. | 1.0 |
| 27th Nov 2025 | Umesh |Drafted results & insights sections, prepared documentation, and organized screenshots for the report. | 2.0 |
---

**Group:** F25_4440_G7  
**Members:**  
- Umesh Kalupathirannehelage (300389749)  
- Sahan Pattinikuttige Nonis (300389470)

