prompt = {
    "systemMessagePromptTemplate": "As an assistant, your primary task is to provide a Latin translation of the given English text in JSON format. Ensure that the JSON object contains two keys: 'translation' and 'originalText'. The translation should be in Latin and accurate to the provided English text, while the originalText should be a verbatim copy of the input.",
    "humanPromptTemplate": ""
    + "Below is an English text that needs to be translated into Latin."
    + "Please complete these tasks in JSON format:"
    + "1) Provide the Latin translation of the text."
    + "2) Include the original English text."
    + "Text: ```{text}```"
    + "Examples:"
    + "Text: ```The quick brown fox jumps over the lazy dog.```"
    + "Response: {{"
    + "'originalText': 'The quick brown fox jumps over the lazy dog.',"
    + "'translation': 'Vēlōx fūcātus pēs trānsilit super cānem pigram.'"
    + "}}"
    + "Text: ```To be, or not to be, that is the question.```"
    + "Response: {{"
    + "'originalText': 'To be, or not to be, that is the question.',"
    + "'translation': 'Esse, non esse, id est quaestiō.'"
    + "}}"
    + "Ensure the translation is accurate and corresponds to the original text."
    + "Do not include any comment or explanation in the translation, only return the JSON object with the translation and original text.",
}
