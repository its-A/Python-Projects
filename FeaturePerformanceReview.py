'''--- Project: The Feature Performance Review ----
Junior Data Analyst for a mobile app for learning languages.
At the beginning of the quarter, the company launched a new feature called Streak Builder. The feature encourages learners to return every day and complete short study tasks.

Now the company wants a short review of the feature’s early performance.

Two different audiences need this review, and each one expects a different type of communication:

the Product Insights Team, which wants a careful and evidence-based summary,
the Executive Leadership Team, which wants a short, clear presentation focused on business meaning and next steps.

Task is to read the data, interpret the visuals critically and prepare communication for both a technical and non-technical audience.'''


#dataset
monthly_lesson_completions = [
    {"month": "Jan", "completed_lessons": 420},
    {"month": "Feb", "completed_lessons": 455},
    {"month": "Mar", "completed_lessons": 510},
    {"month": "Apr", "completed_lessons": 590},
    {"month": "May", "completed_lessons": 660},
    {"month": "Jun", "completed_lessons": 710}
]

average_app_rating = [
    {"period": "Before", "rating": 4.1},
    {"period": "After", "rating": 4.3}
]

monthly_support_tickets = [
    {"month": "Jan", "tickets": 88},
    {"month": "Feb", "tickets": 94},
    {"month": "Mar", "tickets": 101},
    {"month": "Apr", "tickets": 116},
    {"month": "May", "tickets": 128},
    {"month": "Jun", "tickets": 137}
]

#Task 1: inspect the dataset & summarize the main metrics
#print the lesson completion values, app rating values & support ticket values

print("Monthly Lesson Completions:")
for entry in monthly_lesson_completions:
    print(f"{entry['month']}: {entry['completed_lessons']}")   

print("\nAverage App Rating:")
for entry in average_app_rating:
    print(f"{entry['period']}:{entry['rating']}") 

print("\nMonthly Support Tickets:")
for entry in monthly_support_tickets:
    print(f"{entry['month']}: {entry['tickets']}") 

#The dataset tracks engagement, user sentiment, and support demand after the feature launch. 
# Lesson completions show whether people are using the app more, app rating gives a rough signal about user satisfaction
# support tickets may show whether growth is creating more friction or more requests for help.

#Task 2: Analyze the Trend Using Code & Build a Short Data Story

#Calculate the total increase and percentage growth from January to June
start_value = monthly_lesson_completions[0]['completed_lessons']
end_value = monthly_lesson_completions[-1]['completed_lessons']

total_increase = end_value - start_value
percentage_growth = round((total_increase / start_value) * 100, 2)
print(f"\nTotal increase in lesson completions from Jan to Jun: {total_increase}")
print(f"Percentage growth in lesson completions from Jan to Jun: {percentage_growth}%")

#Observation: There is a clear upward trend in monthly lesson completions, with a significant increase of 290 lessons from January to June, representing a 69.05% growth.

#Recommendation: Given the positive trend in lesson completions, it would be beneficial to continue promoting the Streak Builder feature and consider additional incentives to further boost user engagement. Additionally, monitoring user feedback and support tickets closely can help identify any potential issues as the user base grows.

#Task 3: Evaluate the Visuals Carefully
before_rating = average_app_rating[0]['rating']
after_rating = average_app_rating[1]['rating']

start_value = monthly_lesson_completions[0]['completed_lessons']
end_value = monthly_lesson_completions[-1]['completed_lessons']

#Calculate the percentage increase in app rating
rating_increase = after_rating - before_rating
percentage_rating_increase = round((rating_increase / before_rating) * 100, 2)
print(f"\nIncrease in app rating: {rating_increase}")
print(f"Percentage increase in app rating: {percentage_rating_increase}%")

#Observation: The average app rating increased from 4.1 to 4.3 after the launch of the Streak Builder feature, which is a positive sign of improved user satisfaction. The percentage increase in app rating is approximately 4.88%.

#Recommendation: The increase in app rating suggests that users are responding well to the new feature. It would be beneficial to gather qualitative feedback from users to understand what aspects of the Streak Builder they find most appealing and if there are any areas for improvement. This can help guide future updates and enhancements to further boost user satisfaction.

#Line Chart:
#The chart clearly shows a steady increase in lesson completions from 420 to 710. The scale and progression make the trend easy to interpret, and the design supports the message effectively.

#Bar chart:
#The chart does not represent the change fairly because the Y-axis is truncated, which makes the difference between 4.1 and 4.3 appear larger than it really is. Based on the data, the increase is small (0.2 points), so the visual exaggerates the change.


#Task 4: Compute Key Metrics

#Calculate the total increase & percentage growth in lesson completions
start_lessons = monthly_lesson_completions[0]['completed_lessons']
end_lessons = monthly_lesson_completions[-1]['completed_lessons']

lesson_increase = end_lessons - start_lessons
lesson_growth = round((lesson_increase / start_lessons) * 100,2)

#Calculate the change in app rating
rating_before = average_app_rating[0]['rating']
rating_after = average_app_rating[1]['rating']

rating_change = round(rating_after - rating_before, 2)

#Calculate the total increase in support tickets
start_tickets = monthly_support_tickets[0]['tickets']
end_tickets = monthly_support_tickets[-1]['tickets']

ticket_increase = end_tickets - start_tickets

#print the results
print(f"\nLesson Increase: {lesson_increase}")
print(f"Lesson Growth (%): {lesson_growth}%")
print(f"Rating change: {rating_change}")
print(f"Support ticket increase: {ticket_increase}")


#Task 5: Build a Technical Report
'''Technical Report: Feature Performance Review
1. Objective
Evaluate the early performance of the Streak Builder feature using engagement, rating, and support data.
2. Key Metrics
- Lesson completions increased from 420 to 710 (+290, ~69% growth).
- App rating increased from 4.1 to 4.3 (+0.2).
- Support tickets increased from 88 to 137 (+49).
3. Visual Evaluation
- The line chart accurately represents the steady increase in lesson completions.
- The bar chart exaggerates the rating change due to its axis scaling and should be interpreted carefully.
4. Interpretation
The feature appears to increase user engagement significantly. However, the rise in support tickets suggests that increased usage may also introduce friction or additional user needs.
5. Recommendation
Continue monitoring engagement while investigating support ticket categories to better understand user experience during growth.
6. Next Steps
Segment users and support tickets to identify whether specific groups are driving both engagement and support demand.'''

#Task 6: Build an Executive Summary
#Opening – what was analyzed: the Streak Builder feature's early performance
#Main finding – the most important result: significant increase in lesson completions (up 69%) and a modest improvement in app rating (up 0.2 points), but also a notable increase in support tickets (up 49).
#Why it matters – business impact: increased engagement is positive for growth, but the rise in support tickets indicates potential challenges that need to be addressed to maintain user satisfaction.
#Recommendation – what should happen next: continue promoting the feature while closely monitoring user feedback and support requests to ensure we can address any emerging challenges effectively. Further analysis of support ticket data will help us understand user needs and improve the overall experience as we scale.
'''Executive Summary: Streak Builder Performance:
The Streak Builder feature has shown promising early results, with a significant increase in lesson completions (up 69%) and a modest improvement in app rating (up 0.2 points). However, the increase in support tickets (up 49) indicates that while more users are engaging with the app, they may also be encountering issues or seeking more assistance. We recommend continuing to promote the feature while closely monitoring user feedback and support requests to ensure we can address any emerging challenges effectively. Further analysis of support ticket data will help us understand user needs and improve the overall experience as we scale.'''

#Task 7: Plan How to Communicate the Results to both Audiences
#For the Product Insights Team:
#- Use the technical report format to provide a detailed analysis of the data, including key metrics, visual evaluations, and interpretations.
#- Include specific recommendations based on the data analysis and suggest next steps for further investigation.
#- Encourage discussion and feedback from the team to refine the analysis and recommendations.

#For the Executive Leadership Team:
#- Use the executive summary format to present a concise and clear overview of the findings, focusing on the main results and their business implications.
#- Highlight the key metrics that demonstrate the feature's performance and the potential challenges indicated by the support ticket increase.
#- Provide actionable recommendations that are easy to understand and implement, emphasizing the importance of monitoring user feedback and support requests as the feature continues to grow.