# Overview

This software is intended as a meal list manager that runs off of a cloud database. Users can add new meals, categorize them by the type of meal, and then edit or add
information that helps to document the meal. I wrote it to familiarize myself with how cloud databases work and how they can be interacted with through python.

[Software Demo Video](http://youtube.link.goes.here)

# Cloud Database

{Describe the cloud database you are using.}
I used firestore through firebase to store the cloud data. It has a simple structure consisting of one collection labeled "meals," that is then filled with documents titled after each meal that has been added to the collection. Each meal document starts with an empty category attribute, and the program allows for more attributes to be added.

# Development Environment

* Visual Studio Code
* Pylance v2022.2.3
* IntelliSense (Pylance) v2022.0.1814523869
* firebase_admin module

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Firebase Documentation](https://firebase.google.com/docs/firestore)
* [W3Schools Python Tutorial](https://www.w3schools.com/python/default.asp)

# Future Work

* More robust input functions for invalid data
* Sorting functionality for custom attributes
* Allow creation of lists as attributes for ingredients or preparation instructions