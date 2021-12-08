# Milestone 4 

## Task 1 Weights and Biases

**What is Experiment Management and why is it important?**

An experiment in machine learning provide the possibility to test which model can work best for the task at hand. For this reason we might adjust the model applied and the paramaters to observe how it affect our selected metric.  
Experiment Management is the combination of processes to manage and organize models. It helps to keep track of the changes in models, parameters and dataset. The main idea behind is that, especially if we run more than a single experiment, a dedicated solution to track changes is necessary. This enable the developper to compare overtime the performance of different models, keep track of the parameters by aggreagting and visualize those information.
In our example we use Weights and Biases, a solution that allows to log directly weights and biases for free, with a combined visualization of the results of the models. 
Together with the logging functionality described, it provides tools to manage different runs ( like filter,group, sort), the possibility to reproduce pictures (and other rich media types) directly in the UI. 
In addition, it also provide information regarding the system req  uirment of each run (cpu, RAM etc.), which can be useful to identify bottlenecks or if we are trying to optimize perfomance over accuracy. An example could be algorithms that serve webpages recommendation, where it is important to provide a result in the time of milliseconds. 
In addition, with Weights and Biases all files are automatically stored, including our model.
These functionalities allow not only to collaborate more efficiently but also to show to potential customers the improvment of a certain model overtime. 

**What is a Metric in ML?**

A Metric is a way to evaluate the performance of a machine learning algorithm. We can select one or multiple metrics to summarize the outcome of a model. The first question we need to adress is if the machine learning algorithm we are creating is for a regression or classification problem. Of course there are different problems, but if we take the example the regression problems popular metrics include the MSE (Mean Squared Error) and the MAE (Mean Absolute Error). For our example, a classification problem, the main metrics are the accuracy, the precision, the recall, the F1 score, ROC (Receiver Operator Characteristic )/ AUC (Area Under the Curve). 
Because all the other metrics are part of further questions, I will start by describing the accuracy. It is the ratio of number of correct predictions to the total number of input samples. 
By itself it may be misleading to judge a ML algorithm based on precision alone. As an example, if we have an imbalanced dataset we might assess that the model is very precise based on the accuracy alone.

**What is Precision and Recall? Why is there often a Trade-off between them?**
One of the metric in the classification models we mentioned before is the accuracy. However, it is not enough to only evaluate accuracy, as it can often be misleading. 
A better approach is to calculate precision and recall. THe precision is the sum of the true positives, divided by the sum of true and false positives. A true positive is when the model predicted "A" and the actual output in the classification is "A". A false positive is when the model predicted "A" and the actual output was "B". The metric will therefore provide an evaluation of the quality of positive prediction made by the model. 
On the other hand Recall is calculated as the sum of the true positives, divided by the sum of true positives and false negative. A false negative, in our little example, would be when the model predicted "B" and the actual output was "A". 
Recall is also known as sensitivity and it can tell how our model is capable (or not) in reducing the number of false negatives. 
Because both recall and precision are important to evaluate a classification model, a third metric has been created, which is derived from Precision and Recall. This metric is called F1 score and it is the harmonic mean between precision and recall. This provide a single metric, where the higher the score (F1 score), the better the model performs.
In fact, if we isolate the metrics and we take in consideration for example only the precision, we might have a model with a very high precision score. This would indicate that the classifier is precise, but if the recall is low the model would then miss to identify a large number of instances. 

**What is AUROC Metric?**

However, Precision and Recall are not the only metric we can utilize to evaluate a classification model. Another popular metric is the AUROC (Area Under the Receiver Operating Characteristics). 
This combine the aformentioned recall (also known as sensitivity) and the false positive rate (also known as fall-out). The false positive rate is defined by the sum of false positive divided by the sum of false positive + true negatives. This metric corresponds to the proportion of false positive that are mistakenly considered as positive. To combine the true metrics (Recall and false positive rate) different treshold are calculated for the logistic regression.  The resulting curve is called ROC curve and the metric we take in consideration is then the AU (Area Under of the curve). 
The AUROC have values between 0 and 1. If we have a model with AUROC is perfect (or at least the metric to measure the performance is) and a value of 0.5 would indicate a base value. In fact, a model that would perform worse than a simple coin flip in a simple binary classification (A or B) should not be considered.  

**What is a Confusion Matrix?**

The confusion Matrix is the essential element to calculate the metric described above. In a simple classification problem with a binary classification, we can identify 4 possible outcomes. The first is that the model correctly identify when the label is positive and negative, leading to a true positive and true negative. For example, a classification problem where a model has to identify if a picture contains a car or not. If the model see a picture with a car and label that "with car" (true positive) or identify a picture without car as "without car" (true negative).
On the other hand a model could wrongly identify a picture with a car as "without a car "(false negative) and a picture without a car as having a car (false positive). Of course, a confusion matrix can be scaled from binary classification to multi-class classification. In that case the matrix would not be a 2X2 but have as many rows and colomuns as classes.    
## Task 2

Your code should:
Login to W&B (Tip: you can use ENTRYPOINT in a Dockerfile to run a shell script that logs you in (see
below)):  
This was one of the most headache enducing tasks, which would end up with the "easiest" solution. But it wouldn't be a coding project without these type of headaches, right? :')  
Creating a entry_point.sh and the respective .env with the AUTH key file worked out easily. But then the difficulties began.
  1. Entrypoint firstly didn't recognize the sh. file cause we didn't know ```ENTRYPOINT ["docker-entrypoint.sh]```  wasn't enough: The solution ```ENTRYPOINT ["sh", "docker-entrypoint.sh"]``` ended up working for running and building the container with dockerfile
```
docker run --env-file=.env --rm -it  dstoolkitsproject:1.0.12
```
  2. For docker-compose this solution would end up working then, right? right? **WRONG** It was then a whole other story. The ENTRYPOINT statement didn't end up working cause docker-compose up could not find the .env file. We tried defining the env file in the ```docker-compose up``` statement, with:  

```
  docker-compose --env-file=.env -f "docker-compose.yml" up -d --build
```
3. This didn't end up working either and after hours of stackoverflow exploration changing the docker-compose and adding a env_file: statement to the dockerfile image ended up working. 
```
    env_file:
      - .env
```




- Train a Model  
We used the same model as we did in previous task. Adding Wandb statements to different segments of the code to not just log our model but also interesting data.
```
wandb.init(project="ds_toolkits_project", entity="unilu-dstoolkits")
```
- wandb nicely logs most of the necessary metrics the model produces. 
As you can see here: https://wandb.ai/unilu-dstoolkits
It logs accuracy, loss, epochs and other interesting metrics.

- Save and upload the trained model  
After every finished run, wandb saves the best model as "model-best.h5" in your file section. You can then easily download it from there.

- Commitdata:  
Commit Hash's didn't seem to log eventhough our github repos were connected to the project. We set up "file save on runs" in the settings and that basically allows us to see what was changed (diff.patch file) and how the code looked at initialization. 

For the last part of the task: 

skilled-deluge-10 run with binary crossentropy which isn't made for categorical data like our own. 



## Task 3 
Run the docker image while being in the DS_Toolkits_Projects (or wherever you save your .env file) and it will login to wandb and run the code.

´´´
docker run --env-file=.env --rm -it  dstoolkitsproject:1.0.12
´´´  
´´´
docker-compose --env-file=.env -f "docker-compose.yml" up -d --build
´´´


## Task 4



## Task 5