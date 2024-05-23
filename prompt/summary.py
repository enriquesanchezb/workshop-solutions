prompt = {
    "systemMessagePromptTemplate": "As an assistant, your objective is to provide a summary that highlights the most relevant information in JSON format. Ensure that the JSON object contains two keys: 'summary' and 'title'. The summary should be no more than 100 characters, and the title should be shorter than the summary.",
    "humanPromptTemplate": ""
    + "Following is a text transcript obtained."
    + "Please complete these two tasks in JSON format:"
    + "1) Provide a brief and concise summary, limited to 100 characters."
    + "2) Provide a title for the summarization, which must be shorter than the summary."
    + "Transcript: ```{text}```"
    + "Examples:"
    + "Transcript: ```The weather today is sunny with a high of 75 degrees. It's a perfect day for a picnic.```"
    + "Response: {{"
    + "'title': 'Sunny Day',"
    + "'summary': 'Weather is sunny, high of 75 degrees, great for a picnic.'"
    + "}}"
    + "Transcript: ```The company's quarterly earnings report showed a 20% increase in revenue and a 15% increase in profits.```"
    + "Response: {{"
    + "'title': 'Earnings Up',"
    + "'summary': 'Quarterly report: 20% revenue increase, 15% profit increase.'"
    + "}}"
    + "Please ensure the title is shorter than the summary.",
}
