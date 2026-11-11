
import streamlit as st


# --------------------------------
# 1. Page Configuration
# --------------------------------

st.set_page_config(
    page_title="Student Grade Manager",
    page_icon="🎓",
    layout="wide"
)


# --------------------------------
# 2. Initialize Session State
# --------------------------------

if "students" not in st.session_state:
    st.session_state.students = []


# --------------------------------
# 3. Grading Function
# --------------------------------

def calculate_grade(mark):

    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


# --------------------------------
# 4. Application Title
# --------------------------------

st.title("🎓 Student Grade Manager")

st.write(
    "Add students, calculate grades, "
    "and monitor class performance."
)

st.divider()


# --------------------------------
# 5. Add Student Form
# --------------------------------

st.subheader("➕ Add New Student")

with st.form("student_form"):

    student_name = st.text_input(
        "Student Name",
        placeholder="Enter student name"
    )

    student_mark = st.number_input(
        "Student Mark",
        min_value=0,
        max_value=100,
        value=0,
        step=1
    )

    submit = st.form_submit_button("Add Student")

    if submit:

        if not student_name.strip():

            st.error("Please enter a student name.")

        elif not 0 <= student_mark <= 100:

            st.error("Mark must be between 0 and 100.")

        else:

            student = {
                "Name": student_name.strip(),
                "Mark": student_mark,
                "Grade": calculate_grade(student_mark)
            }

            st.session_state.students.append(student)

            st.success(
                f"{student_name} added successfully!"
            )


st.divider()


# --------------------------------
# 6. Display Student Results
# --------------------------------

st.subheader("📋 Student Results")

students = st.session_state.students

if students:

    # Create table header

    header = st.columns([3, 1, 1])

    header[0].markdown("**Student Name**")
    header[1].markdown("**Mark**")
    header[2].markdown("**Grade**")

    st.divider()

    # Display each student

    for student in students:

        row = st.columns([3, 1, 1])

        row[0].write(student["Name"])
        row[1].write(student["Mark"])
        row[2].write(student["Grade"])

        st.divider()

else:

    st.info(
        "No students added yet. "
        "Add your first student above."
    )


# --------------------------------
# 7. Class Performance Metrics
# --------------------------------

st.subheader("📊 Class Performance")

if students:

    marks = [
        student["Mark"]
        for student in students
    ]

    average = sum(marks) / len(marks)

    highest = max(marks)

    lowest = min(marks)

    total_students = len(students)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Students", total_students)

    col2.metric("Class Average", f"{average:.2f}")

    col3.metric("Highest Mark", highest)

    col4.metric("Lowest Mark", lowest)

else:

    st.info(
        "Class statistics will appear "
        "after adding students."
    )


# --------------------------------
# 8. Footer
# --------------------------------

st.divider()

st.caption(
    "Student Grade Manager | Day 3 - Streamlit Project"
)
