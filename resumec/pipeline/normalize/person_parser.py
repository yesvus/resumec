from resumec.schemas.person import Person, Contact, Education, SkillCategory, Experience, Project

def parse_person(raw_markdown: str) -> Person:
    """Parses raw markdown CV into a structured Person schema."""
    # This is a mock implementation. A real one would split sections via regex
    # and map them into the models.
    return Person(
        name="Jane Doe",
        summary="A highly skilled software engineer with passion for pipelines.",
        contact=Contact(email="jane.doe@example.com", github="janedoe", linkedin="janedoe"),
        education=[
            Education(institution="University of Tech", degree="MSc Computer Science", start_date="2018", end_date="2020", gpa=3.9)
        ],
        skills=[
            SkillCategory(name="Languages", skills=["Python", "JavaScript", "SQL", "Go"]),
            SkillCategory(name="Frameworks", skills=["FastAPI", "React", "Docker"])
        ],
        experience=[
            Experience(
                company="Old Corp",
                role="Backend Developer",
                start_date="2020",
                end_date="2023",
                bullets=["Developed robust APIs.", "Improved performance by 20%."]
            )
        ],
        projects=[
            Project(
                name="Data Pipeline",
                description="Built an ETL pipeline using Airflow.",
                technologies=["Python", "Airflow", "PostgreSQL"],
                bullets=["Processed 100GB of data daily.", "Automated reporting."]
            )
        ]
    )
