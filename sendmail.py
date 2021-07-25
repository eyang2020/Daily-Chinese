import yagmail

yag = yagmail.SMTP("example@gmail.com", "password")

# get daily char message
emailFile = open("/emailtemplates.txt", "r").readlines()
message = emailFile[0]
message = message[1:-2]

# overwrite emailtemplates.txt with the daily message removed
with open("/emailtemplates.txt", "w") as deleteFile:
    deleteFile.write("")
with open("/emailtemplates.txt", "a") as rewriteFile:
    rewriteFile.write("")
    for eachTemplate in emailFile[1:]:
        rewriteFile.write(eachTemplate)

# email handler
inputFile = open("/receiverlist.txt", "r").readlines()
emailList = []
for eachEmail in inputFile:
    emailList.append(eachEmail.strip())
for eachEmailAddress in emailList:
    yag.send(eachEmailAddress, 'Daily Chinese', message)