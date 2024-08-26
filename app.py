from docxtpl import DocxTemplate, InlineImage
import datetime as dt
import pypandoc

# Specify input and output file names
input_file = 'docs/invitation.docx'
output_file = 'docs/invitation.pdf'

# create a document object
doc = DocxTemplate("inviteTmpl.docx")

# create context dictionary
context = {
    "todayStr": dt.datetime.now().strftime("%d-%b-%Y"),
    "recipientName": "Chaitanya",
    "evntDtStr": "21-Oct-2021",
    "venueStr": "the beach",
    "senderName": "Sanket",
}

# inject image into the context
context['bannerImg'] = InlineImage(doc, 'images/party_banner_0.png')

# render context into the document object
doc.render(context)

# save the document object as a word file
doc.save(input_file)


# Convert the DOCX file to PDF
output = pypandoc.convert_file(input_file, 'pdf', outputfile=output_file)