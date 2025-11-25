# pdf_generator.py
# Türkçe/İngilizce PDF üretme modülü

from reportlab.platypus import Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

from translator import translate_trigger, behavior_en, diagnosis_en, action_en

# DejaVu fontunu kaydet
pdfmetrics.registerFont(TTFont('DejaVu', 'DejaVuSans.ttf'))

# Paragraf stil
para_style = ParagraphStyle(
    name='TR_EN',
    fontName='DejaVu',
    fontSize=9,
    textColor=colors.white,
    leading=12
)

def create_bilingual_pdf(df, filename="output/AI_Report_TR_EN.pdf"):
    pdf = SimpleDocTemplate(filename, pagesize=letter)
    elements = []

    for idx, row in df.iterrows():
        
        # Çift dilli text
        trigger_tr = row['trigger']
        trigger_en = translate_trigger(trigger_tr)

        behavior_tr = row['behavior']
        behavior_en_text = behavior_en()

        diagnosis_tr = row['diagnosis']
        diagnosis_en_text = diagnosis_en()

        action_tr = row['action']
        action_en_text = action_en()

        data = [
            ["Trigger", Paragraph(f"TR: {trigger_tr}<br/>EN: {trigger_en}", para_style)],
            ["Behavior", Paragraph(f"TR: {behavior_tr}<br/><br/>EN: {behavior_en_text}", para_style)],
            ["Diagnosis", Paragraph(f"TR: {diagnosis_tr}<br/><br/>EN: {diagnosis_en_text}", para_style)],
            ["Action", Paragraph(f"TR: {action_tr}<br/><br/>EN: {action_en_text}", para_style)],
        ]

        # Profesyonel tablo dizaynı
        table = Table(data, colWidths=[120, 380])
        table.setStyle(TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'DejaVu'),
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1E1E1E")),
            ('BACKGROUND', (0,1), (-1,-1), colors.HexColor("#2A2A2A")),
            ('TEXTCOLOR', (0,0), (-1,-1), colors.white),
            ('GRID', (0,0), (-1,-1), 0.3, colors.gray),
            ('BOX', (0,0), (-1,-1), 0.8, colors.gray),
            ('LEFTPADDING', (0,0), (-1,-1), 6),
            ('RIGHTPADDING', (0,0), (-1,-1), 6),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ]))

        title = Paragraph(
            f"<b>INCIDENT #{int(row['event_id'])}</b>",
            ParagraphStyle(
                name="Title",
                fontName="DejaVu",
                fontSize=12,
                textColor=colors.white
            ),
        )

        elements.append(title)
        elements.append(Spacer(1, 8))
        elements.append(table)
        elements.append(Spacer(1, 20))

    pdf.build(elements)
    return filename
