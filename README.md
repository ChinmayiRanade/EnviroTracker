# EnviroTracker
Inspiration: Given the recent rise in climate change, I wanted some sort of tracker to really show people just how much they are contributing to the environment; to raise awareness, and to take the proper steps to mitigate the negative effects for the future.

What it does: It basically takes random values uniformly distributed between 5 and 25 kWh for electricity consumption, and 10 and 25 cubic feet for gas. It emulates real-life values. Then these values are put through the pandas DataFrame in separate variables and then used to get the sum and average for each of them (accessed the values from the data dictionary). The values are taken and put through Matplotlib to generate a graph showing the consumption of each. The averages go through two conditional statements and give the user a message: "Your electricity consumption is high. Consider energy-efficient products like solar chargers." or "Your gas consumption is high. Check for any gas leaks to optimize usage. Explore gas-saving products" if any of them go over a certain threshold (I just chose 15 and 20 respectively).

How I built it: Using VS Code.

Challenges I ran into: I was not able to implement API data into the dictionary of data instead of the random data, hence why I used randomly generated data as a means to emulate actual data.

What I learned: Matplotlib was easy to use, and I learned to experiment with its features.

What's next for EnviroTracker is implementing real-life data from an open-source API like the one from eia.gov. Through this people will actually get a clear idea of electricity and gas consumption. Also, I would like to implement other data such as data for natural gas emissions, for example. This way it will be more comprehensive and the data should not be limited to a specific sector; it should also give data by the time period (annually, monthly, etc.), by location (state, residential, commercial, etc.), and even be able to implement links that can take you to product alternatives to reduce reliance on traditional sources of electricity to solar chargers, for example. Sort of like a user-friendly interface, that can be implemented using Flask for apps and Tkinter for desktop apps.
