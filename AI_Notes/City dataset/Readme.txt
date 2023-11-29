										Dataset for AI Algorithm
Table of content
	Introduction
	Dataset Collection
	Processing of data
	Challenges
	Solution
	Contributors
	Reference

Introduction
	While we were studying the classical AI algorithms, our professor Dr. Kushal Shah told that whole world is using just one dataset to teach AI algorithms. Everybody is using just one and only one dataset which is road map of Romania. So, we curated a dataset to study AI algorithms. This data collection is the combined efforts of Batch 2026 and 2027 of Sitare University. This dataset contains widely spreaded and well connected cities of Bharat.

Dataset Collection
	The cities in the data are the birth places of students of Sitare University. The students of 2026 and 2027 batch are asked to enter their cities in a shared excel sheet. Then, duplicate cities were removed while reviewing the data before further processing on it.

Processing of data
	After collection of data there were around 50 cities.Some of cities were not well suited for the structuring of dataset. Since when we plotted cities on the map they were so much congested on the graph and graph was complex to see.As the raw data, there left only 45 cities with no additional information except name. Data has been further processed to add additional information. This has been done with help of following steps:

	For rough idea of graph, we plotted all the cities on the google map to see how it looks like.
	Need to calculate road distance and straight line distance between every two cities. To do this we searched on google for APIs which can make our job easy. Hopefully, we found an API which can do this with high accuracy.
	Now plotted a graph with route distances between any two cities on Paint as well as on a chart with help of an artist.
	Created a csv file to record that how many cities are connected to a particular city.
	Created a script which will give a randomized connected sub graph by dropping some of edges from whole graph.

About DataSet
	We have created a dataset for complete graph and for the simpl implementation of the code we made some changes in representation of the dat in  
	our dataset. Our dataset is of the following type:

		If we have two cities city A and city B then in our data set there will be a row which have (A, B, Route_Distance, Heuristic_distance) as well as a other row for (B, A, Route_Distance, Heuristic_distance).
		Also if we have a city A then our dataset also contains a row (A, A, 0, 0) for simple implementation of code.

Challenges
	Since there was huge data collection so it was very difficult to calculate distance of every city from other cities manually. Furthermore, it was challenging to enter 2025 entries in excel sheets manually.

Solutions
	These challenges were addressed with the help of our programming skills, we used some APIs and wrote our own programs to make work more easy.

Code Example:-
	>>> G = RandomGraph.Graph()          # Created Graph object.
	>>> G.add_nodes(df['nodes'])         # Adding the edges to the graph object.
	>>> G.randomGraphCreater(dropout)    # Creating the random connect graph from the complete graph.
	### Dropout means how much fraction of edges you want to drop from the Graph. 
	### ( Note:- For randomGraphCreater first you should have complete graph in the graph object G.)


Contributors
	Guided By: Dr. Kushal Shah

	Project Leader: Kirtan Khichi

	Content writers: Bharat Suthar and Narayan Jat

	Script writers: Kirtan, Narendra, Shravan, Ranjan.

	Graph drawing: Gajanand and Narendra.

	Team members: Batch 2026 and 2027(data collection)

Reference
	API : https://api.openrouteservice.org/v2/directions/driving-car