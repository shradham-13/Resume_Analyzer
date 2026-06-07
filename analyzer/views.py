import os
import re
from groq import Groq
from django.shortcuts import render
from .models import Resume
import PyPDF2
import docx

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

def extract_ats_score(analysis_text):
    match = re.search(r'ATS Score[:\s]*(\d+)', analysis_text)
    if match:
        return int(match.group(1))
    return 75

def analyze_resume(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        resume_file = request.FILES.get('resume_file')

        if resume_file.name.endswith('.pdf'):
            text = extract_text_from_pdf(resume_file)
        else:
            text = extract_text_from_docx(resume_file)

        prompt = f"""
        Analyze this resume and provide:
        1. ATS Score out of 100
        2. Strong points
        3. Missing keywords
        4. Improvements needed
        5. Overall feedback

        Resume:
        {text}
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )

        analysis = response.choices[0].message.content
        ats_score = extract_ats_score(analysis)

        Resume.objects.create(
            name=name,
            email=email,
            resume_file=resume_file,
            analysis_result=analysis,
            ats_score=ats_score
        )

        return render(request, 'analyzer/result.html', {
            'analysis': analysis,
            'name': name,
            'score': ats_score
        })

    return render(request, 'analyzer/index.html')