from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Rule-based chatbot function
# Rule-based chatbot function
def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    college_link = "https://gmiu.edu.in/gmiu/website/#"

    if user_input == 'quit':
        return "Thank you for chatting. Have a great day!"

    elif any(word in user_input for word in ['hello', 'hi', 'hey', 'greetings']):
        return "Hello! How can I help you today?"

    elif any(word in user_input for word in ['bye', 'goodbye', 'see you']):
        return "Goodbye! Have a great day!"

    elif 'thank' in user_input:
        return "You're welcome! Is there anything else I can help with?"

    elif any(word in user_input for word in ['course', 'classes', 'subjects']):
        if 'computer science' in user_input:
            return f"The Computer Science program includes courses like Programming, Data Structures, Algorithms, and AI. More info: {college_link}"
        elif 'business' in user_input:
            return f"The Business program offers courses in Management, Marketing, Finance, and Entrepreneurship. More info: {college_link}"
        elif 'engineering' in user_input:
            return f"Engineering programs include Mechanical, Electrical, and Civil Engineering. More info: {college_link}"
        else:
            return f"We offer programs in Computer Science, Business, Engineering, and more. Which program interests you? Details here: {college_link}"

    elif any(word in user_input for word in ['schedule', 'timing', 'when', 'time']):
        if 'exam' in user_input:
            return f"Final exams are scheduled for Dec 15-22. Check the portal for your exact schedule: {college_link}"
        elif 'class' in user_input or 'lecture' in user_input:
            return f"Classes run from 9 AM to 4 PM, Monday–Friday. Schedule varies by course. See more: {college_link}"
        else:
            return f"Are you asking about class schedules, exam schedules, or something else? Visit: {college_link}"

    elif any(word in user_input for word in ['professor', 'faculty', 'teacher', 'instructor']):
        if 'computer science' in user_input:
            return f"The CS department has 15 faculty, including Dr. Smith (AI) and Dr. Johnson (Data Science). Info: {college_link}"
        elif 'contact' in user_input or 'email' in user_input:
            return f"Find faculty contact info on the university website directory: {college_link}"
        else:
            return f"We have experienced faculty across all departments. Which department interests you? See more: {college_link}"

    elif any(word in user_input for word in ['library', 'lab', 'cafeteria', 'gym', 'facility']):
        if 'library' in user_input:
            return f"Library open: 8 AM–10 PM weekdays, 10 AM–6 PM weekends. More: {college_link}"
        elif 'lab' in user_input:
            return f"Computer labs in Building A & B. Open until 8 PM weekdays. More info: {college_link}"
        elif 'cafeteria' in user_input or 'food' in user_input:
            return f"Cafeteria serves breakfast, lunch, dinner. Meal plans available. More info: {college_link}"
        elif 'gym' in user_input:
            return f"Gym open 6 AM–10 PM. Includes cardio, weights, and pool. More: {college_link}"
        else:
            return f"Our campus has library, labs, cafeteria, and gym. Which one do you want details about? Info: {college_link}"

    elif any(word in user_input for word in ['admission', 'apply', 'requirement', 'deadline']):
        if 'deadline' in user_input:
            return f"Application deadline for Fall semester is Jan 31st. Details: {college_link}"
        elif 'requirement' in user_input:
            return f"Requirements: application, transcripts, and test scores. Vary by program. More: {college_link}"
        else:
            return f"For admission details, visit the admissions office or website: {college_link}"

    elif any(word in user_input for word in ['where', 'location', 'address', 'contact', 'phone']):
        return f"University is at 123 Education Street, Knowledge City. Call (555) 123-4567. Website: {college_link}"

    else:
        return f"I'm not sure I understand. I can help with courses, schedules, faculty, facilities, and admissions. Visit: {college_link}"



# API route for chatbot
@app.route("/get", methods=["POST"])
def get_response():
    user_input = request.json.get("message")
    response = chatbot_response(user_input)
    return jsonify({"response": response})


# Home page route
@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
