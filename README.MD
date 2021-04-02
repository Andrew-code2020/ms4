# Temple Lean Fitness Gym

## Executive Summary 
The Temple Lean Gym website is designed for people .

The membership categories on offer are below ;

1. Online 
2. Student
3. Corporate
4. OAP

The class categories on offer are below ;

1. Kettlebells 
2. Pilates
3. Lean Machine
4. HIIT

The problem that we are trying to solve for the owner are;  
1. Remodel the Temple Lean Business for living with COVID-19

The problem that we are trying to solve for the service user are;
They lack a social support network to encourage them to (gym a social network). 
We set out to bring Temple Lean gym members into a community of their peers . 
The above named membership categories are four strategically valuable markets. They are what people want from a gym. We have designed the website to offer bitesize information on the best gym experience. 
The success of this website is that the user is able to locate the type of class/memebership/coach they want quickly and easily without having to sift through the large amount of information on the web. 

Further success will be measured by the number of Temple Lean members who sign up to the Temple Lean website, create a profile, update their profile and delete a profile they no longer find useful. 
Purchase Membership and classes   

### UX

The key reasons for producing the website were to;

- help current gym members get the best quality coaching from their trusted Health and Fitness professionals at Temple Lean Gym
- help members easily access 4 common memebership categories
- help integrate new and current members into a community where they can
  - support each other on their fitness journey
  - read recipes that others have added to the Temple Lean Recipe website
  - update recipes they have used themselves
  - delete recipes they no longer find useful  
- In the future help Temple Lean Gym attract and retain online subscription members through their website 

At the outset the minimum viable product was determined to be a community platform whereby the operator(s) of the Temple Lean Recipes website add a source of basic information about Temple Lean products and begin to build a social support platform amongst members in a Lifetsyle and Physical Activity context.
It was an objective of this project to include an intuitive design which would allow new and current clients to navigate and engage with the website without any prior experience of Temple Lean the gym facility or even a high level of knowledge about healthy food recipes. 
Current and potential client surveys were conducted to assess the minumim effective information required to illicit a positive emotional response from users.
This information was incredibly valuable during the construction of wireframes for the website. 

At the outset conventional web design features were favoured because we wanted everyone from the novice to the accompolished web user to feel like they were still in a familiar place on the web. 
The vision for the project was to have a website that;

- Delivered basic information that the user could read about Temple Leans online and on site facilities 
- Allow users to add recipes they feel have benefitted them for others to use
- Allow users to modify the recipes they created in case they discover new information about a recipe
- Allow users to delete recipes they created should they feel that they are no longer useful
- Offer a route to find out more about Temple Lean the fitness facility

Further objectives included;
- implementing interactive features on the Temple Lean Recipes website to help the user feel they were unlocking short manageable amounts of information about healthy food recipes.


##### Strategy Plan - Business Strategy

What are you aiming to achieve? 
- Users are looking for; 
  - A place for users to create, read, update and delete their recipes they have found useful and want to share with others. This was based on research on what will help the user/client feel at home in the Temple Lean Recipes community.

Business wants the client to;
- 

Review the competition - Is someone else already doing it?
- A review of the market in Cork Ireland suggested that a platform for members to access recipes within a Health and Fitness Clubs website was a new or under developed idea
- A review of the businesses below showed little or no area for members to find the correct recipe advice from their trusted health and fitness provider
- Businesses reviewed
   - https://www.mardykearena.com/
   - https://www.dennehys.ie/
   - https://www.energiefitness.com/midleton
   - https://onelifefitness.ie/

Stakeholder interviews
- reference SGT studies

Who else is doing this?
- 

What are the pros of what we're offering?
- 
-   

What are the cons?
- 

What are the competition missing?
- The connectivity this area offers
- The software development expertise to carry out this functionality

What are they doing, but they could be doing better?
- They are providing the facility and knowledge to particpate in regular exercise
- They aren't offering direct sign up and online payments

User interviews (What a user thinks they need may not be exactly what they need?)
- Niche wanted marathon programmes
- Majority wanted basic classes and memebership
- The conclusion the developer drew from these interviews was that we should start basic and progress to more advanced recipe recommendations if a clear market or demand emerged. 

Would you use this and why? 
- 
- Clients indicated they would use it because the would finally have vital health resource in place that they knew with information they felt was clear and trustworthy.

Who is our target audience? 
- This project is primarily a consumer business to customer service (B2C) 
- We noted the potential for business to business B2B partnerships later but accepted that this was not within the current scope of the business strategy plan because we need a viable live product before opening discussions with another business.
- Our aim was to access clients we already have but leave the door open for other clients to join us 
- Our thoughts were that our current clients wouldn't need much justifcation to purchase a new offering from us given our existing relationship and the trust we have built up over many years.

What makes a good recipe website experience?
- Following reserach we settled on the points below as a good recipe website experience
  - Intuitive design (Simple Navigation)
  - Clean, attractive layout with point and clicks revealing information slowly in an easy to understand readable format
  - Blog (Users liked to read about recipe experiences or other health and fitness related experiences)
  - Users can create, read, update and delete their own recipes and interact with other members(future development) 
  - Pictures of the finished recipe
  - Videos (This was placed in future development plans)
  - Pricing transparent (3 step purchase - This was placed in future development plans) 


## Scope Plane 
Features we wanted to include in our design

- Colour light background generally white then strong font and color
- Basic Observations
   - Navbar 
    - Two tiers
   - Includes Navigation for following items
    -
   - Rating (Opportunity to Card Flip js)
   - Register/Login (Right and collapsible) then reveals, profile and log out and recipe navbar

- Section
  - Home/Landing Page Body (Hero image photo options))
  - CRUD Functionality to be available in 
    - Profile
    - Breakfast 
    - Lunch 
    - Dinner 
    - Snacks

Cards with Photo Gallery
  - Homepage
  - Profile
  - Breakfast 
  - Lunch 
  - Dinner 
  - Snacks

Card flip - Testimonials

Footer    
 - Social Media Icons wired up Facebook. Instagram, Twitter(developers social media) (Left) 
 - Gap in Center
 - Blog entries (Right)

Data Schema - Database Mongo DB

Collections

User information
- Object Id
- Username
- Name
- Email 
- Password Werkzeug 

Lean Recipes
- Object Id
- Meal Type
- Meal Name
- Meal Image
- Instructions 
- Ingredients
- Method
- Required Tools
- Nutritional information (Format opportunity to display creativity - Traffic light healthy range of macronutrients)
  - Kcals
  - Carbs
  - Protein
  - Fats

Recipe types or Categories
- Object Id
- Breakfast 
- Lunch 
- Dinner 
- Snacks


### User Story 1 (Creating and reading a profile - Registeration)

I am a currently a member of Temple Lean Gym. Following a conversation with a friend about diet and exercise my friend recommends that I check out a new website named "Temple Lean Recipes". I search the web find the Temple Lean Recipes website. 
I register and I click on the option 'Dinner' because I have always had trouble cooking healthy dinner recipes. I click on a recipe I am interested in through the collapsible buttons on the page and the collapsible feature reveals information in a
step wise manner that allows me to learn what I need to know about how to make the recipe as well as other information.

### User Story 2 (Editing my profile)

I have registered for Temple Lean Recipes. My email provider has decided to charge me a monthly fee to continue using my email address. I have gone ahead and changed to a new email provider. I want to update my email on the Temple Lean Recipes Website. I log in to the Temple Lean Website. I am brought directly to my profile page. I click on the update profile button. I make my updates to the email section and then click the update profile button. The screen flashes a message updated successfully. I can also see the updates rendered on the form in front of me. I then click profile on the top right of the screen to bring me back to my profile page where I can also review the update I have made.

### User Story 2B (Delete profile)
I wish to leave the Temple Lean Recipes community. I log in and go to the profile I created in User Story 1 on the Temple Lean Recipes website. On the profile page that I see the Delete Profile button. I click the button and I receive a flash message on the screen telling me my profile has been deleted. I am automatically logged out when I delete my profile. 

### User Story 3 (Creating and Reading Recipes)

I am registered and logged in at the Temple Lean Recipes page. I use a recipe that I wish to add to the community. I click create recipe on any recipe page. I am brought to the add recipe form. I select the category (Breakfast, Lunch, Dinner or Snacks). I fill in the rest of the form. When I click the create recipe button I see a flash message stating "Recipe Created Successfully!". I am redirected to my profile where I click on the appropriate category and I scroll down to see the recipe I created and the information I input on the form earlier on the screen. 


### User Story 3A (Update Recipes)
I spot an error in the recipe I created (from User Story 3) so I click update recipe. I notice that I can only update the recipes I have created but not any other recipes. I make my edits I need to make in the form hit update recipe and then review my updates as before on the relevant page.

### User Story 3B (Delete Recipes)
A recipe I created a while ago has stopped being useful to me and the Temple Lean Recipes community. I log into the Temple Lean recipes website. I scroll to the Recipe I created earlier click the Delete Recipe button. I receive a flash message on the screen telling me the recipe has been deleted. 

### User Story 4 (Log out)

I am logged into the Temple Lean Recipes page. I have found the recipe I wanted and made the recipe using the Temple Lean Recipes site as a reference. I click on the log out button to log out. I receive a flash message stating that I have been logged out and I am redirected to the log in page. The recipe pages disappear and I am unable to access them until I log in again.

## Structure Plane
In development we set out to make sure that our site would be consistent. We used the categories below to describe our efforts
 - Predictable
   - To make the website predictable we used the same materialize cards and collapsibles for Breakfast, Lunch, Dinner and Snacks
   - We used similar forms to register, to log in, create profile information, create recipe information, update profile information and update recipe information.  
 - Learnable
   - We used collapsible to reveal information slowly to the user
   - We repeated the collapsible to make the website easily learnable no matter what recipe page we are on
   - Flash messages tell the user that have successfully complete a task or entered any invalid information 
 - Visible 
   - A user can easily review updates they have made on the site immediately after they have been made
 - Clear and intuitive feedback
   - Flash messages give clear and intuituve feedback to the user
   - Collapsibles reveal and close off information with one click

### User Questions

- Where am I?
  - On each page the Navbar highlights text in light blue of the relevant page. This helps you locate where you are on the Temple Lean Recipes site

- How did I get here?
  - Clicking on certain icons or words opens up new tabs to a specific external site so the user does not forget which website they accessed the content from such as social media platforms and the monthly blog links. The platforms are currently connected to the developers social media accounts and private website because the social media accounts for this website do not exist 
  - The navbar and footer are the exact same on each page and with the current page highlighted in light blue in the navbar so that the user may easily identify where they are on the Temple Lean website
  
- What can I do here?
  - The user is invited clearly to click on and then access various features of the Temple Lean Recipes website. 
  - This occurs in the following places;
     - Navbar with the hover feature
     - Footer via the social media icons (Hover feature turns them light blue when the cursor is over the icons)
     - The Create, Update and Delete buttons
     - On click the collapsible feature reveals basic information 
     - The user is also invited to type information on forms throughout the site

- Where can I go from here?
  - The navbar and footer are the exact same on each page. In the navbar the user is able to easily identify where they are using the light blue active feature and where they can go from here is not highlighted letting the user know that they can go here if they wish. 
  - Buttons also tell the user intuitively where they can go from here ie update profile or create recipe
  - The blue hover feature is also designed to indicate to the user that they can click on this icon in the footer and access further content.
  - On the home page in the cards (under the main hero image) the Log In and Register Page buttons invite the user to click on them and log in or register.
 

### Skeleton Plane

Wireframe Pictures 

Desktop wireframes

- readmedocs/desktopwireframe/basetemplate.jpg
- readmedocs/desktopwireframe/landingpage.jpg
- readmedocs/desktopwireframe/loginpage.jpg
- readmedocs/desktopwireframe/paintlandingpage.jpg
- readmedocs/desktopwireframe/recipelooppage.jpg
- readmedocs/desktopwireframe/registerpage.jpg
- readmedocs/desktopwireframe/recipespageoutline.jpg

Mobile/Tablet Device wireframe
- readmedocs/mobilewireframe/recipeloopmobile.jpg
- readmedocs/mobilewireframe/loginmobile.jpg
- readmedocs/mobilewireframe/profilemobile.jpg
- readmedocs/mobilewireframe/registertemplatemobile.jpg
- readmedocs/mobilewireframe/editrecipemobile.jpg

### Features

##### Summary

- Internal links
- External links
- Header
- Navbar
- Footer
- Section
- Form Select
- Collapsible
- Hover
- Flask
- Integrated with MongoDB
- Icons
- Jquery 
    - Collapsible
    - Sidenav 
    - Form Select



##### Existing Features

- Internal links to different parts of the Temple Lean Recipes website
- External links that open different platforms such as social media, the developers Milestone 1 project website and the developers private blog. The social media accounts, the developers Milestone 1 project website and the developers private blog are linked to this project to demonstrate the skill of adding external links.
- Header - Contains the Navbar design for desktop and mobile devices 
- Easy navigation - The Navbar at the top of each page is similar to conventional navbars of other recipe pages allowing the user an intuitive experience on a perhaps unfamiliar website. We maintained this navbar across each page using a base template for ease of navigation and coding. The top part of the navbar including log in and registeration collapse on a mobile device to a single apple icon which the user can click on. The navbar items Breakfast, Lunch, Dinner and Snacks appear after you register or log in. This was done to avoid overhwleming the user when they land on the page and guide them to log in or register and then more content will be revealed. 
- Footer - Linked to some pages we used to develop the website and contains direct links to the developers Social Media platforms, Milestone 1 project and private blog. Temple Lean recipes social media specific to this site does not exist but is in future plans.
- Section - The middle section is where the block content Jinja template is injected. The content changes on each page and gives basic information on aspects of the Temple Lean Recipes site.
- Hero Image - The eye catching landing/homepage page is designed to convey to the user that they have arrived on a Temple Lean Recipes site as distinct from the gym site. 
- Select - We used select options to allow a better visual experience for the user and to avoid long typed responses on the forms through out the website. 
- Hover 
   - social media icons all turn blue when the cursor hovers over them
   - internal links turn light black when the cursor hovers over them except for the homepage. 
   - external links do not have a hover
   - The hover lets the user know that there is more information they can access here if they click. It draws attention to options which keep the user on the Temple Lean Recipe page. 
- Icons - font awesome icons were used to add style and an intuitive feel to the user experience. 
- jQuery & JavaScript 
    - Collapsible - On each recipes page clicking the on the Ingredients, Method, Tools or Nutitrional Information will open the collapsible revealing more content  
    - Sidenav - On Mobile devices the Navbar containing Login, Register and Logout collapses to an apple icon which the user can click on to access
    - Form Select - Forms are used throughout the page to allow users to register, login, update profiles, create recipes and update recipes. The select option is used to avoid long form answers and allow users to progress through the website quickly
- CRUD Functionality
    - Create - Users can create a profile and create recipes on the Temple Lean Recipe website
    - Read - Logged in users can read recipes and their profile information on the Temple Lean Recipe site 
    - Update - Logged in users can update recipes they created and their profile information only on the Temple Lean Recipes site
    - Delete - Logged in users can delete recipes they created and their profile information only on the Temple Lean Recipes site


##### Features Left to Implement
- Search function
- Automatic image upload and rendering to the website
- Book and pay for a private Nutrition Consultation
- Analytics that show user traffic flow
- Testimonials from Users
- Members Subscription
- Password update & reset your password function
- Forgot password feature
- Recipe Videos
- E-Commerce subscription Business Model 
- Comments so users can interact with other users


### Technologies Used

- HTML5 - Used for structure and content of website
- CSS3 - Used for personalised custom built styling of website
- JavaScript 
   - Used for 
    - Collapsible   
    - Sidenav
    - Form Select 
- jQuery 
    - Used to configure interactive features above 
    - Website https://jquery.com/
- Bootstrap
  - Website https://getbootstrap.com/
  - Used to import generic styling for the entire website
- Github and Gitpod
  - Website of Github repository https://github.com/Andrew-code2020/ms3onlinecookbook
  - Used to construct host and deploy the website
- Font Awesome
  - Website https://fontawesome.com/
  - Used to import icons
- Google Font
  - Website https://fonts.google.com/
  - Used to import font
 
- Python https://www.python.org/
  - Used to created roots,view and integrate with flask to deliver functionality to the website 

- Heroku https://www.heroku.com/  
  - Used to deploy the website
  - Website link to the deployed Heroku app https://lean-temple-recipes.herokuapp.com/ 
  
- Dependencies (Also listed in requirements.txt file)
  - click==7.1.2
  - dnspython==2.0.0
  - Flask==1.1.2
  - Flask-PyMongo==2.3.0
  - itsdangerous==1.1.0
  - pymongo==3.11.1
  - Werkzeug==1.0.1


### Testing

- We carried out the procedures below to test the Temple Lean Recipe Website

- Name of Test CRUD Unique to User who created recipe 
- Outline of Testing
  - Check that different users could create recipes but they could update or delete recipes they created
- Test planning
  - Used two profiles and created recipes with them
- Implementation
  - We created recipes on mutliple profiles and reviewed which options came up for each user
- Fix (if applicable)
  - first we did have a created_by in our python views so our created recipes intially belonged to no one
  - we corrected this by adding created_by in our python roots and then manually adding the created_by variable and value to MongoDB
  - We assigned the variable to the admin or the developers user profile
- Results
  - We reached a point where admin profile had created half the recipes on the website and could update and delete them
  - The other half were created and could be update or deleted by the developer who created a user in his own name
- Outcomes
  - Because we updated our root newly created recipes did not need us to intervene on MongoDB to assign a created_by instead the creator of the recipe was the only one who could modify that recipe
  - This was verified by getting the developers girlfriend to add a recipe on her profile

- Name of Test JS File
- Outline of Testing
  - The objective of the test was to check if the directory to the js file was working 
- Test planning
  - Input code into recipe.js and check the developer tools specifically the console tab to check if the js file is rendering effects across the Temple Lean Recipes website  
- Implementation
  - In the recipe.js file we input the code console.log('linked properly');
- Fix (if applicable)
  - A fix was not necessary because the code worked 
- Results
  - The results are available to view 
  - readmedocs/testing/jsfiletest/jsfiletestresult.jpg
- Outcomes
  - Test successful. the words 'linked properly' appeared into console


- Name of Test - JS file functionality
- Outline of Testing
  - Check that js code is producing functionality on the Temple Lean Recipe Website
- Test planning
  - Check the following js functionality
  - Collapsible - On each recipes page clicking the on the Ingredients, Method, Tools or Nutritional Information will open the collapsible revealing more content. Does this happen?  
  - Sidenav - On Mobile devices the Navbar containing Login, Register and Logout collapses to an apple icon. Does this happen?
  - Form Select - The form select option is used across the site does the menu work and the options appear. Does this happen? 
- Implementation
  - Collapsible
    - collapsible class added to brekfast, lunch, dinner and snacks html pages
    - pertinent initialisation code added to recipe.js
  - Sidenav
    - pertinent initialisation code added to recipe.js
    - check nav elements collapse to an apple on the right on Mobile device
    - Open deployed site https://lean-temple-recipes.herokuapp.com/
    - Ctrl+Shift+I on the keyboard
    - Select mobile device from responsive dropdown menu
    - Click apple icon
    - Check nav items are there 
  - Form Select
    - Open deployed site https://lean-temple-recipes.herokuapp.com/
    - Go to the Register page
    - Check the Preferred Recipe Category
    - Click the dropdown carrot
    - See if options come up
    - Check Form Select occurs on all other forms in the website
- Fix (if applicable)
  - Collapsible
    - no fix neccessary
    - code was copied and extended to add more collapsible sections on the page which also worked
  -Form Select
   - We added disabled and selected attributes to ensure the register form was blank at first
   - We added the relevant value ie value = "breakfast" into the html template to each option to ensure the that the option was passed and documented in MongoDB. 
  - Sidenav
    - To render the sidenav bar on the right of the page we added {edge: "right"} to the js code

- Results
  - Collapsible
    - Breakfast result image start readmedocs/testing/jsfiletest/jscollapsibleresult1.jpg
    - Click on Collapsible result image start readmedocs/testing/jsfiletest/jscollapsibleresult2.jpg  
 - Sidenav
   - Sidenav result image readmedocs/testing/jsfiletest/jssidenavresult1.jpg
   - Clicked through sidenav apple readmedocs/testing/jsfiletest/jssidenavresult2.jpg
 - Form Select   
   - Register page results readmedocs/testing/jsfiletest/jsselectformresult.jpg
   - Edit profile page resultss readmedocs/testing/jsfiletest/jsselectformresult.jpg
   - Edit recipe page results readmedocs/testing/jsfiletest/jsselectformupdatereciperesult.jpg
- Outcomes
   - Form Select
     - The tests lead to bug fixes and helped ad functionality without errors on the site
   - Collapsible
     - Checked collapsible  across breakfast, lunch, dinner and snacks and it worked
   - Sidenav
     - Side nav functionality worked and revealed sidenav elements



### Performance Testing Lighthouse 
- Name of Test 
  - Lighthouse Test
- Test planning 
  - Check the Temple Lean site for performance, best practices and accessibility. 
- Implementation
  - access the deployed site via https://lean-temple-recipes.herokuapp.com/
  - Use Ctrl+Shift+I on your keyboard to access the developer tools
  - Click genereate report refer to image for visual detail 
  - Sample result image readmedocs/testing/lighthouse/generatereportlighthouse.jpg
- Fix (if applicable)
  - no obvious performance issues on mobile or desktop device according to the lighthouse tests
- Results
  - The lighthouse test results are documented in the images below 
    - readmedocs/testing/lighthouse/mobilelighthousetest.jpg
    - readmedocs/testing/lighthouse/desktoplighthouseresults.jpg
- Outcomes
  - performance was optimum

### Performance Testing CSS
- Test planning 
    - Premise is our custom css file talks to our html files through python 
- Implementation
    - At the beginning of the project we checked to see if the background color red appeared when we added background color red to style.css
- Fix (if applicable)
    - not applicable code worked
- Results
  - readmedocs/testing/cssfiletest/testinglinkbetweenbasetemplateandcustomcss.jpg
- Outcomes
  - test was successful

### Performance Testing Python Initial functionality 
- Subject Test app.py inital ran 
   - used python3 app.py to run the app.py file from gitpod
   - screenshots in readmedocs/testing/pythontestfile/initialapppyrun.jpg
- Result
   - Hello World of Temple Lean Again appeared in the browser as expected
- Conclusion
  - initial set up worked well

 Testing 
- Test
   - Registeration form check the content renders on our app 
- Implementation
   -used python3 app.py to run the app.py file from gitpod to visualise our registeration file
- Fix (if applicable)
    - icons render on top of label text
    - to fix we placed the icons within the label element
- Results
  - visually the icon and the label are no longer over lapping
- Outcomes
  - Fixed a visual bug

### Testing Browser Screens

### Chrome Browser
- I tested the website by copying and pasting the Heroku pages link https://lean-temple-recipes.herokuapp.com/ into the Chrome Browsers
- I pressed control+shift+I to access developer tools in the Chrome Browser and checked the web pages responsiveness
- There were no obvious bugs in the chrome browser on desktop or mobile views within this browser

### Edge Browser
- I tested the website by copying and pasting the Heroku pages link https://lean-temple-recipes.herokuapp.com/ into Edge Browser
- I pressed control+shift+I to access developer tools in the Edge Browser and checked the web pages responsiveness
- There were no obvious bugs in the chrome browser on desktop or mobile views within this browser

### Testing Device screens
- I used the chrome developer tools to test that the websites appearance and functionality was available across multiple devices listed below;
  - Moto G4
  - Galaxy S5
  - Pixel 2
  - Pixel 2 XL
  - iPhone 5/SE
  - iPhone 6/7/8
  - iPhone 6/7/8 Plus
  - iPhone X
  - iPad
  - iPad Pro
- I checked the console in developer tools showed no errors on each page as I went through each page of the Temple Lean Recipes site

### Header and Footer

- Across each page of the website you may verify that the Header and the Footer have the same features outlined below in the Testing Navbar and Testing Footer sections

### Testing Navbar

- Go to the Temple Lean Recipes "Home/Landing" page or any other Temple Lean Recipes page
- Click on Log In or Register
- On the Log In or Register page the text and icon will take on a light blue background so the user will know where they are on the Temple Lean Recipes Website
- Verify that when the user clicks on the Log In or Register active feature highlights in light blue occurs when the user is on either page
- Verify that the forms to allow a user to log in or register appear
- When you have logged in or registered verify that the secondary navbar containing the Breakfast, Lunch, Dinner & Snacks appear
- Verify that when the user clicks on Breakfast, Lunch, Dinner & Snacks active feature highlights the text in light blue when the user is on any of the pages

### Testing Footer
 - Go to the Temple Lean Recipes "Home/Landing" page or any other Temple Lean Recipes page
 - Verify that clicking the links to the blog open in a new tab
 - Verify that clicking on the social media icons open the correct social media page in a new tab


### Testing Section

- The section element changes it's content depending on which page you are on
- Below I have outlined briefly the testing on each section

### Testing Home/Landing page

- Go to the "Home" page by clicking on the words Temple Lean Recipes
- Verify that the page with the salad bowl appears with a welcome message and log in and registeration buttons
- Verify that clicking the buttons connect to the correct internal page

#### Testing Log In

- Go to the "Log in" page by clicking on the Log In icon
- Verify that when you hover over Log In a light black background appears inviting the user to click on Log In   
- Click on Log In verify the log in page appears. 
- Verify that the Log In text and icon appears with a light blue background to help users determine where they are on the Temple Lean Website
- Fill in the log in form
- Verify that you can log into the site or that the flash messages appears if you enter invalid or non existing log in information
- Verify that when you log in you are directed to your profile page 
  

#### Testing Registeration page

- Go to the "Registeration" page by clicking on the Register icon
- Verify that when you hover over Register a light black background appears inviting the user to click on Log In   
- Click on Register verify the registeration page appears. 
- Verify that when you are on the Register page that the Register text and icon appears with a light blue background to help users determine where they are on the Temple Lean Recipes Website
- Fill in the Registeration form
- Verify that you can Register with the site and that the flash messages appears when you finish registeration and you are redirected to your newly created profile page


#### Testing Profile page including CRUD functionality

- Log into the Temple Lean Recipe page 
- Verify that when you are logged your profile page appears on the screen    
- Verify that when you are on the Profile page that the icon and text appear with a light blue background to help users determine where they are on the Temple Lean Recipes Website  
- Verify that you can update the profile and that the update renders on the profile page
- Verify that you receive a flash messages telling you that you have completed the update successfully and are redirected to your newly updated edit profile page
- Verify that you can delete the profile and that you are automatically logged out with a flash message telling that your profile is deleted whilst you are redirected to the registeration page


#### Testing Breakfast, Lunch, Dinner & Snacks page including CRUD functionality

- Log into the Temple Lean Recipe page 
- Verify that when you are you logged into the Temple Lean Recipes site that the Breakfast, Lunch, Dinner & Snacks pages appear in the secondary navbar.
- Verify that this Navbar adjusts on a mobile device to become smaller but the words and the ability to click on the Breakfast, Lunch, Dinner & Snacks pages remains possible    
- Verify that when you are on the Breakfast, Lunch, Dinner or Snacks pages that the text appears with a light blue background to help users determine where they are on the Temple Lean Recipes Website  
- Verify that you can create a recipe on the Breakfast, Lunch, Dinner or Snacks pages by pressing the create recipe button and that the recipe information appears in the relevant section of the Temple Lean Recipe website. (The image url will need to be adjusted from the back end to render on the Temple Lean Recipe site. The Temple Lean Admin will do this until in future development it is possible for the user to upload an image directly)
- Verify that when you create a recipe on the Breakfast, Lunch, Dinner or Snacks pages that a flash appears telling you that the recipe has been added successfully and that you are redirected to your profile page.
- Verify that the recipe has been added to the bottom of the relevant recipe category page
- Verify that the alt image notice appears if your image link has not rendered successfully
- Verify later that the admin managing the site has added an appropriate image from the back end database MongoDB.
- Verify that you can receive a flash message telling you that you have completed the update successfully and are redirected to your profile page.
   - We redirected the user to the profile page to avoid creating seperate addrecipe roots in python that redirected users back to each individual recipe page.
   - The profile page was deemed an acceptable compromise as it also has quick links to the recipe pages so the user can easily verify within 3 clicks if their recipe has been created successfully.
- Once you have created a recipe verify that the following green buttons appear Update Recipe and Delete Recipe. Only the user who created the recipe may update or delete a recipe from the Temple Lean Website. The admin of the site may delete a recipe from MongoDB.
- In a recipe you created verify that you can click the update recipe button and that you are taken to the edit recipe form. Make edits to the section you wish to edit. Click update recipe when you have completed your edits.
- Verify that a flash message appears telling you that you have updated the recipe successfully and that you are again redirected to the profile page.
   - We redirected the user to the profile page to avoid creating seperate editrecipe roots in python that redirected users back to each individual recipe page.
   - The profile page was deemed an acceptable compromise as it also has quick links to the recipe pages so the user can easily verify within 3 clicks if their recipe has been updated successfully.
- In a recipe you created verify that you can delete the recipe by pressing the delete button. A flash message will appear on the profile page telling the user that they have deleted the recipe successfully. 
   - We redirected the user to the profile page to avoid creating seperate deleterecipe roots in python that redirected users back to each individual recipe page.
   - The profile page was deemed an acceptable compromise as it also has quick links to the recipe pages so the user can easily verify within 3 clicks that their recipe has been deleted successfully. 

#### Testing Log Out functionality

- Log into the Temple Lean Recipes page 
- Verify that when you are on your any page that the log out ability is available on the top right in the desktop and through the apple icon on a mobile device   
- Click the log out button
- Verify that you receive a flash message telling you that you have logged out are redirected to the log in page


### Code Validators
I used the following code validators to help me debug my code 
 - HTML - https://validator.w3.org/
 - CSS Validator - https://jigsaw.w3.org/css-validator/#validate_by_input
    - Result visible in readmedocs/testing/codevalidators/cssvalidatorresult.jpg
 - JavaScript and JQuery validator https://jshint.com/
    - Result visible in  readmedocs/testing/codevalidators/shintcheckresult.jpg
 - Python Validator http://pep8online.com/
    - Result visible readmedocs/testing/codevalidators/pep8vaildatorresult.jpg

I also used following website to help me correct any formatting anomalies in my code
- https://codebeautify.org/ 

I also used Shift+alt+F on my laptop to beautify each page of code in gitpod

#### Bugs

Bug - images set to 250 px
taregtting css classes .card-img, .card-img-top with height 250 px would not render. Targeting the img element did. Did have to change some images as the looked stretched 

Bug - Directory Structure wrong in Facilities app
- facilities on top of template instead of template on top of facilities

Bug - Visual- Pictures 
- Button primary class overwriting hover
- Home page Picture not rendering quite as effectively on the screen 

Bugs - input data postgres to sqlite

Bugs - css for home button changed nav and footer so bottom css was not working at all

Bugs - data delay into Toast Header div and not container div

Bugs - bag tools in checkout template or template error showed. Forgot to add bag tools at the top

Bugs - checkout app missing div caused footer to loose the outer edge of it's blue. inserted code into validator and found missing div

Bugs - countries field navigate through model and forms removed the label. Changing the css height in StripeElement,
.stripe-style-input to 60 px resolved the image problem

### Deployment

#### Set up the Repository 

- Project Repository on Github
  - This project is hosted in a github repository. 
  - The project was developed using a Gitpod workspace. 
  - Link to the repository https://github.com/Andrew-code2020/ms3onlinecookbook


#### Creating the repository

- To create the project in my github repository I went to the code institute recommended repository via this link https://github.com/Code-Institute-Org/gitpod-full-template
- We copied the code institute template
- The screenshots of this process are available by following the directories below
    - readmedocs/creatingrepo/creatingsitetemplate/step1copyrepotemplate.png
    - readmedocs/creatingrepo/creatingsitetemplate/step2creatingreponame.png
- Finally we cloned the repository from the developers milestone project 2 using the instructions on the following website https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository

#### Deploying the project to Heroku

- To deploy the project the developer went into Gitpod 
- The developer followed the steps outlined the code institute video available by following this link https://www.youtube.com/watch?v=YfQIUSuPm2w&feature=youtu.be
- The screenshots of this process are available by following the directories below;
    - readmedocs/deploytheproject/deployonheroku/deploymenttoheroku1.jpg
    - readmedocs/deploytheproject/deployonheroku/deploymenttoheroku2.jpg
    - readmedocs/deploytheproject/deployonheroku/deploymenttoheroku3.jpg
    - readmedocs/deploytheproject/deployonheroku/deploymenttoheroku4.jpg
    - readmedocs/deploytheproject/deployonheroku/deploymenttoheroku5.jpg
    - readmedocs/deploytheproject/deployonheroku/deploymenttoheroku6.jpg
    - readmedocs/deploytheproject/deployonheroku/deploymenttoheroku7.jpg
    - readmedocs/deploytheproject/deployonheroku/deploymenttoheroku8.jpg
- The live Temple Lean Recipes site may be accessed by following this link https://lean-temple-recipes.herokuapp.com/


### Credits

- I consulted the folowing websites to learn about Recipe Websites and to help construct meaningful content for the Temple Lean Recipes site
   - Recipe Websites
     -  

- I consulted the following websites for inspiration and to learn how to implement certain features into my project;
    - https://stackoverflow.com/
        - Features influenced
        - Active class in navbar 
        - height of images
    - https://www.w3schools.com/default.asp
         - Features influenced
            - Border
            - Hover
            - Overflow
            - Card custom css
- I used Materialize through out the project to deploy a mobile first design principle.
  - Website https://materializecss.com/
  - Features influenced
    - Navbar
    - Header
    - Footer
    - Section
    - Navbar
    - Forms
    - Select Option
    - Buttons
    - Cards
    - Collapsible

- Google Fonts 
  - I imported the text font Recursive from Google Fonts website https://fonts.google.com/
  - I used this font because it was the same font as other recipe websites and therefore made my website feel familiar and readable to users

- I copied the hero image idea in a similar way to the Jumbtron idea from our code along whiskey drop project with the code institute. I copied a Materialize card code to mimic a jumbotron. 
  - Reference to Github repository from code along project https://andrew-code2020.github.io/whiskeydrop/

- I copied the icons from Font awesome https://fontawesome.com/ and used the CDN to implement them in the project. I then wrote custom css code to style the icons and make them more responsive. I did not use the materialize icons because they did not look as good as the font awesome icons.

- I reviewed the lessons on jQuery in the Interactive Front Development Module to help me implement the features in this project. 

- I frequently referred back to the following code institute modules to research how to construct certain features

  - HTML Fundamentals
  - CSS Fundamentals
  - User Centric Front End Development
  - JavaScript Fundamentals
  - Interactive Front End Development
  - Python Fundamentals
  - Practical Python
  - Data Centric Development Milestone Project 
  - Full Stack Frameworks with Django 

- I copied the knowledge of how to implement Materialize CDN and Font awesome CDN links from my mini project during the data centric development. Link to mini project https://github.com/Andrew-code2020/datacentricminiproject
 

##### Content

- The content was constructed by the student with inspiration from their experience as a Health and Fitness professional for the past 10 years. 
-   

##### Media

- The photos used in this site were obtained from pexels.com and https://unsplash.com/
  - These photos are placed in the website on the following pages;
    - Home page
    - Registeration page
    - Breakfast page
    - Lunch page
    - Dinner page
    - Snacks page


##### Acknowledgements

- I received inspiration for this project from the Code Institute Tutorial videos and my mentor Mr. Adegbenga Adeye.
- I would also like thank the following members of the Tutor Team Tim Nelson, Anna, Xavier, Igor, Miklos, Cormac, Kevin, Johann, Samantha and Haley (apologies that I could not find all your surnames). I spent many hours trying to work through problems I encountered with them.