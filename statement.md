Symptom Helper Project Statement
1.) Statement
The goal is to address the need for quick, accessible, non-medical, common-sense advice when an individual experiences mild, everyday symptoms. Users often search for immediate 
home remedies or self-care suggestions for minor discomforts like headaches, colds, or stomach aches. This simple application provides immediate, pre-defined comforting 
suggestions to help users feel better or decide on the next steps, while clearly stating that it is not a substitute for professional medical guidance.

2.)Scope of the Project
The scope of this project is limited to a single, standalone desktop application built using Python's tkinter library. It functions as a simple key-value look-up tool.
1.	Input: Accepts text input of a known symptom (e.g., "cold," "headache").
2.	Logic: Compares the input to a small, hardcoded dictionary of symptoms.
3.	Output: Displays a pre-written, comforting suggestion corresponding to the symptom, or a message indicating the symptom is unknown.
4.	Disclaimer: The application includes a clear, explicit disclaimer that the advice is not medical.
It does not include networking, external database connectivity, user personalization, or complex diagnostic logic.

3.)Target Users
The primary target users are:
•	Individuals experiencing common, mild, and self-identifiable symptoms (such as a cold, headache, or sore throat).
•	Anyone seeking quick, general, comforting self-care ideas and reminders (like drinking water or resting) rather than professional medical analysis.
•	Novice programmers looking for a simple, functional example of a Python tkinter application with basic input/output handling.

4.)High-Level Features
1.	Symptom Input Field: A text box (tk.Entry) for the user to type the symptom they are experiencing.
2.	Suggestion Retrieval: A function (showStuff) to process the user's input and look up the corresponding advice.
3.	Dynamic Output Display: A large output area (tk.Label) that displays the retrieved suggestion, error messages (if the input is unknown), or a prompt (if the input is empty).
4.	Clear Input Management: The input field is automatically cleared after the "Get Suggestion" button is pressed.
5.	Non-Medical Disclaimer: A visible, italicized label emphasizing that the advice provided is general and not medical.

