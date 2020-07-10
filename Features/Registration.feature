

@sanity @smoke
Feature: Customer search and purchase item from the Application

	Scenario : Verify user logged in and logged out
	Given  User is on Registration Page
	When   User enters username <"Username">
	And    User enters password <"Password">
	And    User clicks on Sign Up Link
	Then   User should log in to the link
	When   User clicks on Sign out link
	Then   User should log out of the website

Examples :
		 |Username|Password|
		 |User 1  |Pass 1  |
		 |User 2  |Pass 2  |
		 |User 3  |Pass 3  |
		 |User 4  |Pass 4  |