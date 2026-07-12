# Simulated structural office communications from the Dean and COD
OFFICE_RESPONSES = {
    "greeting": (
        "Hello! Welcome to the DeKUT School of Computer Science & IT FAQ Assistant.\n\n"
        "How can I assist you today? You can query me about:\n"
        "• Exam Timetables 🗓️\n"
        "• Missing Marks Form procedures 📝\n"
        "• Industrial Attachment Logbook submissions 💼\n"
        "• Graduation List clearance updates 🎓\n"
        "• Setting up appointments with the COD or Dean 🏛️"
    ),
    "exam_timetable": (
        "Message from the Dean's Desk:\n"
        "The provisional examination timetable for this semester has been uploaded to the student portal. "
        "Please review it immediately and raise any clashing concerns with your respective class representatives."
    ),
    "missing_marks": (
        "Message from the COD (Computer Science & IT):\n"
        "To report missing marks, please download the Missing Marks Form from the university website, "
        "attach your evidence of exam attendance/coursework grades, and hand it to the department clerk for processing."
    ),
    "attachment_logbook": (
        "Message from the Industrial Attachment Coordinator:\n"
        "All completed logbooks and industrial supervisor evaluation forms must be handed over physically "
        "to the School office before the conclusion of the second week of the new academic semester."
    ),
    "graduation_list": (
        "Message from the Dean's Desk:\n"
        "The 1st provisional graduation list is currently under verification. Ensure you have fully paid all "
        "outstanding fees and cleared with your department to guarantee inclusion in the upcoming final ledger."
    ),
    "office_appointment": (
        "Message from the Administration:\n"
        "The Dean is available for open consultation on Tuesdays and Thursdays from 2:00 PM to 4:00 PM. "
        "To book an official appointment with the COD, write directly to cod-csit@dekut.ac.ke."
    ),
    "unknown": (
        "I could not clearly define that query under standard department rules. "
        "Please structure your question clearly regarding exams, missing marks, logbooks, graduation, or appointments."
    )
}

def get_simulated_response(intent_category):
    return OFFICE_RESPONSES.get(intent_category, OFFICE_RESPONSES["unknown"])