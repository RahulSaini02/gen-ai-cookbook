# Machine Learning

**ML** is the process of `training` a piece of software, called a `model`, to make useful `predictions` or generate content (like text, images, audio, or video) from data.

## Types of ML Systems
ML systems fall into one or more of the following categories based on how they learn to make predictions or generate content:

- Supervised learning
- Unsupervised learning
- Reinforcement learning
- Generative AI

### Supervised learning

Supervised learning models can make predictions after seeing lots of data with the correct answers and then discovering the connections between the elements in the data that produce the correct answers. These ML systems are "supervised" in the sense that a human gives the ML system data with the known correct results.

Supervised machine learning is based on the following core concepts:

- Data
- Model
- Training
- Evaluating
- Inference

Two of the most common use cases for supervised learning are regression and classification.

#### Regression

A regression model predicts a numeric value. For example, a weather model that predicts the amount of rain, in inches or millimeters, is a `regression model`.

See the table below for more examples of regression models:

- **Future house price**	
  - **Inputs:** Square footage, zip code, number of bedrooms and bathrooms, lot size, mortgage interest rate, property tax rate, construction costs, and number of homes for sale in the area.	
  - **Output:** The price of the home.

- **Future ride time**	
  - **Inputs:** Historical traffic conditions (gathered from smartphones, traffic sensors, ride-hailing and other navigation applications), distance from destination, and weather conditions.	
  - **Output:** The time in minutes and seconds to arrive at a destination.

#### Classification

Classification models predict the likelihood that something belongs to a category.

Classification models are divided into two groups: `binary classification` and `multiclass classification`. 

- `Binary classification models` output a value from a class that contains only two values, for example, a model that outputs either `rain` or `no rain`. 
- `Multiclass classification models` output a value from a class that contains more than two values, for example, a model that can output either `rain`, `hail`, `snow`, or `sleet`.

### Unsupervised learning

Unsupervised learning models make predictions by being given data that does not contain any correct answers. An unsupervised learning model's goal is to identify meaningful patterns among the data.

A commonly used unsupervised learning model employs a technique called `clustering`. The model finds data points that demarcate natural groupings.

![Clustering example from 'Introduction to Machine Lerning - Google'](../02-machine-learning/assets/image.png)


### Reinforcement learning

Reinforcement learning models make predictions by getting rewards or penalties based on actions performed within an environment. A reinforcement learning system generates a policy that defines the best strategy for getting the most rewards.

### Generative AI

Generative AI is a class of models that creates content from user input.

Generative AI can take a variety of inputs and create a variety of outputs, like text, images, audio, and video. It can also take and create combinations of these.

Different type of generative models:
- Text-to-text
- Text-to-image
- Text-to-video
- Text-to-code
- Text-to-speech
- Image and text-to-image