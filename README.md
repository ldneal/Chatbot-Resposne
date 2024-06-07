# Chatbot-Resposne
Chatbot Rule Based Response

Rule-based chatbots are structured as a dialog tree and often use regular expressions to match a user's input to human-like responses. The aim is to simulate the back-and-forth of a real-life conversation, often in a specific context, like telling the user what the weather is like outside.

Rule-based chatbots are pretty straightforward. They use a predefined response database and follow set rules to determine appropriate replies. Although they can’t generate answers independently, their effectiveness hinges on the depth of the response database and the efficiency of their rules.

The simplest form of Rule-based Chatbots has one-to-one tables of inputs and their responses. These bots are extremely limited and can only respond to queries if they are an exact match with the inputs defined in their database.Rule-based chatbots are pretty straightforward. They use a predefined response database and follow set rules to determine appropriate replies. Although they can’t generate answers independently, their effectiveness hinges on the depth of the response database and the efficiency of their rules.

The simplest form of Rule-based Chatbots has one-to-one tables of inputs and their responses. These bots are extremely limited and can only respond to queries if they are an exact match with the inputs defined in their database.

The chatbot we are going to develop will be very simple. First we need a corpus that contains lots of information about the sport of tennis. We will develop such a corpus by scraping the Wikipedia article on tennis. Next, we will perform some preprocessing on the corpus and then will divide the corpus into sentences.

When a user enters a query, the query will be converted into vectorized form. All the sentences in the corpus will also be converted into their corresponding vectorized forms. Next, the sentence with the highest cosine similarity with the user input vector will be selected as a response to the user input.

![image](https://github.com/ldneal/Chatbot-Resposne/assets/131946106/9eb83992-6e2b-486c-bab5-ebe40707d12f)
