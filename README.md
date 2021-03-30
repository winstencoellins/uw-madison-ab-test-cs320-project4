# uw-madison-ab-test-cs320-project4
This is a simple A/B Testing homework given by instructor at CS320 (Data Programming II) class at UW - Madison. The basic idea is to test which homepage will attract the most click on the donation link (based on link color) and use that homepage which has the most click so that the homepage could attract more donation. This homework project was built using Flask and HTML. 

## The Actual (Control) Version
![blue_link_donation_image](https://github.com/winstencoellins/uw-madison-ab-test-cs320-project4/blob/main/blue_donation_link.png)

## The Modified (Variation) Version
![red_link_donation_image](https://github.com/winstencoellins/uw-madison-ab-test-cs320-project4/blob/main/red_donation_link.png)

## About the Homepage
The homepage has 2 links: 1) Direct the user to the data being shown in the webpage. 2) Direct the user to the donation link.

## How does it work?
For the first 10 times, the different homepage version will appear by turns every time we hit the refresh page button. For example, if the first display is the blue link donation, the second display will be the red link donation, and so on until 10 times. After 10 times, we determine which donation link has the highest click and keep displaying homepage with donation link color that has the highest click per visit.
