from docx import Document
from docx.shared import Pt
from datetime import datetime
import os


def generate_document(user_request: str, content: str) -> str:
    """
    Generate a professional Word document.
    """

    os.makedirs("output", exist_ok=True)

    document = Document()

    # Title
    title = document.add_heading("AI Generated Business Document", level=1)
    title.runs[0].font.size = Pt(20)

    # Metadata
    document.add_heading("Request", level=2)
    document.add_paragraph(user_request)

    document.add_heading("Generated On", level=2)
    document.add_paragraph(
        datetime.now().strftime("%d %B %Y %I:%M %p")
    )

    # Main Content
    document.add_heading("Document", level=2)
    document.add_paragraph(content)

    output_path = "output/report.docx"

    document.save(output_path)

    return output_path